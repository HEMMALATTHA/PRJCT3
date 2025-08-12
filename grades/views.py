from django.shortcuts import render
import csv

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from students.models import StudentProfile
from .models import Grade

@login_required
def gradebook(request):
    student_profile = StudentProfile.objects.get(user=request.user)
    grades = Grade.objects.filter(student=student_profile)
    return render(request, 'grades/gradebook.html', {'grades': grades})
@login_required
def export_grades_csv(request):
    student = StudentProfile.objects.get(user=request.user)
    grades = Grade.objects.filter(student=student)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="grades.csv"'

    writer = csv.writer(response)
    writer.writerow(['Course', 'Grade'])
    for grade in grades:
        writer.writerow([grade.course.name, grade.grade])
    return response
