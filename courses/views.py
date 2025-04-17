from django.views.generic import TemplateView

from courses.models import Course


class IndexView(TemplateView):
    template_name = 'courses/index.html'


class CourseView(TemplateView):
    template_name = 'courses/course.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['courses'] = Course.objects.all()

        course_slug = self.kwargs.get('course_slug')
        if course_slug:
            context['course'] = Course.objects.filter(course_slug=course_slug).first()

        return context


class AboutView(TemplateView):
    template_name = 'courses/about.html'


