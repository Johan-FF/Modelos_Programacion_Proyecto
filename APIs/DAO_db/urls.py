from django.urls import path
from .views import *

urlpatterns = [
    # URLS Product

    path('software_products/', Software_ProductView.as_view(), name='software_products_list'),
    path('software_products/<int:id_s_p>', Software_ProductView.as_view(), name='software_products_process'),
    path('technologies/', TechnologyView.as_view(), name='technologies_list'),
    path('technologies/<int:id_t>', TechnologyView.as_view(), name='technologies_process'),
    path('licenses/', LicenseView.as_view(), name='licenses_list'),
    path('licenses/<int:id_l>', LicenseView.as_view(), name='licenses_process'),
    path('resources/', ResourcesView.as_view(), name='resources_list'),
    path('resources/<int:id_r>', ResourcesView.as_view(), name='resources_process'),
    path('kind_products/', Kind_ProductView.as_view(), name='kind_products_list'),
    path('kind_products/<int:id_k_p>', Kind_ProductView.as_view(), name='kind_products_process'),

    # URLS Sale

    path('stores/', StoreView.as_view(), name='stores_list'),
    path('stores/<int:id_s>', StoreView.as_view(), name='stores_process'),    
    path('stock/', StockView.as_view(), name='stock_list'),
    path('stock/<int:id_s>', StockView.as_view(), name='stock_process'),
    path('banks/', BankView.as_view(), name='banks_list'),
    path('banks/<int:id_b>', BankView.as_view(), name='banks_process'),
    path('sales/', SaleView.as_view(), name='sales_list'),
    path('sales/<int:id_s>', SaleView.as_view(), name='sales_process'),

    # URLS User

    path('users/', UserView.as_view(), name='users_list'),
    path('users/<int:id_u>', UserView.as_view(), name='users_process'),
    path('user_rols/', User_RolView.as_view(), name='user_rols_list'),
    path('user_rols/<int:id_u_r>', User_RolView.as_view(), name='user_rols_process'),
    path('countrys/', CountryView.as_view(), name='countrys_list'),
    path('countrys/<int:id_c>', CountryView.as_view(), name='countrys_process'),
    path('historys/', HistoryView.as_view(), name='historys_list'),
    path('historys/<int:id_h>', HistoryView.as_view(), name='historys_process'),
]