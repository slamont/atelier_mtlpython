# -*- encoding: utf-8 -*-

from django.contrib import admin

from ligue.models import *

class EquipeAdmin(admin.ModelAdmin):
    pass

class JoueurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'equipe',)
    list_filter = ('equipe__nom',)
    search_fields = ('nom', 'prenom',)

admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Joueur, JoueurAdmin)
