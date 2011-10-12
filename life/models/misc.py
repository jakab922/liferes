from django.db import models

class Misc(models.Model):
	iphone_app_link = models.URLField()
	main_phone_number = models.CharField(max_length = 30)

	def __unicode__(self):
		return u'misc'

	class Meta:
		app_label = "life"