from django.contrib import admin
from .models import *

# Tables Product

admin.site.register(Kind_Product)
admin.site.register(License)
admin.site.register(Technology)
admin.site.register(Resources)
admin.site.register(Software_Product)

# Tables Sale

admin.site.register(Sale)
admin.site.register(Stock)
admin.site.register(Store)
admin.site.register(Bank)

# Tables User

admin.site.register(User)
admin.site.register(User_Rol)
admin.site.register(Country)
admin.site.register(History)
