from django.views import View
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from .forms import EmployerForm, VacancyForm
from .models import Vacancy
from .signals import custom_signal


class Index(View):
    def get(self, request):
        custom_signal.send(sender=None, text='privet')
        vacancies = Vacancy.objects.all()

        return render(request, 'index.html', {
            'vacancies': vacancies
        })
    
    def post(self, request):
        return render(request, 'index.html', None)
    

class ShowVacancy(View):
    def get(self, request, vacancy_id):
        try:
            vacancy = Vacancy.objects.get(id=vacancy_id)
        except ObjectDoesNotExist:
            return redirect('vacancies')


        return render(request, 'show_vacancy.html', {'vacancy': vacancy})
    

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
        if not request.user.is_authenticated:
            return redirect(to='register')

        form = VacancyForm(author=request.user)
        
        return render(request, 'add_vacancy.html', {'form': form})
    
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect(to='register')
        
        form = VacancyForm(request.POST, author=request.user)

        if form.is_valid():
            
            form.save()
            
            return redirect(to='/')
        
        return render(request, 'add_vacancy.html', {'form': form})