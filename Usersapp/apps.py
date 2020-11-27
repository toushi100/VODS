from django.apps import AppConfig


class UsersappConfig(AppConfig):
    name = 'Usersapp'

    def ready(self):
        import users.signals