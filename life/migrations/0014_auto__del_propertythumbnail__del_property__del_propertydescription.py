# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'PropertyThumbnail'
        db.delete_table('life_propertythumbnail')

        # Deleting model 'Property'
        db.delete_table('life_property')

        # Deleting model 'PropertyDescription'
        db.delete_table('life_propertydescription')


    def backwards(self, orm):
        
        # Adding model 'PropertyThumbnail'
        db.create_table('life_propertythumbnail', (
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Property'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('life', ['PropertyThumbnail'])

        # Adding model 'Property'
        db.create_table('life_property', (
            ('style', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('bed_count', self.gf('django.db.models.fields.IntegerField')()),
            ('sale_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.District'])),
            ('reception_count', self.gf('django.db.models.fields.IntegerField')()),
            ('status_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('parking', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('tenure_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('bath_count', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('branch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Branch'])),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Address'])),
            ('setting', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('property_id', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
        ))
        db.send_create_signal('life', ['Property'])

        # Adding model 'PropertyDescription'
        db.create_table('life_propertydescription', (
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Property'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Language'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('life', ['PropertyDescription'])


    models = {
        'life.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postcode': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'life.branch': {
            'Meta': {'object_name': 'Branch'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Address']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'life.citypart': {
            'Meta': {'object_name': 'CityPart'},
            'cp_id': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'life.district': {
            'Meta': {'object_name': 'District'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.CityPart']"})
        },
        'life.faq': {
            'Meta': {'object_name': 'Faq'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'life.faqtranslation': {
            'Meta': {'object_name': 'FaqTranslation'},
            'answer': ('django.db.models.fields.TextField', [], {}),
            'faq': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Faq']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Language']"}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'life.language': {
            'Meta': {'object_name': 'Language'},
            'flag': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'lang_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'})
        },
        'life.staffmember': {
            'Meta': {'object_name': 'StaffMember'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['life.Language']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'life.testimonial': {
            'Meta': {'object_name': 'Testimonial'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'quote_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        'life.testimonialtranslation': {
            'Meta': {'object_name': 'TestimonialTranslation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Language']"}),
            'quote': ('django.db.models.fields.TextField', [], {}),
            'testimonial': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Testimonial']"})
        },
        'life.textelement': {
            'Meta': {'object_name': 'TextElement'},
            'element_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'life.textelementtranslation': {
            'Meta': {'object_name': 'TextElementTranslation'},
            'element_name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.TextElement']"}),
            'element_text': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Language']"})
        }
    }

    complete_apps = ['life']
