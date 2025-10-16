from django.views import View
from django.shortcuts import render, redirect

from .forms import EmployerForm, VacancyForm
from .models import Vacancy

# Create your views here.

class Index(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()

        if not request.user.is_authenticated:
            return redirect(to='/')

        return render(request, 'index.html', {
            'vacancies': vacancies
        })
    
    def post(self, request):
        return render(request, 'index.html', None)
    

class AddEmployer(View):
    def get(self, request):
        form = EmployerForm()
        
        return render(request, 'add_employer.html', {'form': form})
    
    def post(self, request):
        form = EmployerForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(to='/')
        
        return render(request, 'add_employer.html', {'form': form})
    

class AddVacancy(View):
    def get(self, request):
        form = VacancyForm()
        
        return render(request, 'add_vacancy.html', {'form': form})
    
    def post(self, request):
        form = VacancyForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect(to='/')
        
        return render(request, 'add_vacancy.html', {'form': form})