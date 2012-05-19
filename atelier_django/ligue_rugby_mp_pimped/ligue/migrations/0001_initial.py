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
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('ligue', ['Equipe'])

        # Adding model 'Joueur'
        db.create_table('ligue_joueur', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('prenom', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('equipe', self.gf('django.db.models.fields.related.ForeignKey')(related_name='joueurs', null=True, to=orm['ligue.Equipe'])),
        ))
        db.send_create_signal('ligue', ['Joueur'])

    def backwards(self, orm):
        # Deleting model 'Equipe'
        db.delete_table('ligue_equipe')

        # Deleting model 'Joueur'
        db.delete_table('ligue_joueur')

    models = {
        'ligue.equipe': {
            'Meta': {'object_name': 'Equipe'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'ligue.joueur': {
            'Meta': {'object_name': 'Joueur'},
            'equipe': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'joueurs'", 'null': 'True', 'to': "orm['ligue.Equipe']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'prenom': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['ligue']