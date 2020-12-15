from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here.


class CourseListView(ListView):
    queryset = Course.objects.all()
    template_name = 'coursedetails.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CourseListView, self).get_context_data(*args, **kwargs)
        return context


def course_list_view(request):
    queryset = Course.objects.all()
    context = {
        'object_list': queryset,

    }
    return render(request, 'coursedetails.html', context)


def course_details_view(request, slug=None, *args, **kwargs):
    #queryset = Course.objects.get(pk=pk)
    queryset = get_object_or_404(Course, slug=slug)

    context = {
        'object': queryset,
        'slug': slug,

    }
    return render(request, 'coursedetails.html', context)


