from django.urls import path
from blog.views import *


urlpatterns = [
    path('',index, name='index'),
    path('projetos/', projects, name='projects'),
    path('contatos/',contact,name='contact'),
    path('projeto/<int:projeto_id>',project,name='project'),
    path('novoprojeto/',novoprojeto,name='novoprojeto')
] 