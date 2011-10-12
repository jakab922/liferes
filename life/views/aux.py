from life.models import *

def generate_base_dict(lang_code, pagename):
	languages = [(langobj.lang_code, langobj.lang) for langobj in Language.objects.all()]
	
	for language in languages: # The current langauge need to be selected
		if language[0] == lang_code:
			languages.remove(language)
			languages = [language] + languages
			break
	
	return {'pagename': pagename, 'curr_lang_code': lang_code, 'curr_lang': Language.objects.filter(lang_code = lang_code)[0].lang, 'curr_flag': Language.objects.filter(lang_code = lang_code)[0].flag, 'languages': languages}
	

def add_searchform(template_dict):
	# TODO: should change after adding translations and shit...
	template_dict['searchform_types'] = type_choices
	
	template_dict['sales_min_prices'] = [25000 * i for i in range(1,17)] + [450000] + [i * 100000 for i in range(5,10)]
	template_dict['sales_max_prices'] = [25000 * i for i in range(2,17)] + [450000] + [i * 100000 for i in range(5,10)] + [1000000]
	template_dict['rentals_min_prices'] = [250 * i for i in range(1,9)] + [500 * i for i in range(5,10)]
	template_dict['rentals_max_prices'] = [250 * i for i in range(2,9)] + [500 * i for i in range(5,10)] + [5000]
	
	template_dict['min_bedrooms'] = [i for i in range(7)]
	template_dict['max_bedrooms'] = [i for i in range(1,8)]

	if 'property_ids' in template_dict:
		template_dict = add_map_details(template_dict)
		print "We've got some property ids"
	else:
		print "We have no property ids"
		template_dict['property_ids'] = []
		template_dict['property_coords'] = []

	return template_dict
	
def add_testimonials(template_dict):
	template_dict['testimonials'] = [(t.testimonial.name, t.testimonial.date, t.quote) for t in TestimonialTranslation.objects.filter(language__lang_code = template_dict['curr_lang_code'])]
	
	return template_dict
	
def add_staff(template_dict):
	template_dict['staff'] = StaffMember.objects.all()

	return template_dict

def add_map_details(template_dict):
	coords = []

	for prop_id in template_dict['property_ids']:
		print type(prop_id), prop_id
		ccord = PropertyCoordinate.objects.filter(property__property_id = prop_id)[0]
		print ccord
		coords.append(ccord.latitude)
		coords.append(ccord.longitude)

	template_dict['property_coords'] = coords
	return template_dict

def add_rows(template_dict, page_name):
	print 'got called with page name:', page_name
	page = Page.objects.filter(name = page_name, lang__lang_code = template_dict['curr_lang_code'])[0]

	names = []
	if page.first_row.name != 'empty':
		names.append(page.first_row.name)
	if page.second_row.name != 'empty':
		names.append(page.second_row.name)
	if page.third_row.name != 'empty':
		names.append(page.third_row.name)
	if page.forth_row.name != 'empty':
		names.append(page.forth_row.name)
	if page.fifth_row.name != 'empty':
		names.append(page.fifth_row.name)
	if page.sixth_row.name != 'empty':
		names.append(page.sixth_row.name)

	results = []

	for name in names:
		res = OneColumnRow.objects.filter(name__name = name)
		if len(res) != 0:
			results.append(('onecol', res[0]))
			continue
		res = TwoColumnRow.objects.filter(name__name = name)
		if len(res) != 0:
			results.append(('twocol', res[0]))
			continue
		res = ThreeColumnRow.objects.filter(name__name = name)
		if len(res) != 0:
			results.append(('threecol', res[0]))
			continue
		res = ThreePictureRow.objects.filter(name__name = name)
		if len(res) != 0:
			results.append(('threepic', res[0]))
			continue
		res = FourPictureRow.objects.filter(name__name = name)
		if len(res) != 0:
			results.append(('fourpic', res[0]))
			continue
		res = TabbedMedia.objects.filter(name__name = name)
		if len(res) != 0:
			res[0].media = []

			if res[0].media1.name != 'empty':
				if res[0].media1.media_type == 'i':
					res[0].media.append(('image', res[0].media1.media))
				else:
					res[0].media.append(('video', res[0].media1.media))

			if res[0].media2.name != 'empty':
				if res[0].media2.media_type == 'i':
					res[0].media.append(('image', res[0].media2.media))
				else:
					res[0].media.append(('video', res[0].media2.media))

			if res[0].media3.name != 'empty':
				if res[0].media3.media_type == 'i':
					res[0].media.append(('image', res[0].media3.media))
				else:
					res[0].media.append(('video', res[0].media3.media))

			if res[0].media4.name != 'empty':
				if res[0].media4.media_type == 'i':
					res[0].media.append(('image', res[0].media4.media))
				else:
					res[0].media.append(('video', res[0].media4.media))

			if res[0].media5.name != 'empty':
				if res[0].media5.media_type == 'i':
					res[0].media.append(('image', res[0].media5.media))
				else:
					res[0].media.append(('video', res[0].media5.media))
			
			results.append(('tabbed', res[0]))

	template_dict['rows'] = results
	return template_dict

def add_simple_title(template_dict, page_name, lang_code):
	template_dict['header_text'] = '<h2>' + TextElementTranslation.objects.filter(element_name__element_name = 'title-' + page_name, language__lang_code = lang_code)[0].element_text + '</h2>'
	return template_dict