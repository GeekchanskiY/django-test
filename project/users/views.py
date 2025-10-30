from datetime import datetime, timezone

from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404

from .models import Profile
from .forms import UploadAvatarForm


class ShowProfile(View):
    def get(self, request, user_id):
        if user_id == 0:
            user_id = request.user.id

        profile = get_object_or_404(Profile, user=user_id)
        date_joined = profile.user.date_joined.strftime('%Y-%m-%d')

        now = datetime.now(timezone.utc)
        time_since = now - profile.user.last_login
        seconds = time_since.seconds
        hours = seconds // 3600
        
        last_login = 'long time ago'

        if hours < 48:
            last_login = 'yesterday'

        if hours < 24:
            last_login = 'today'

        if hours < 1:
            last_login = 'just now'

        form = UploadAvatarForm()

        return render(request, 'profile.html', {
            'profile': profile,
            'date_joined': date_joined,
            'last_login': last_login,
            'form': form
        })
    
    def post(self, request, user_id):
        if user_id == 0:
            user_id = request.user.id

        profile = get_object_or_404(Profile, user=user_id)
        date_joined = profile.user.date_joined.strftime('%Y-%m-%d')

        now = datetime.now(timezone.utc)
        time_since = now - profile.user.last_login
        seconds = time_since.seconds
        hours = seconds // 3600
        
        last_login = 'long time ago'

        if hours < 48:
            last_login = 'yesterday'

        if hours < 24:
            last_login = 'today'

        if hours < 1:
            last_login = 'just now'

        form = UploadAvatarForm(request.POST, request.FILES)
        print(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.cleaned_data["image"]
            print(avatar)
            print(type(avatar))

            profile.avatar = avatar

            profile.save()
        else:
            print(form.errors)

        return render(request, 'profile.html', {
            'profile': profile,
            'date_joined': date_joined,
            'last_login': last_login,
            'form': form
        })

class Register(View):
    def get(self, request):
        form = UserCreationForm()

        return render(request, 'register.html', {'form': form})
    
     
    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            Profile(user=user, avatar=None).save()
            
            return redirect(to='/')
        
        return render(request, 'register.html', {'form': form})
    

class Logout(View):
    def get(self, request):
        logout(request)

        return redirect(to='/')