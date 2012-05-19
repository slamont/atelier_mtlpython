# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Joueur.birthDate'
        db.add_column('ligue_joueur', 'birthDate',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Joueur.birthDate'
        db.delete_column('ligue_joueur', 'birthDate')


    models = {
        'ligue.equipe': {
            'Meta': {'object_name': 'Equipe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teamName': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'ligue.joueur': {
            'Meta': {'object_name': 'Joueur'},
            'birthDate': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['ligue']