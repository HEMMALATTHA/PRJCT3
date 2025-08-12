from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_assignment, name='upload_assignment'),
    path('', views.assignment_list, name='assignment_list'),  # list assignments

    path('dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
]
