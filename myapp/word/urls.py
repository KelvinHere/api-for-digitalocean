from django.urls import path
from .views import RandomWord, home, WordDetail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', home, name='home'),
    path('word/', RandomWord.as_view(), name='word'),
    path('word/<int:id>/', WordDetail.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]