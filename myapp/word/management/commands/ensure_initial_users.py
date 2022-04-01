from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
import os

class Command(BaseCommand):
    help = "Creates an admin user if it doesn't already exist"

    def handle(self, *args, **options):
        User = get_user_model()
        ''' Setup Superuser if doesn't exist '''
        if not User.objects.filter(username='ADMIN').exists():
            superuser = User.objects.create_superuser(username=os.environ.get('SU_NAME'),
                                          email=os.environ.get('SU_EMAIL'),
                                          password=os.environ.get('SU_PASS'))
            print(f'{superuser.username} : CREATED')
        else:
            print(f'ADMIN : Already Exists')

        ''' Setup Standard User if doesn't exist '''
        if not User.objects.filter(username='USER1').exists():
            new_user = User.objects.create_user(username=os.environ.get('USER_NAME'),
                                          email=os.environ.get('USER_EMAIL'),
                                          password=os.environ.get('USER_PASS'))
            print(f'{new_user.username} : CREATED')
        else:
            print(f'{new_user.username} : Already Exists')


