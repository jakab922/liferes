from django.db import models
from life.models import *

class PropertyDescription(models.Model):
	property = models.ForeignKey('Property')
	description = models.TextField()
	language = models.ForeignKey('Language')

	def __unicode__(self):
		if len(self.description) < 60:
			return unicode(self.description)
		else:
			return unicode(self.description[:60] + '...')

	class Meta:
		app_label = "life"

class PropertyThumbnail(models.Model):
	property = models.ForeignKey('Property')
	image = models.ImageField(upload_to = 'images/properties')

	def __unicode__(self):
		return unicode(self.image)

	class Meta:
		app_label = "life"

class PropertyCoordinate(models.Model):
	property = models.ForeignKey('Property')
	longitude = models.FloatField()
	latitude = models.FloatField()

	def __unicode__(self):
		return unicode(self.property.address.address + u'-' + self.property.address.postcode + u'-' + unicode(self.latitude) + u', ' + unicode(self.longitude))

	class Meta:
		app_label = "life"

type_choices = (('APTEN', 'Apartment (tenanted)'), ('APVAC', 'Apartment (vacant)'), ('DETA', 'Detached'), ('ENDT', 'End Of Terrace'), ('FLAT', 'High-rise'), ('HSTEN', 'House (tenanted)'), ('HSVAC', 'House (vacant)'), ('SEMI', 'Semi Detached'), ('STTEN', 'Studio (tenanted)'), ('STVAC', 'Studio (vacant)'), ('MID', 'Terraced'), ('NA', 'Not specified'))
style_choices = (('1FLR', '1st Floor'), ('2FLR', '2nd Floor'), ('2', '3rd Floor '), ('4', '4th Floor '), ('5', '5th Floor '), ('6', '6th Floor '), ('7', '7th Floor '), ('8', '8th Floor '), ('9', '9th Floor '), ('10', '10th Floor '), ('11', '11th Floor '), ('12', '12th Floor '), ('13', '13th Floor '), ('14', '14th Floor '), ('15', '15th Floor'), ('16', '16th Floor '), ('17', '17th Floor '), ('18', '18th Floor '), ('19', '19th Floor '), ('20', '20th Floor'), ('21', '21st Floor '), ('22', '22nd Floor '), ('23', '23rd Floor'), ('24', '24th Floor'), ('25', '25th Floor'), ('26', '26th Floor'), ('27', '27th Floor'), ('28', '28th Floor'), ('29', '29th Floor'), ('30', '30th Floor'), ('31', '31st Floor'), ('32', '32nd Floor'), ('33', '33rd Floor'), ('34', '34th Floor'), ('35', '35th Floor'), ('36', '36th Floor'), ('37', '37th Floor'), ('38', '38th Floor'), ('39', '39th Floor'), ('40', '40th Floor'), ('41', '41st Floor'), ('42', '42nd Floor'), ('43', '43rd Floor'), ('44', '44th Floor'), ('45', '45th Floor'), ('DUP', 'Duplex'), ('MAIS', 'Maisonette'), ('SEMI', 'Semi-Detached'), ('NA', 'Not specified'))
age_choices = (('NEW', 'New'), ('TENT', 'Tenanted '), ('VAC', 'Vacant '), ('VICT', 'Victorian'), ('EDWA', 'Edwardian'), ('80S', 'Eighties'), ('50S', 'Fifties'), ('40S', 'Fourties'), ('NEOG', 'Georgian'), ('90S', 'Nineties'), ('REGCY', 'Regency'), ('70S', 'Seventies'), ('60S', 'Sixties'), ('30S', 'Thirties'))
parking_choices = (('NOP', 'No Parking'), ('PARK', 'Parking'), ('NA', 'Not specified'))
setting_choices = (('CITY', 'City'), ('RVR', 'Riverside'))
tenure_type_choices = (('F', 'Freehold'), ('L', 'Leasehold'), ('N', 'Not Known'), ('D', 'Feudal'), ('S', 'Share of Freehold'), ('V', 'Vendor to Confirm'))
status_code_choices = (('AV_LET', 'Available to let'), ('AVAI', 'For Sale'), ('REACTIVATE', 'Reactivated'), ('SSTC', 'Sold subject to contract'), ('UO', 'Under Offer'), ('VALUE', 'Valuation'), ('WEBPROS', 'Web Prospect'), ('WITH', 'Withdrawn'))
sale_type_choices = (('S', 'Sale'), ('R', 'Rent'))

class Property(models.Model):
	property_id = models.IntegerField()
	price = models.IntegerField()

	sale_type = models.CharField(max_length = 1, choices = sale_type_choices)
	type = models.CharField(max_length = 5, choices = type_choices)
	style = models.CharField(max_length = 4, choices = style_choices)
	setting = models.CharField(max_length = 4, choices = setting_choices)
	age = models.CharField(max_length = 4, choices = age_choices)
	parking = models.CharField(max_length = 4, choices = parking_choices)
	tenure_type = models.CharField(max_length = 1, choices = tenure_type_choices)
	status_code = models.CharField(max_length = 10, choices = status_code_choices)
	bed_count = models.IntegerField()
	bath_count = models.IntegerField()
	reception_count = models.IntegerField()

	address = models.ForeignKey('Address')
	branch = models.ForeignKey('Branch')
	district = models.ForeignKey('District')

	def __unicode__(self):
		return unicode((self.id, self.address))

	class Meta:
		verbose_name_plural = "Properties"
		app_label = "life"