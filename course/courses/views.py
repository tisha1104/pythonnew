from django.shortcuts import render,redirect, get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *

# Create your views here.

def instructor_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.role != 'instructor':
            return HttpResponse("Only instructors allowed")
        return view_func(request, *args, **kwargs)
    return wrapper

@login_required
@instructor_required
def create_course(request):
    form = CourseForm(request.POST or None)

    if form.is_valid():
        course = form.save(commit=False)
        course.instructor = request.user
        course.save()
        return redirect('course_list')

    return render(request, 'courses/create_course.html', {'form': form})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def home(request):
    return render(request, 'core/home.html')



from enrollments.models import Enrollment

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)

    is_enrolled = False

    if request.user.is_authenticated:
        is_enrolled = Enrollment.objects.filter(
            student=request.user,
            course=course
        ).exists()

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'is_enrolled': is_enrolled   
    })


@login_required
def instructor_dashboard(request):

    if request.user.role != 'instructor':
        return redirect('home')

    courses = Course.objects.filter(instructor=request.user)

    return render(request, 'instructor_dashboard.html', {
        'courses': courses
    })


@login_required
def edit_course(request, id):
    course = get_object_or_404(Course, id=id)

    if course.instructor != request.user:
        return redirect('home')

    form = CourseForm(request.POST or None, instance=course)

    if form.is_valid():
        form.save()
        return redirect('instructor_dashboard')

    return render(request, 'courses/edit_course.html', {'form': form})

@login_required
def delete_course(request, id):
    course = get_object_or_404(Course, id=id)

    if course.instructor != request.user:
        return redirect('home')

    course.delete()
    return redirect('instructor_dashboard')