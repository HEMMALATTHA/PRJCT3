from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.attendance_list, name='attendance_list'),
    path('calendar/', views.attendance_calendar, name='attendance_calendar'),
]
