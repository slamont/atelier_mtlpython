# -*- encoding: utf-8 -*-

from django.db import models

class Equipe(models.Model):
    nom = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s" % (self.nom)

class Joueur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255, null=True)
    date_naissance = models.DateField(null=True)
    equipe  = models.ForeignKey(Equipe, null=True, related_name='joueurs')

    def __unicode__(self):
        return "%s %s" % (self.nom.upper(), self.prenom)
