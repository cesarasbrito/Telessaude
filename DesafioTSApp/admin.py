from django.contrib import admin
from .models import Solicitacao,Solicitante,Teleconsultor


# Register your models here.
admin.site.register(Solicitacao)
admin.site.register(Solicitante)
admin.site.register(Teleconsultor)