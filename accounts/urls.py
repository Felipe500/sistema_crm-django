
from django.urls import path, include

from .views import prod, cust, inicio

urlpatterns = [
    path('', inicio, name = 'home'),
    path('produtos/', prod, name = 'produtos'),
    path('custom/', cust , name='customize')

]