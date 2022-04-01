from django.urls import path
from .views import RandomWord, home, WordDetail

urlpatterns = [
    path('', home, name='home'),
    path('word/', RandomWord.as_view(), name='word'),
    path('word/<int:id>/', WordDetail.as_view())
]