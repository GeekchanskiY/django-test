from datetime import date

from django.contrib import admin
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class IsDimaListFilter(admin.SimpleListFilter):
    title = "is_dima"

    parameter_name = "is_dima"

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each
        tuple is the coded value for the option that will
        appear in the URL query. The second element is the
        human-readable name for the option that will appear
        in the right sidebar.
        """
        return [
            ("yes", "Yes, Dima!"),
            ("no", "No, Dima!"),
        ]

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value
        provided in the query string and retrievable via
        `self.value()`.
        """
        if self.value() == "yes":
            return queryset.filter(
                Q(user__icontains='Dima') | Q(user__icontains='Dmitry') | Q(user__icontains='Dimka'),
            )
        if self.value() == "no":
            return queryset.exclude(
                Q(user__icontains='Dima') | Q(user__icontains='Dmitry') | Q(user__icontains='Dimka')
            )