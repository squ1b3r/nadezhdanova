# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ActivitySlide.order'
        db.add_column(u'activities_activityslide', 'order',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=0),
                      keep_default=False)


        # Changing field 'ActivitySlide.image'
        db.alter_column(u'activities_activityslide', 'image', self.gf('sorl.thumbnail.fields.ImageField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'ActivitySlide.order'
        db.delete_column(u'activities_activityslide', 'order')


        # Changing field 'ActivitySlide.image'
        db.alter_column(u'activities_activityslide', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'activities.activity': {
            'Meta': {'object_name': 'Activity'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'text_ru': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'title_ru': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'})
        },
        u'activities.activityslide': {
            'Meta': {'ordering': "('order',)", 'object_name': 'ActivitySlide'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'slides'", 'to': u"orm['activities.Activity']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['activities']