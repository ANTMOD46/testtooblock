from django.shortcuts import render
from . models import Course
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
# Create your views here.
def course_list(request):
    courses = Course.objects.all()
    return render (request, 'list_courses.html', {'mod': courses})



def course_idsearch(request):
    serch = request.GET.get("course_id",'')
    courses  = Course.objects.filter(Course_id__icontains = serch)
    return render(request, 'course_seach.html',{'mod':courses})
    


def course_nameseach(request) :
    seach = request.GET.get('course_name','')
    courses = Course.objects.filter(Course_name__icontains = seach)
    return render(request,'course_namesearch.html',{"mod":courses})


class CourseUpdateView(UpdateView):
    model = Course
    fields = '__all__'
    template_name = 'courseupdate.html'
    success_url = reverse_lazy('course_list')

from django.views.generic import DeleteView
class CourseDeleteView(DeleteView):
    model = Course
    template_name='coursedelete.html'
    success_url = reverse_lazy('course_list')

