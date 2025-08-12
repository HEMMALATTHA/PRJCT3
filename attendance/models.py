from django.db import models

# Create your models here.
from django.db import models
from students.models import StudentProfile
from courses.models import Course

class AttendanceRecord(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', 'course', 'date')
