from django.contrib import admin

from .models import Vacancy, Employer

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    fields = ['name', 'salary', 'employer', 'author']
    list_display = ['name', 'salary', 'employer']


# Register your models here.
admin.site.register(Employer)