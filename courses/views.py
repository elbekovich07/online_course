from django.db.models import Avg, Count
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from courses.forms import StudentForm
from courses.models import Course, Category


class IndexView(TemplateView):
    template_name = 'courses/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.annotate(num_courses=Count('course')).order_by('-num_courses')
        context['courses'] = Course.objects.all()
        context['form'] = StudentForm()
        return context

    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:index')
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)



class CourseView(TemplateView):
    template_name = 'courses/course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['courses'] = Course.objects.all()
        context['categories'] = Category.objects.annotate(num_courses=Count('course')).order_by('-num_courses')


        course_slug = self.kwargs.get('course_slug')
        if course_slug:
            context['course'] = Course.objects.filter(course_slug=course_slug).first()


        return context


class AboutView(TemplateView):
    template_name = 'courses/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentForm()
        context['courses'] = Course.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:about')
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)


def course_list_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    courses = Course.objects.filter(category=category).annotate(avg_rating=Avg('reviews__rating'))
    return render(request, 'courses/course_list.html', {
        'courses': courses,
        'category': category,
    })


def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    return render(request, 'courses/course_detail.html', {'course': course})


def student_signup_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:index')  # yoki "Thank you" sahifa
    else:
        form = StudentForm()
    return render(request, 'courses/student_signup.html', {'form': form})
