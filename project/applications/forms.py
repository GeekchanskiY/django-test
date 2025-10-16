from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('want_salary', 'user', 'email', 'vacancy')
        widgets = {'vacancy': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        self.vacancy = kwargs.pop('vacancy', None)
        super().__init__(*args, **kwargs)

        if self.vacancy:
            self.fields['vacancy'].initial = self.vacancy