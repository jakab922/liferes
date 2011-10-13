# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Language'
        db.create_table('life_language', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lang_code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('lang', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('flag', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('life', ['Language'])

        # Adding model 'StaffMember'
        db.create_table('life_staffmember', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('life', ['StaffMember'])

        # Adding M2M table for field language on 'StaffMember'
        db.create_table('life_staffmember_language', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('staffmember', models.ForeignKey(orm['life.staffmember'], null=False)),
            ('language', models.ForeignKey(orm['life.language'], null=False))
        ))
        db.create_unique('life_staffmember_language', ['staffmember_id', 'language_id'])

        # Adding model 'Faq'
        db.create_table('life_faq', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('life', ['Faq'])

        # Adding model 'FaqTranslation'
        db.create_table('life_faqtranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('faq', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Faq'])),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Language'])),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('answer', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('life', ['FaqTranslation'])

        # Adding model 'Testimonial'
        db.create_table('life_testimonial', (
            ('quote_name', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('life', ['Testimonial'])

        # Adding model 'TestimonialTranslation'
        db.create_table('life_testimonialtranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('testimonial', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Testimonial'])),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Language'])),
            ('quote', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('life', ['TestimonialTranslation'])

        # Adding model 'Address'
        db.create_table('life_address', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('postcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('life', ['Address'])

        # Adding model 'Branch'
        db.create_table('life_branch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Address'])),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=50)),
        ))
        db.send_create_signal('life', ['Branch'])

        # Adding model 'CityPart'
        db.create_table('life_citypart', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cp_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('life', ['CityPart'])

        # Adding model 'District'
        db.create_table('life_district', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('part', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.CityPart'])),
        ))
        db.send_create_signal('life', ['District'])

        # Adding model 'MemberOf'
        db.create_table('life_memberof', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.StaffMember'])),
            ('branch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Branch'])),
        ))
        db.send_create_signal('life', ['MemberOf'])

        # Adding model 'Page'
        db.create_table('life_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lang', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Language'])),
            ('first_row', self.gf('django.db.models.fields.related.ForeignKey')(related_name='first_row_of', to=orm['life.ContentName'])),
            ('second_row', self.gf('django.db.models.fields.related.ForeignKey')(related_name='second_row_of', to=orm['life.ContentName'])),
            ('third_row', self.gf('django.db.models.fields.related.ForeignKey')(related_name='third_row_of', to=orm['life.ContentName'])),
            ('forth_row', self.gf('django.db.models.fields.related.ForeignKey')(related_name='forth_row_of', to=orm['life.ContentName'])),
            ('fifth_row', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fifth_row_of', to=orm['life.ContentName'])),
            ('sixth_row', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sixth_row_of', to=orm['life.ContentName'])),
        ))
        db.send_create_signal('life', ['Page'])

        # Adding model 'ContentName'
        db.create_table('life_contentname', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('life', ['ContentName'])

        # Adding model 'OneColumnRow'
        db.create_table('life_onecolumnrow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('column', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['life.ContentName'], unique=True)),
        ))
        db.send_create_signal('life', ['OneColumnRow'])

        # Adding model 'TwoColumnRow'
        db.create_table('life_twocolumnrow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title1', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('column1', self.gf('django.db.models.fields.TextField')()),
            ('title2', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('column2', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['life.ContentName'], unique=True)),
        ))
        db.send_create_signal('life', ['TwoColumnRow'])

        # Adding model 'ThreeColumnRow'
        db.create_table('life_threecolumnrow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title1', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('column1', self.gf('django.db.models.fields.TextField')()),
            ('title2', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('column2', self.gf('django.db.models.fields.TextField')()),
            ('title3', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('column3', self.gf('django.db.models.fields.TextField')()),
            ('name', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['life.ContentName'], unique=True)),
        ))
        db.send_create_signal('life', ['ThreeColumnRow'])

        # Adding model 'EmptyRow'
        db.create_table('life_emptyrow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['life.ContentName'], unique=True)),
        ))
        db.send_create_signal('life', ['EmptyRow'])

        # Adding model 'ThreePictureRow'
        db.create_table('life_threepicturerow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('pic1', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('label1', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('pic2', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('label2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('pic3', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('label3', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['life.ContentName'], unique=True)),
        ))
        db.send_create_signal('life', ['ThreePictureRow'])

        # Adding model 'FourPictureRow'
        db.create_table('life_fourpicturerow', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('desc', self.gf('django.db.models.fields.TextField')()),
            ('pic1', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('label1', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('pic2', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('label2', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('pic3', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('label3', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('pic4', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('label4', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['life.ContentName'], unique=True)),
        ))
        db.send_create_signal('life', ['FourPictureRow'])

        # Adding model 'RealMedia'
        db.create_table('life_realmedia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('media_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('media', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('life', ['RealMedia'])

        # Adding model 'TabbedMedia'
        db.create_table('life_tabbedmedia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.ContentName'])),
            ('media1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='media1_of', to=orm['life.RealMedia'])),
            ('media2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='media2_of', to=orm['life.RealMedia'])),
            ('media3', self.gf('django.db.models.fields.related.ForeignKey')(related_name='media3_of', to=orm['life.RealMedia'])),
            ('media4', self.gf('django.db.models.fields.related.ForeignKey')(related_name='media4_of', to=orm['life.RealMedia'])),
            ('media5', self.gf('django.db.models.fields.related.ForeignKey')(related_name='media5_of', to=orm['life.RealMedia'])),
        ))
        db.send_create_signal('life', ['TabbedMedia'])

        # Adding model 'NewsLetterSubscription'
        db.create_table('life_newslettersubscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('life', ['NewsLetterSubscription'])

        # Adding model 'NewsLetter'
        db.create_table('life_newsletter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('life', ['NewsLetter'])

        # Adding model 'EmailAlert'
        db.create_table('life_emailalert', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sale_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('location_string', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('min_price', self.gf('django.db.models.fields.IntegerField')()),
            ('max_price', self.gf('django.db.models.fields.IntegerField')()),
            ('min_bedroom', self.gf('django.db.models.fields.IntegerField')()),
            ('max_bedroom', self.gf('django.db.models.fields.IntegerField')()),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('life', ['EmailAlert'])

        # Adding model 'PropertyDescription'
        db.create_table('life_propertydescription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Property'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Language'])),
        ))
        db.send_create_signal('life', ['PropertyDescription'])

        # Adding model 'PropertyThumbnail'
        db.create_table('life_propertythumbnail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Property'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('life', ['PropertyThumbnail'])

        # Adding model 'PropertyCoordinate'
        db.create_table('life_propertycoordinate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Property'])),
            ('longitude', self.gf('django.db.models.fields.FloatField')()),
            ('latitude', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('life', ['PropertyCoordinate'])

        # Adding model 'Property'
        db.create_table('life_property', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property_id', self.gf('django.db.models.fields.IntegerField')()),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('sale_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('style', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('setting', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('age', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('parking', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('tenure_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('status_code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('bed_count', self.gf('django.db.models.fields.IntegerField')()),
            ('bath_count', self.gf('django.db.models.fields.IntegerField')()),
            ('reception_count', self.gf('django.db.models.fields.IntegerField')()),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Address'])),
            ('branch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Branch'])),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.District'])),
        ))
        db.send_create_signal('life', ['Property'])

        # Adding model 'TextElement'
        db.create_table('life_textelement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('element_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('life', ['TextElement'])

        # Adding model 'TextElementTranslation'
        db.create_table('life_textelementtranslation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('element_name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.TextElement'])),
            ('element_text', self.gf('django.db.models.fields.TextField')()),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['life.Language'])),
        ))
        db.send_create_signal('life', ['TextElementTranslation'])

    def backwards(self, orm):
        # Deleting model 'Language'
        db.delete_table('life_language')

        # Deleting model 'StaffMember'
        db.delete_table('life_staffmember')

        # Removing M2M table for field language on 'StaffMember'
        db.delete_table('life_staffmember_language')

        # Deleting model 'Faq'
        db.delete_table('life_faq')

        # Deleting model 'FaqTranslation'
        db.delete_table('life_faqtranslation')

        # Deleting model 'Testimonial'
        db.delete_table('life_testimonial')

        # Deleting model 'TestimonialTranslation'
        db.delete_table('life_testimonialtranslation')

        # Deleting model 'Address'
        db.delete_table('life_address')

        # Deleting model 'Branch'
        db.delete_table('life_branch')

        # Deleting model 'CityPart'
        db.delete_table('life_citypart')

        # Deleting model 'District'
        db.delete_table('life_district')

        # Deleting model 'MemberOf'
        db.delete_table('life_memberof')

        # Deleting model 'Page'
        db.delete_table('life_page')

        # Deleting model 'ContentName'
        db.delete_table('life_contentname')

        # Deleting model 'OneColumnRow'
        db.delete_table('life_onecolumnrow')

        # Deleting model 'TwoColumnRow'
        db.delete_table('life_twocolumnrow')

        # Deleting model 'ThreeColumnRow'
        db.delete_table('life_threecolumnrow')

        # Deleting model 'EmptyRow'
        db.delete_table('life_emptyrow')

        # Deleting model 'ThreePictureRow'
        db.delete_table('life_threepicturerow')

        # Deleting model 'FourPictureRow'
        db.delete_table('life_fourpicturerow')

        # Deleting model 'RealMedia'
        db.delete_table('life_realmedia')

        # Deleting model 'TabbedMedia'
        db.delete_table('life_tabbedmedia')

        # Deleting model 'NewsLetterSubscription'
        db.delete_table('life_newslettersubscription')

        # Deleting model 'NewsLetter'
        db.delete_table('life_newsletter')

        # Deleting model 'EmailAlert'
        db.delete_table('life_emailalert')

        # Deleting model 'PropertyDescription'
        db.delete_table('life_propertydescription')

        # Deleting model 'PropertyThumbnail'
        db.delete_table('life_propertythumbnail')

        # Deleting model 'PropertyCoordinate'
        db.delete_table('life_propertycoordinate')

        # Deleting model 'Property'
        db.delete_table('life_property')

        # Deleting model 'TextElement'
        db.delete_table('life_textelement')

        # Deleting model 'TextElementTranslation'
        db.delete_table('life_textelementtranslation')

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