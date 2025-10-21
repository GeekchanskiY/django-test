from django.contrib import admin

from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    class Meta:
        verbose_name = 'application'
        verbose_name_plural = 'applications'