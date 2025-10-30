from django.urls import path

from .views import AddApplication, MyApplications


urlpatters = [
    path('apply/<int:vacancy_id>', AddApplication.as_view(), name='apply'),
    path('my_candidates', MyApplications.as_view(), name='my_candidates')
]