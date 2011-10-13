# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Misc.faq_contact_email'
        db.add_column('life_misc', 'faq_contact_email',
                      self.gf('django.db.models.fields.EmailField')(default=0, max_length=75),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Misc.faq_contact_email'
        db.delete_column('life_misc', 'faq_contact_email')

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
        'life.contentname': {
            'Meta': {'object_name': 'ContentName'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'life.district': {
            'Meta': {'object_name': 'District'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'part': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.CityPart']"})
        },
        'life.emailalert': {
            'Meta': {'object_name': 'EmailAlert'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_string': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'max_bedroom': ('django.db.models.fields.IntegerField', [], {}),
            'max_price': ('django.db.models.fields.IntegerField', [], {}),
            'min_bedroom': ('django.db.models.fields.IntegerField', [], {}),
            'min_price': ('django.db.models.fields.IntegerField', [], {}),
            'sale_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'life.emptyrow': {
            'Meta': {'object_name': 'EmptyRow'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['life.ContentName']", 'unique': 'True'})
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
        'life.fourpicturerow': {
            'Meta': {'object_name': 'FourPictureRow'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'label2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'label3': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'label4': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['life.ContentName']", 'unique': 'True'}),
            'pic1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pic4': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'life.language': {
            'Meta': {'object_name': 'Language'},
            'flag': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'lang_code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'})
        },
        'life.memberof': {
            'Meta': {'object_name': 'MemberOf'},
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Branch']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.StaffMember']"})
        },
        'life.misc': {
            'Meta': {'object_name': 'Misc'},
            'faq_contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'iphone_app_link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'linkedin_address': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'main_contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'main_phone_number': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'twitter_pass': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'twitter_username': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'life.newsletter': {
            'Meta': {'object_name': 'NewsLetter'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'life.newslettersubscription': {
            'Meta': {'object_name': 'NewsLetterSubscription'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'life.onecolumnrow': {
            'Meta': {'object_name': 'OneColumnRow'},
            'column': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['life.ContentName']", 'unique': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'life.page': {
            'Meta': {'object_name': 'Page'},
            'fifth_row': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fifth_row_of'", 'to': "orm['life.ContentName']"}),
            'first_row': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'first_row_of'", 'to': "orm['life.ContentName']"}),
            'forth_row': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'forth_row_of'", 'to': "orm['life.ContentName']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'second_row': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'second_row_of'", 'to': "orm['life.ContentName']"}),
            'sixth_row': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sixth_row_of'", 'to': "orm['life.ContentName']"}),
            'third_row': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'third_row_of'", 'to': "orm['life.ContentName']"})
        },
        'life.property': {
            'Meta': {'object_name': 'Property'},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Address']"}),
            'age': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'bath_count': ('django.db.models.fields.IntegerField', [], {}),
            'bed_count': ('django.db.models.fields.IntegerField', [], {}),
            'branch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Branch']"}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.District']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parking': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'property_id': ('django.db.models.fields.IntegerField', [], {}),
            'reception_count': ('django.db.models.fields.IntegerField', [], {}),
            'sale_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'setting': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'status_code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'style': ('django.db.models.fields.CharField', [], {'max_length': '4'}),
            'tenure_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        },
        'life.propertycoordinate': {
            'Meta': {'object_name': 'PropertyCoordinate'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Property']"})
        },
        'life.propertydescription': {
            'Meta': {'object_name': 'PropertyDescription'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Language']"}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Property']"})
        },
        'life.propertythumbnail': {
            'Meta': {'object_name': 'PropertyThumbnail'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'property': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.Property']"})
        },
        'life.realmedia': {
            'Meta': {'object_name': 'RealMedia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'media_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'life.staffmember': {
            'Meta': {'object_name': 'StaffMember'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['life.Language']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'life.tabbedmedia': {
            'Meta': {'object_name': 'TabbedMedia'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media1_of'", 'to': "orm['life.RealMedia']"}),
            'media2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media2_of'", 'to': "orm['life.RealMedia']"}),
            'media3': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media3_of'", 'to': "orm['life.RealMedia']"}),
            'media4': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media4_of'", 'to': "orm['life.RealMedia']"}),
            'media5': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'media5_of'", 'to': "orm['life.RealMedia']"}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['life.ContentName']"})
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
        },
        'life.threecolumnrow': {
            'Meta': {'object_name': 'ThreeColumnRow'},
            'column1': ('django.db.models.fields.TextField', [], {}),
            'column2': ('django.db.models.fields.TextField', [], {}),
            'column3': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['life.ContentName']", 'unique': 'True'}),
            'title1': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title2': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title3': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'life.threepicturerow': {
            'Meta': {'object_name': 'ThreePictureRow'},
            'desc': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label1': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'label2': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'label3': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['life.ContentName']", 'unique': 'True'}),
            'pic1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pic2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'pic3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'life.twocolumnrow': {
            'Meta': {'object_name': 'TwoColumnRow'},
            'column1': ('django.db.models.fields.TextField', [], {}),
            'column2': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['life.ContentName']", 'unique': 'True'}),
            'title1': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'title2': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['life']