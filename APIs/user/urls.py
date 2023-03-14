from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserView.as_view(), name='users_list'),
    path('users/<int:id_u>', UserView.as_view(), name='users_process'),
    path('user_rols/', User_RolView.as_view(), name='user_rols_list'),
    path('user_rols/<int:id_u_r>', User_RolView.as_view(), name='user_rols_process'),
    path('countrys/', CountryView.as_view(), name='countrys_list'),
    path('countrys/<int:id_c>', CountryView.as_view(), name='countrys_process'),
    path('historys/', HistoryView.as_view(), name='historys_list'),
    path('historys/<int:id_h>', HistoryView.as_view(), name='historys_process'),
]