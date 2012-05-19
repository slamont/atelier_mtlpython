# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Equipe'
        db.create_table('ligue_equipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('teamName', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('ligue', ['Equipe'])

        # Adding model 'Joueurs'
        db.create_table('ligue_joueurs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lastName', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('firstName', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('ligue', ['Joueurs'])


    def backwards(self, orm):
        # Deleting model 'Equipe'
        db.delete_table('ligue_equipe')

        # Deleting model 'Joueurs'
        db.delete_table('ligue_joueurs')


    models = {
        'ligue.equipe': {
            'Meta': {'object_name': 'Equipe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'teamName': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'ligue.joueurs': {
            'Meta': {'object_name': 'Joueurs'},
            'firstName': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastName': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['ligue']