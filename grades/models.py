from django.db import models

# Create your models here.
from django.db import models
from students.models import StudentProfile
from courses.models import Course

class Grade(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)  # e.g., A, B, C, 85%

    class Meta:
        unique_together = ('student', 'course')
