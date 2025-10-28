from django.contrib import admin

from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    # fields = ('user', 'email', 'vacancy', 'want_salary', 'created_at',)
    fieldsets = (
        ('primary user info', {'fields': ('user', 'email')}),
        ('other info', {'fields': ('vacancy', 'want_salary', 'created_at')}),
    )

    readonly_fields = ('created_at',)

    list_display = ('user', 'vacancy', 'created_at', 'salary_diff')

    def salary_diff(self, obj):
        return obj.vacancy.salary - obj.want_salary

    class Meta:
        verbose_name = 'application'
        verbose_name_plural = 'applications'