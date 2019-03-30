from django.contrib import admin
from .models import Pessoa, Compromisso, Agenda, AgendaInstitucional

@admin.register(Pessoa,Agenda,Compromisso,AgendaInstitucional)
class NoticiaAdmin(admin.ModelAdmin):
    pass

# Register your models here.
