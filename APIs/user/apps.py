from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

class User_RolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_rol'

class CountryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'country'

class HistoryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'history'