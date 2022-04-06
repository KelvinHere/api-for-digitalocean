from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.home, name='home'),
    path('word/', views.RandomWord.as_view(), name='word'),
    path('word/<int:id>/', views.WordDetail.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('restore-dictionary/', views.restore_dictionary, name='restore_dictionary'),
]