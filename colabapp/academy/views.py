from django.shortcuts import render

# Create your views Academy.

def v_index(request):
    context = {}
    return render(request, 'index.html', context) #Enlaza la view de Academy con el html

def v_course(request):
    context = {}
    return render(request, 'course.html', context)
