from django.db import models

class Misc(models.Model):
	iphone_app_link = models.URLField()
	
	main_phone_number = models.CharField(max_length = 30)
	main_contact_email = models.EmailField()
	faq_contact_email = models.EmailField()

	twitter_username = models.CharField(max_length = 30)
	twitter_pass = models.CharField(max_length = 30)

	linkedin_address = models.CharField(max_length = 70)

	def __unicode__(self):
		return u'misc'

	class Meta:
		app_label = "life"