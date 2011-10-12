from django.db import models

class Page(models.Model):
	name = models.CharField(max_length = 50)
	lang = models.ForeignKey('Language')
	first_row = models.ForeignKey('ContentName', related_name="first_row_of")
	second_row = models.ForeignKey('ContentName', related_name="second_row_of")
	third_row = models.ForeignKey('ContentName', related_name="third_row_of")
	forth_row = models.ForeignKey('ContentName', related_name="forth_row_of")
	fifth_row = models.ForeignKey('ContentName', related_name="fifth_row_of")
	sixth_row = models.ForeignKey('ContentName', related_name="sixth_row_of")

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		app_label = "life"

class ContentName(models.Model):
	name = models.CharField(max_length = 30)

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		app_label = "life"

class OneColumnRow(models.Model):
	title = models.CharField(max_length = 30)
	column = models.TextField()
	name = models.OneToOneField('ContentName')

	def __unicode__(self):
		return unicode(self.name.name)

	class Meta:
		app_label = "life"

class TwoColumnRow(models.Model):
	title1 = models.CharField(max_length = 30)
	column1 = models.TextField()
	title2 = models.CharField(max_length = 30)
	column2 = models.TextField()
	name = models.OneToOneField('ContentName')

	def __unicode__(self):
		return unicode(self.name.name)

	class Meta:
		app_label = "life"

class ThreeColumnRow(models.Model):
	title1 = models.CharField(max_length = 30)
	column1 = models.TextField()
	title2 = models.CharField(max_length = 30)
	column2 = models.TextField()
	title3 = models.CharField(max_length = 30)
	column3 = models.TextField()
	name = models.OneToOneField('ContentName')

	def __unicode__(self):
		return unicode(self.name.name)

	class Meta:
		app_label = "life"

class EmptyRow(models.Model):
	name = models.OneToOneField('ContentName')

	def __unicode__(self):
		return u'empty'

	class Meta:
		app_label = "life"

class ThreePictureRow(models.Model):
	title = models.CharField(max_length = 30)
	desc = models.TextField()
	pic1 = models.ImageField(upload_to = 'images/picrows')
	label1 = models.CharField(max_length = 20)
	pic2 = models.ImageField(upload_to = 'images/picrows')
	label2 = models.CharField(max_length = 20)
	pic3 = models.ImageField(upload_to = 'images/picrows')
	label3 = models.CharField(max_length = 20)
	name = models.OneToOneField('ContentName')

	def __unicode__(self):
		return unicode(self.name.name)

	class Meta:
		app_label = "life"

class FourPictureRow(models.Model):
	title = models.CharField(max_length = 30)
	desc = models.TextField()
	pic1 = models.ImageField(upload_to = 'images/picrows')
	label1 = models.CharField(max_length = 20)
	pic2 = models.ImageField(upload_to = 'images/picrows')
	label2 = models.CharField(max_length = 20)
	pic3 = models.ImageField(upload_to = 'images/picrows')
	label3 = models.CharField(max_length = 20)
	pic4 = models.ImageField(upload_to = 'images/picrows')
	label4 = models.CharField(max_length = 20)
	name = models.OneToOneField('ContentName')

	def __unicode__(self):
		return unicode(self.name.name)

	class Meta:
		app_label = "life"

media_type_choices = (('v', 'Video'), ('i', 'Image'))

class RealMedia(models.Model):
	name = models.CharField(max_length = 30, unique = True)
	media_type = models.CharField(max_length = 1, choices = media_type_choices)
	media = models.FileField(upload_to = 'tabbed_media')

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		app_label = "life"

class TabbedMedia(models.Model):
	name = models.ForeignKey('ContentName')
	media1 = models.ForeignKey('RealMedia', related_name = 'media1_of')
	media2 = models.ForeignKey('RealMedia', related_name = 'media2_of')
	media3 = models.ForeignKey('RealMedia', related_name = 'media3_of')
	media4 = models.ForeignKey('RealMedia', related_name = 'media4_of')
	media5 = models.ForeignKey('RealMedia', related_name = 'media5_of')

	def __unicode__(self):
		return unicode(self.name.name)

	class Meta:
		app_label = "life"