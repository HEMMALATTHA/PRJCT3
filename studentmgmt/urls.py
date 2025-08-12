"""
URL configuration for studentmgmt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from students import views as student_views
from courses import views as course_views
from attendance import views as attendance_views
from grades import views as grades_views

from timetable import views as timetable_views
from notifications import views as notifications_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/register/', student_views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', student_views.home, name='home'),
    path('courses/enroll/', course_views.enroll_course, name='enroll_course'),
    path('courses/enrollments/', course_views.enrollments, name='enrollments'),

    path('attendance/list/', attendance_views.attendance_list, name='attendance_list'),
    path('attendance/calendar/', attendance_views.attendance_calendar, name='attendance_calendar'),

    path('grades/', grades_views.gradebook, name='gradebook'),
    path('grades/export_csv/', grades_views.export_grades_csv, name='export_grades_csv'),

    path('timetable/', timetable_views.timetable, name='timetable'),

    path('notifications/', notifications_views.notifications_list, name='notifications'),

    path('assignments/upload/', student_views.upload_assignment, name='upload_assignment'),
    path('assignments/', student_views.assignment_list, name='assignment_list'),

    path('teacher/dashboard/', student_views.teacher_dashboard, name='teacher_dashboard'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)