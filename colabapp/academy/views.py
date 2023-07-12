from django.shortcuts import render
from .models import Course

# Create your views Academy.

def v_index(request):
    context = {
        'course1': Course.objects.get(name = 'BD1'),
        'course2': Course.objects.get(name = 'BD2')
    }
    return render(request, 'index.html', context) #Enlaza la view de Academy con el html

def v_course(request, course_id):
    context = {
        'course': Course.objects.get(id = course_id)
    }
    return render(request, 'course.html', context)
