from django.contrib import admin
from django.http import HttpResponse

from .models import Application
from .admin_filters import IsDimaListFilter


def print_data(modeladmin, request, queryset):
    text_content = ""

    for i in queryset.all():
        text_content += str(i) + "\n"

    response = HttpResponse(
        text_content,
        content_type="text/plain"  # Specify the content type as plain text
    )

    response['Content-Disposition'] = 'attachment; filename="my_dynamic_file.txt"'

    return response

print_data.short_description = 'print data in console'


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('primary user info', {'fields': ('user',)}),
        ('other info', {'fields': ('vacancy', 'want_salary', 'created_at')}),
    )
    readonly_fields = ('created_at',)
    search_fields = ('email', 'user__username', 'vacancy__id')

    actions = (print_data,)

    list_filter = ('user', 'created_at', IsDimaListFilter)
    list_display = ('id', 'user', 'vacancy', 'vacancy__id', 'created_at', 'salary_diff', 'is_dima')
    list_display_links = ('id', 'salary_diff',)

    ordering = ('-vacancy__id', '-id', )

    def salary_diff(self, obj):
        return obj.vacancy.salary - obj.want_salary
    
    def is_dima(self, obj):
        if obj.user:
            username_lower = obj.user.username.lower()
            return username_lower == "dima" or username_lower == "dimka" or username_lower == "dmitry"
        else:
            return False
    
    is_dima.boolean = True
    is_dima.short_description = '?Dima'


    class Meta:
        verbose_name = 'application'
        verbose_name_plural = 'applications'