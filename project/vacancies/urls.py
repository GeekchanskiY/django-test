from django.urls import path
from .views import Index, AddEmployer, AddVacancy, ShowVacancy

urlpatters = [
    path('', Index.as_view(), name='vacancies'),
    path('vacancy/<int:vacancy_id>', ShowVacancy.as_view(), name='show_vacancy'),
    path('employers/add', AddEmployer.as_view(), name='add_employer'),
    path('vacancy/add', AddVacancy.as_view(), name='add_vacancy')
]