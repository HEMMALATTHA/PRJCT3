from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import StudentProfile
from courses.models import Course
from .models import AttendanceRecord
from datetime import date, timedelta

@login_required
def attendance_list(request):
    student_profile = StudentProfile.objects.get(user=request.user)
    records = AttendanceRecord.objects.filter(student=student_profile).order_by('-date')
    return render(request, 'attendance/attendance_list.html', {'records': records})

@login_required
def attendance_calendar(request):
    # Simple calendar: show attendance for last 7 days for all courses student enrolled
    student = StudentProfile.objects.get(user=request.user)
    today = date.today()
    dates = [today - timedelta(days=i) for i in range(6, -1, -1)]
    courses = [en.course for en in student.enrollment_set.all()]
    attendance = {}
    for course in courses:
        attendance[course] = []
        for d in dates:
            rec = AttendanceRecord.objects.filter(student=student, course=course, date=d).first()
            attendance[course].append(rec.present if rec else False)
    return render(request, 'attendance/attendance_calendar.html', {'dates': dates, 'attendance': attendance})
