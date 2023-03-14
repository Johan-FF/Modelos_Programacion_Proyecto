from django.urls import path
from .views import *

urlpatterns = [
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
]