from django.db import models

# Create your models here.

class Equipe(models.Model):
    teamName = models.CharField(max_length=255)
    
    def __unicode__(self):
        return "%s [%d]" % (self.teamName, self.id )

class Joueur(models.Model):
    helpText = "Ceci est un text d'aide dans une variable"
    lastName = models.CharField(max_length=255, verbose_name="Nom", help_text=helpText)
    firstName = models.CharField(max_length=255, verbose_name="Prenom")
    birthDate = models.DateField(null=True, blank=True, verbose_name="Date de Naissance")
    equipe = models.ForeignKey('Equipe', null=True, blank=True)

    def __unicode__(self):
        return "%s %s" % (self.lastName, self.firstName )


