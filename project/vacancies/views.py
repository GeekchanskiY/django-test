from django.views import View
from django.shortcuts import render

from .models import Vacancy

# Create your views here.

class IndexView(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()

        return render(request, 'index.html', {
            'vacancies': vacancies
        })