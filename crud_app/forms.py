from django import forms
from . models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model =  Student
        fields = ['name',"email","password"]
        widgets = {"password":forms.PasswordInput()}
