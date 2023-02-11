from django.contrib import admin
from blog.models import Projetos

# Register your models here.
class ProjetosAdmin(admin.ModelAdmin):
    list_display = ('id','nome','legenda')
    list_display_links = ('nome',)
    list_per_page = 10
    ordering = ('id',)
admin.site.register(Projetos,ProjetosAdmin)