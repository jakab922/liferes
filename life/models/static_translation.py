from django.db import models

class TextElement(models.Model):
	element_name = models.CharField(max_length = 200)
	
	def __unicode__(self):
		return unicode(self.element_name)

	class Meta:
		app_label = "life"
		
class TextElementTranslation(models.Model):
	element_name = models.ForeignKey('TextElement')
	element_text = models.TextField()
	language = models.ForeignKey('Language')
	
	def __unicode__(self):
		return unicode((self.language, self.element_name))

	class Meta:
		app_label = "life"