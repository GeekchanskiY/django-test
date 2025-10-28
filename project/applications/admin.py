from django.contrib import admin

from .models import Application

from .admin_filters import IsDimaListFilter


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    # fields = ('user', 'email', 'vacancy', 'want_salary', 'created_at',)
    fieldsets = (
        ('primary user info', {'fields': ('user', 'email')}),
        ('other info', {'fields': ('vacancy', 'want_salary', 'created_at')}),
    )

    readonly_fields = ('created_at',)

    list_display = ('id', 'user', 'vacancy', 'vacancy__id', 'created_at', 'salary_diff')
    list_editable = ('user',)
    list_display_links = ('id', 'salary_diff',)
    ordering = ('-vacancy__id', '-id', )

    search_fields = ('email', 'user', 'vacancy__id')
    list_filter = ('user', 'created_at', IsDimaListFilter)

    def salary_diff(self, obj):
        return obj.vacancy.salary - obj.want_salary

    class Meta:
        verbose_name = 'application'
        verbose_name_plural = 'applications'