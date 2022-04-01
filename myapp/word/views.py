from random import choice
from django.http import QueryDict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Word, APICounter
from .serializers import WordSerializer
import datetime


def home(request):
    requests_dict = {}
    previous_dates_to_show = 5
    # Get requests for previous days
    for i in range(0,previous_dates_to_show):
        date = datetime.date.today() - datetime.timedelta(i)    
        try:
            requests_made = APICounter.objects.get(date=date)
        except APICounter.DoesNotExist:
            requests_made = 0
        requests_dict[str(date)] = requests_made

    template = "word/index.html"
    context = {
        'requests_dict': requests_dict
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

class WordDetail(generics.RetrieveUpdateDestroyAPIView):
    ''' Retrieve / Update / Destroy Word '''
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    lookup_field = 'id'