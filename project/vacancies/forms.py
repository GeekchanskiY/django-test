from django import forms

from .models import Employer, Vacancy

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('name',)

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('name', 'salary', 'employer')