from django.urls import path
from .views import RandomWord, home

urlpatterns = [
    path('', home, name='home'),
    path('word/', RandomWord.as_view(), name='word'),
]