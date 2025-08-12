from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from students.models import StudentProfile
from .forms import EnrollmentForm
from .models import Enrollment

@login_required
def enroll_course(request):
    student_profile = StudentProfile.objects.get(user=request.user)
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            course = form.cleaned_data['course']
            Enrollment.objects.get_or_create(student=student_profile, course=course)
            return redirect('enrollments')
    else:
        form = EnrollmentForm()
    return render(request, 'courses/enroll.html', {'form': form})

@login_required
def enrollments(request):
    student_profile = StudentProfile.objects.get(user=request.user)
    courses = Enrollment.objects.filter(student=student_profile)
    return render(request, 'courses/enrollments.html', {'courses': courses})
