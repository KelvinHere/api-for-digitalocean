from random import choice
from django.http import HttpResponse, QueryDict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Word, APICounter
from .serializers import WordSerializer
from .utils import restore_dictionary_function, api_usage_logs
import datetime


def home(request):
    # How many days usage logs to show
    days_to_show = 5
    api_usage = api_usage_logs(days_to_show)

    template = "word/index.html"
    context = {
        'api_usage': api_usage,
        'dictionary_restored': False,
    }
    return render(request, template, context)


class RandomWord(APIView):

    ''' Get Random Word '''
    def get(self, request):
        #  Get random word
        pks = Word.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        random_word = Word.objects.get(pk=random_pk)
        serializer = WordSerializer(random_word)

        # Record API request date
        today = datetime.date.today()
        try:
            api_counter = APICounter.objects.get(date=today)
        except APICounter.DoesNotExist:
            api_counter = APICounter.objects.create()
            api_counter.save()

        # Update API usage
        api_counter.requests += 1
        api_counter.save()

        return Response(serializer.data)


class WordDetail(generics.RetrieveUpdateAPIView):
    ''' Retrieve / Update / Destroy Word '''
    authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.edited = True
        instance.save()
        return self.update(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance.edited)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


def restore_dictionary(request):
    restore_dictionary_function()
    # How many days usage logs to show
    days_to_show = 5
    api_usage = api_usage_logs(days_to_show)

    template = "word/index.html"
    context = {
        'api_usage': api_usage,
        'dictionary_restored': True,
    }
    return render(request, template, context)
