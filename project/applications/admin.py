from django.contrib import admin

from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    class Meta:
        verbose_name = 'заявка'
        verbose_name_plural = 'заявки'