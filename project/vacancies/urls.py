from django.urls import path
from .views import Index, AddEmployer

urlpatters = [
    path('', Index.as_view(), name='vacancies'),
    path('employers/add', AddEmployer.as_view(), name='add_employer')
]