from django.urls import path,include
from usuarios.views import *

urlpatterns = [
    path('login', login, name='login'),
    path('logout',logout,name='logout'),
]