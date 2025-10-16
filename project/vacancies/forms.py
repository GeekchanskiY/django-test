from django import forms

from .models import Employer, Vacancy

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('name',)

class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ('name', 'salary', 'employer', 'author')

        widgets = {'author': forms.HiddenInput()}
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('author', None)
        super().__init__(*args, **kwargs)

        if self.user:
            self.fields['author'].initial = self.user