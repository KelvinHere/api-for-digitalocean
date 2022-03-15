from random import choice
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Word, APICounter
from .serializers import WordSerializer


def home(request):
    try:
            api_counter = APICounter.objects.get(pk=1)
    except APICounter.DoesNotExist:
            api_counter = APICounter(total_requests=0)
            api_counter.save()
    
    total_requests = api_counter.total_requests

    return HttpResponse(f"<b>Random Word Home Page<b> <br><br> Ask for a random word with /word <br><br>Total API requests: {total_requests}")


class RandomWord(APIView):

    ''' Get Random Word '''
    def get(self, request):
        #  Get random word
        pks = Word.objects.values_list('pk', flat=True)
        random_pk = choice(pks)
        random_word = Word.objects.get(pk=random_pk)
        serializer = WordSerializer(random_word)

        # Update Hit Counter
        try:
            api_counter = APICounter.objects.get(pk=1)
        except APICounter.DoesNotExist:
            api_counter = APICounter(total_requests=0)
            api_counter.save()

        api_counter.total_requests += 1
        api_counter.save()

        return Response(serializer.data)