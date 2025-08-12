from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from .forms import AssignmentUploadForm
from django.contrib.auth.decorators import login_required
from students.models import StudentProfile
from django.contrib.auth.decorators import user_passes_test
from courses.models import Course
from attendance.models import AttendanceRecord
from grades.models import Grade


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'students/register.html', {'form': form})

def home(request):
    return render(request, 'students/home.html')

@login_required
def upload_assignment(request):
    student_profile = StudentProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = AssignmentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.student = student_profile
            assignment.save()
            return redirect('assignment_list')
    else:
        form = AssignmentUploadForm()
    return render(request, 'students/upload_assignment.html', {'form': form})

@login_required
def assignment_list(request):
    student_profile = StudentProfile.objects.get(user=request.user)
    assignments = student_profile.assignment_set.all()
    return render(request, 'students/assignment_list.html', {'assignments': assignments})
def is_teacher(user):
    return user.is_authenticated and user.is_teacher

@user_passes_test(is_teacher)
def teacher_dashboard(request):
    courses = Course.objects.all()
    student_count = sum(course.enrollment_set.count() for course in courses)
    total_attendance = AttendanceRecord.objects.count()
    total_grades = Grade.objects.count()
    context = {
        'courses': courses,
        'student_count': student_count,
        'total_attendance': total_attendance,
        'total_grades': total_grades,
    }
    return render(request, 'students/teacher_dashboard.html', context)
