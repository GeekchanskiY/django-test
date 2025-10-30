from django.contrib import admin

from .models import Vacancy, Employer
from applications.models import Application


class ApplicationInline(admin.StackedInline):
    model = Application
    extra = 1


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    fields = ('name', 'salary', 'employer', 'author',)
    list_display = ('name', 'salary', 'employer',)
    inlines = (ApplicationInline,)


admin.site.register(Employer)