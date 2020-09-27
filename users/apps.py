from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self): #create user profile sending signal
        import users.signals
