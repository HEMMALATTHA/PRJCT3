from django import forms
from .models import Enrollment, Course
from students.models import StudentProfile

class EnrollmentForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all())
