from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout


from django.shortcuts import render, redirect

# Create your views here.
class Register(View):
    def get(self, request):
        form = UserCreationForm()

        return render(request, 'register.html', {'form': form})
    
     
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            
            return redirect(to='/')
        
        return render(request, 'register.html', {'form': form})
    

class Logout(View):
    def get(self, request):
        logout(request)

        return redirect(to='/')