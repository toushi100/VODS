from django.apps import AppConfig
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UsersappConfig(AppConfig):
    name = 'Userapp'

    def ready(self):
        import Usersapp.signals