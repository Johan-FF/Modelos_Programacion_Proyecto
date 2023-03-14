from django.apps import AppConfig

class ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'product'

class Software_ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'software_product'

class Kind_ProductConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kind_product'

class ResourcesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'resources'

class LicensesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'licenses'

class TechnologyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'technology'
