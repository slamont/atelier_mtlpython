# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Joueurs'
        db.delete_table('ligue_joueurs')

        # Adding model 'Joueur'
        db.create_table('ligue_joueur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('ligue', ['Joueur'])


    def backwards(self, orm):
        # Adding model 'Joueurs'
        db.create_table('ligue_joueurs', (
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('ligue', ['Joueurs'])

        # Deleting model 'Joueur'
        db.delete_table('ligue_joueur')


    models = {
        'ligue.equipe': {
            'Meta': {'object_name': 'Equipe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teamName': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'ligue.joueur': {
            'Meta': {'object_name': 'Joueur'},
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['ligue']