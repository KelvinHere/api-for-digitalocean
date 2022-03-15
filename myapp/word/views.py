from random import choice
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Word, APICounter
from .serializers import WordSerializer
import datetime


def home(request):
    today = datetime.date.today()
    requests_today = APICounter.objects.get(date=today)
    return HttpResponse(f"<b>Random Word Home Page<b> <br><br> Ask for a random word with /word <br><br>Total API requests today: {requests_today}")


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
            api_counter = APICounter.objects.create
            api_counter.save()

        api_counter.requests += 1
        api_counter.save()
        a = APICounter.objects.get(date=today)
        print(a.requests)

        return Response(serializer.data)