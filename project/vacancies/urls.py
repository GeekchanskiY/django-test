from django.urls import path
from .views import IndexView

urlpatters = [
    path('', IndexView.as_view()),
]