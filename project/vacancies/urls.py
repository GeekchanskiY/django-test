from django.urls import path
from .views import Index, AddEmployer, AddVacancy

urlpatters = [
    path('', Index.as_view(), name='vacancies'),
    path('employers/add', AddEmployer.as_view(), name='add_employer'),
    path('vacancy/add', AddVacancy.as_view(), name='add_vacancy')
]