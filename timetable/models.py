from django.db import models

# Create your models here.
from django.db import models
from courses.models import Course

class TimetableSlot(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day_of_week = models.IntegerField()  # 0=Monday, 6=Sunday
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['day_of_week', 'start_time']
