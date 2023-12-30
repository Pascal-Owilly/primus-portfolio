# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('initiate_payment/', views.initiate_payment, name='initiate_payment'),
    path('get_amount/', views.get_amount, name='get_amount'),

]
