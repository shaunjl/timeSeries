# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'tSRType'
        db.create_table(u'timeSeriesApp_tsrtype', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            (u'comments_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'tsrtypes', to=orm['auth.User'])),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'creator_of_timeseriesapp_tsrtype', to=orm['auth.User'])),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('frozen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('do_not_distribute', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('discoverable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('published_and_frozen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_changed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'last_changed_timeseriesapp_tsrtype', null=True, to=orm['auth.User'])),
            ('resource_description', self.gf('django.db.models.fields.TextField')(default='', blank=True)),
        ))
        db.send_create_signal(u'timeSeriesApp', ['tSRType'])

        # Adding M2M table for field owners on 'tSRType'
        m2m_table_name = db.shorten_name(u'timeSeriesApp_tsrtype_owners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tsrtype', models.ForeignKey(orm[u'timeSeriesApp.tsrtype'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tsrtype_id', 'user_id'])

        # Adding model 'tS'
        db.create_table(u'timeSeriesApp_ts', (
            (u'page_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['pages.Page'], unique=True, primary_key=True)),
            (u'comments_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('content', self.gf('mezzanine.core.fields.RichTextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'tss', to=orm['auth.User'])),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'creator_of_timeseriesapp_ts', to=orm['auth.User'])),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('frozen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('do_not_distribute', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('discoverable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('published_and_frozen', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('last_changed_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'last_changed_timeseriesapp_ts', null=True, to=orm['auth.User'])),
            ('tsrtype', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['timeSeriesApp.tSRType'])),
            ('tS_title', self.gf('django.db.models.fields.TextField')(max_length=60)),
            ('resource_content', self.gf('django.db.models.fields.TextField')(max_length=200)),
        ))
        db.send_create_signal(u'timeSeriesApp', ['tS'])

        # Adding M2M table for field owners on 'tS'
        m2m_table_name = db.shorten_name(u'timeSeriesApp_ts_owners')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ts', models.ForeignKey(orm[u'timeSeriesApp.ts'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['ts_id', 'user_id'])


    def backwards(self, orm):
        # Deleting model 'tSRType'
        db.delete_table(u'timeSeriesApp_tsrtype')

        # Removing M2M table for field owners on 'tSRType'
        db.delete_table(db.shorten_name(u'timeSeriesApp_tsrtype_owners'))

        # Deleting model 'tS'
        db.delete_table(u'timeSeriesApp_ts')

        # Removing M2M table for field owners on 'tS'
        db.delete_table(db.shorten_name(u'timeSeriesApp_ts_owners'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'pages.page': {
            'Meta': {'ordering': "(u'titles',)", 'object_name': 'Page'},
            '_meta_title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            '_order': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'content_model': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'expiry_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'gen_description': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_menus': ('mezzanine.pages.fields.MenusField', [], {'default': '(1, 2, 3)', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'in_sitemap': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'keywords_string': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'login_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'children'", 'null': 'True', 'to': u"orm['pages.Page']"}),
            'publish_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'short_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titles': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'timeSeriesApp.ts': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'tS', '_ormbases': [u'pages.Page']},
            u'comments_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'creator_of_timeseriesapp_ts'", 'to': u"orm['auth.User']"}),
            'discoverable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'do_not_distribute': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'frozen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_changed_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'last_changed_timeseriesapp_ts'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'owns_timeseriesapp_ts'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'published_and_frozen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resource_content': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'tS_title': ('django.db.models.fields.TextField', [], {'max_length': '60'}),
            'tsrtype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['timeSeriesApp.tSRType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'tss'", 'to': u"orm['auth.User']"})
        },
        u'timeSeriesApp.tsrtype': {
            'Meta': {'ordering': "(u'_order',)", 'object_name': 'tSRType', '_ormbases': [u'pages.Page']},
            u'comments_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'content': ('mezzanine.core.fields.RichTextField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'creator_of_timeseriesapp_tsrtype'", 'to': u"orm['auth.User']"}),
            'discoverable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'do_not_distribute': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'frozen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_changed_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'last_changed_timeseriesapp_tsrtype'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'owners': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "u'owns_timeseriesapp_tsrtype'", 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            u'page_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['pages.Page']", 'unique': 'True', 'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'published_and_frozen': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resource_description': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'tsrtypes'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['timeSeriesApp']