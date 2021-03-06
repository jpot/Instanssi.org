# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Event', fields ['name']
        db.create_unique('kompomaatti_event', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'Event', fields ['name']
        db.delete_unique('kompomaatti_event', ['name'])


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'kompomaatti.competition': {
            'Meta': {'object_name': 'Competition'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'end': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kompomaatti.Event']"}),
            'hide_from_archive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'participation_end': ('django.db.models.fields.DateTimeField', [], {}),
            'score_sort': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'score_type': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'show_results': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'start': ('django.db.models.fields.DateTimeField', [], {})
        },
        'kompomaatti.competitionparticipation': {
            'Meta': {'object_name': 'CompetitionParticipation'},
            'competition': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kompomaatti.Competition']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant_name': ('django.db.models.fields.CharField', [], {'default': "u''", 'max_length': '32'}),
            'score': ('django.db.models.fields.FloatField', [], {'default': '0', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'kompomaatti.compo': {
            'Meta': {'object_name': 'Compo'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'adding_end': ('django.db.models.fields.DateTimeField', [], {}),
            'compo_start': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'editing_end': ('django.db.models.fields.DateTimeField', [], {}),
            'entry_sizelimit': ('django.db.models.fields.IntegerField', [], {'default': '134217728'}),
            'entry_view_type': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kompomaatti.Event']"}),
            'formats': ('django.db.models.fields.CharField', [], {'default': "'zip|7z|gz|bz2'", 'max_length': '128'}),
            'hide_from_archive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'show_voting_results': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'source_formats': ('django.db.models.fields.CharField', [], {'default': "'zip|7z|gz|bz2'", 'max_length': '128'}),
            'source_sizelimit': ('django.db.models.fields.IntegerField', [], {'default': '134217728'}),
            'voting_end': ('django.db.models.fields.DateTimeField', [], {}),
            'voting_start': ('django.db.models.fields.DateTimeField', [], {})
        },
        'kompomaatti.entry': {
            'Meta': {'object_name': 'Entry'},
            'archive_rank': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'archive_score': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'compo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kompomaatti.Compo']"}),
            'creator': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'disqualified': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'disqualified_reason': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'entryfile': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagefile_original': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'sourcefile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'youtube_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        'kompomaatti.event': {
            'Meta': {'object_name': 'Event'},
            'archived': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'kompomaatti.profile': {
            'Meta': {'object_name': 'Profile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'otherinfo': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'kompomaatti.vote': {
            'Meta': {'object_name': 'Vote'},
            'compo': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kompomaatti.Compo']"}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kompomaatti.Entry']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rank': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'kompomaatti.votecode': {
            'Meta': {'unique_together': "(('event', 'key'), ('event', 'associated_to'))", 'object_name': 'VoteCode'},
            'associated_to': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kompomaatti.Event']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '64'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'kompomaatti.votecoderequest': {
            'Meta': {'object_name': 'VoteCodeRequest'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['kompomaatti.Event']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['kompomaatti']