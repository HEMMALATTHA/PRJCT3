from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import TimetableSlot
from django.contrib.auth.decorators import login_required

@login_required
def timetable(request):
    slots = TimetableSlot.objects.all().order_by('day_of_week', 'start_time')
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    return render(request, 'timetable/timetable.html', {'slots': slots, 'days': days})
