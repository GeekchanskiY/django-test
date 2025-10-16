from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from .forms import ApplicationForm
from .models import Application
from vacancies.models import Vacancy


class AddApplication(View):
    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)

        form = ApplicationForm(vacancy=vacancy)
        
        return render(request, 'apply.html', {'form': form, 'vacancy': vacancy})
    
    def post(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, pk=vacancy_id)

        form = ApplicationForm(request.POST, vacancy=vacancy)

        if form.is_valid():
            form.save()

            return redirect('/')
        
        return render(request, 'add_vacancy.html', {'form': form, 'vacancy': vacancy})
    

class MyApplications(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        
        application = Application.objects.filter(vacancy__author=request.user)

        return render(request, 'my_candidates.html', {'applications': application})