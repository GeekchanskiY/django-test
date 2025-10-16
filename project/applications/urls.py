from django.urls import path

from .views import AddApplication

urlpatters = [
    path('apply/<int:vacancy_id>', AddApplication.as_view(), name='apply')
]