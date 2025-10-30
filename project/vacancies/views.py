from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from .forms import EmployerForm, VacancyForm
from .models import Vacancy
from .signals import custom_signal


class Index(View):
    def get(self, request):
        custom_signal.send(sender=None, text='privet')
        vacancies = Vacancy.objects.all()

        paginator = Paginator(vacancies, 2) 
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        return render(request, 'index.html', {
            'vacancies': page_obj,
            'page_minus': page_obj.number - 1,
            'page_minus_2': page_obj.number - 2,
            'page_plus': page_obj.number + 1,
            'page_plus_2': page_obj.number + 2,
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
    

class DeleteVacancy(View):
    def get(self, request, vacancy_id):
        get_object_or_404(Vacancy, pk=vacancy_id).delete()

        return redirect('vacancies')
    

class UpdateVacancy(View):
    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
        if vacancy.author != request.user:
            return redirect('vacancies')

        form = VacancyForm(instance=vacancy)

        return render(request, 'update_vacancy.html', {'form': form, 'vacancy_id': vacancy_id})

    def post(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)
        if vacancy.author != request.user:
            return redirect('vacancies')

        form = VacancyForm(request.POST, instance=vacancy)
        if form.is_valid():
            form.save()

            return redirect('show_vacancy', vacancy_id)
        
        return render(request, 'update_vacancy.html', {'form': form, 'vacancy_id': vacancy_id})