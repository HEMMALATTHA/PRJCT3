from django.urls import path
from . import views

urlpatterns = [
    path('', views.gradebook, name='gradebook'),
    path('export_csv/', views.export_grades_csv, name='export_grades_csv'),
]
