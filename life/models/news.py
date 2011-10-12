from django.db import models
from life.models import *

newsletter_frequency_choices = (('w','weekly'),('m','monthly'))
sale_type_choices = (('S', 'Sale'), ('R', 'Rent'))
type_choices = (('APTEN', 'Apartment (tenanted)'), ('APVAC', 'Apartment (vacant)'), ('DETA', 'Detached'), ('ENDT', 'End Of Terrace'), ('FLAT', 'High-rise'), ('HSTEN', 'House (tenanted)'), ('HSVAC', 'House (vacant)'), ('SEMI', 'Semi Detached'), ('STTEN', 'Studio (tenanted)'), ('STVAC', 'Studio (vacant)'), ('MID', 'Terraced'), ('NA', 'Not specified'))

class NewsLetterSubscription(models.Model):
	frequency = models.CharField(max_length = 1, choices = newsletter_frequency_choices)
	email = models.EmailField()

	def __unicode__(self):
		return unicode(self.email)

	class Meta:
		app_label = "life"

class NewsLetter(models.Model):
	title = models.CharField(max_length = 30)
	body = models.TextField()
	date = models.DateField()

	def __unicode__(self):
		return unicode(self.title)

	class Meta:
		app_label = "life"

class EmailAlert(models.Model):
	sale_type = models.CharField(max_length = 1, choices = sale_type_choices)
	location_string = models.CharField(max_length = 50)
	type = models.CharField(max_length = 5, choices = type_choices)
	min_price = models.IntegerField()
	max_price = models.IntegerField()
	min_bedroom = models.IntegerField()
	max_bedroom = models.IntegerField()

	frequency = models.CharField(max_length = 1, choices = newsletter_frequency_choices)
	email = models.EmailField()

	def __unicode__(self):
		return unicode(self.email)

	class Meta:
		app_label = "life"