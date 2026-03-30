from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from courses.models import *
from django.contrib import messages

# Create your views here.

from django.http import HttpResponse

@login_required
def enroll_course(request, course_id):
    if request.user.role != 'student':
        return HttpResponse("Only students can enroll")

    course = Course.objects.get(id=course_id)

    if Enrollment.objects.filter(student=request.user, course=course).exists():
        messages.warning(request, "You are already enrolled!")
        return redirect('course_detail', id=course_id)

    Enrollment.objects.create(
        student=request.user,
        course=course
    )

    messages.success(request, "Enrolled successfully!")
    return redirect('course_detail', id=course_id)

@login_required
def student_dashboard(request):
    if request.user.role != 'student':
        return HttpResponse("Only students can access dashboard")

    enrollments = Enrollment.objects.filter(student=request.user)

    return render(request, 'enrollments/dashboard.html', {
        'enrollments': enrollments
    })