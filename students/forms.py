from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, StudentProfile
from .models import Assignment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    profile_picture = forms.ImageField(required=False)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_student', 'is_teacher']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            if user.is_student:
                StudentProfile.objects.create(user=user)
        return user
    
class AssignmentUploadForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['title', 'document']
