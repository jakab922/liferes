from django.db import models

class Language(models.Model):
	lang_code = models.CharField(max_length = 2, unique = True)
	lang = models.CharField(max_length = 50, unique = True)
	flag = models.ImageField(upload_to = 'images/flags')
	
	def __unicode__(self):
		return unicode(self.lang)

	class Meta:
		app_label = "life"

class StaffMember(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField()
	thumbnail = models.ImageField(upload_to = 'images/thumbnails')
	language = models.ManyToManyField('Language')
	
	def __unicode__(self):
		return unicode((self.id, self.name))

	class Meta:
		app_label = "life"
		
class Faq(models.Model):
	name = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		app_label = "life"

class FaqTranslation(models.Model):
	faq = models.ForeignKey('Faq')
	language = models.ForeignKey('Language')
	question = models.CharField(max_length = 200)
	answer = models.TextField()

	def __unicode__(self):
		return unicode(self.question)

	class Meta:
		app_label = "life"

class Testimonial(models.Model):
	quote_name = models.CharField(max_length = 50, primary_key = True)
	name = models.CharField(max_length = 200)
	date = models.DateTimeField()
	
	def __unicode__(self):
		return unicode(self.quote_name)

	class Meta:
		app_label = "life"
			
class TestimonialTranslation(models.Model):
	testimonial = models.ForeignKey('Testimonial')
	language = models.ForeignKey('Language')
	quote = models.TextField()
	
	def __unicode__(self):
		if len(self.quote) < 60:
			return unicode(self.quote)
		else:
			return unicode(self.quote[:60] + '...')

	class Meta:
		app_label = "life"

class Address(models.Model):
	address = models.CharField(max_length = 200)
	city = models.CharField(max_length = 50)
	postcode = models.CharField(max_length = 10)
	
	def __unicode__(self):
		return unicode(self.address + ', ' + self.city)
		
	class Meta:
		verbose_name_plural = "Addresses"
		app_label = "life"

class Branch(models.Model):
	code = models.CharField(max_length = 10)
	name = models.CharField(max_length = 50)
	address = models.ForeignKey('Address')
	phone = models.CharField(max_length = 30)
	fax = models.CharField(max_length = 30)
	email = models.EmailField(max_length = 50)
	
	def __unicode__(self):
		return unicode(self.name)
		
	class Meta:
		verbose_name_plural = "Branches"
		app_label = "life"
		
class CityPart(models.Model):
	cp_id = models.IntegerField("id")
	name = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		app_label = "life"
		
class District(models.Model):
	name = models.CharField(max_length = 50)
	part = models.ForeignKey('CityPart')
	
	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		app_label = "life"

class MemberOf(models.Model):
	staff = models.ForeignKey('StaffMember')
	branch = models.ForeignKey('Branch')

	def __unicode__(self):
		return unicode(self.staff.name + ' at ' + self.branch.name)

	class Meta:
		app_label = "life"