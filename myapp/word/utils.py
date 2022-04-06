from .models import Word, APICounter
from django.conf import settings
import json
import datetime


def restore_dictionary_function():
    ''' Resets all changes to the dictionary'''
    with open(f'{settings.BASE_DIR}/word/fixtures/dictionary.json') as file:
        original_words = json.load(file)
    
    for original_word in original_words:
        word = Word.objects.get(pk=original_word['pk'])
        word.word = original_word['fields']['word']
        word.meaning = original_word['fields']['meaning']
        word.edited = False
        word.save()
        

def api_usage_logs(days):
    ''' Gets N days of API usage & returns as dict '''
    requests_dict = {}
    for i in range(0,days):
        date = datetime.date.today() - datetime.timedelta(i)    
        try:
            requests_made = APICounter.objects.get(date=date)
        except APICounter.DoesNotExist:
            requests_made = 0
        requests_dict[str(date)] = requests_made
    
    return requests_dict
    