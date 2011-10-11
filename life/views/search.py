def search(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/search/')
	if request.method == 'POST':
		query_dict = {}

		if 'shortlist_ids' in request.POST:
			print 'shortlist_ids', request.POST['shortlist_ids']
			query_dict['property_id__in'] = parse_json(request.POST['shortlist_ids'])
		else:
			query_dict['sale_type'] = request.POST['sale_type']
			
			placeholder = TextElementTranslation.objects.filter(language__lang_code = lang_code, element_name__element_name = 'searchboxes-form-location_placeholder')[0].element_text
			if request.POST['district'] != placeholder:
				query_dict['district__name__icontains'] = request.POST['district']
			
			if request.POST['type'] != 'NA':
				query_dict['type'] = request.POST['type']
			
			query_dict['price__gte'] = request.POST['min_price']
			query_dict['price__lte'] = request.POST['max_price']
			query_dict['bed_count__gte'] = request.POST['min_bedrooms']
			query_dict['bed_count__lte'] = request.POST['max_bedrooms']

		print query_dict

		template_dict['search_results'] = Property.objects.filter(**query_dict).order_by('price')
	else:
		template_dict['search_results'] = Property.objects.all().order_by('price')

	template_dict['property_ids'] = [p.property_id for p in template_dict['search_results']]

	# Gathering images for the properties
	for i in range(len(template_dict['search_results'])):
		template_dict['search_results'][i].searchimages = [sub(r'(.*/)([^/]+)', r'\1searchpage/\2', j.image.name) for j in PropertyThumbnail.objects.filter(property__property_id = template_dict['search_results'][i].property_id)][1:5]

	for result in template_dict['search_results']:
		desc = PropertyDescription.objects.filter(language__lang_code = lang_code, property__property_id = result.property_id)[0].description
		if len(desc) >= 150:
			result.description = desc[:150] + '...'
		else:
			result.description = desc
	
	template_dict = add_searchform(template_dict)
	template_dict = add_testimonials(template_dict)

	price_low_to_high_text = TextElementTranslation.objects.filter(language__lang_code = lang_code, element_name__element_name = 'search-ordering_price_low_to_high')[0].element_text
	price_high_to_low_text = TextElementTranslation.objects.filter(language__lang_code = lang_code, element_name__element_name = 'search-ordering_price_high_to_low')[0].element_text
	template_dict['ordering_dict'] = {'plh': price_low_to_high_text, 'phl': price_high_to_low_text};
	template_dict['default_ordering'] = 'plh'

	all_text = TextElementTranslation.objects.filter(language__lang_code = lang_code, element_name__element_name = 'search-all_text')[0].element_text
	template_dict['result_per_page_dict'] = [(5,'5'), (10,'10'), (15,'15'), (99999999, all_text)]
	template_dict['default_result_per_page'] = 5
	
	print template_dict

	return render_to_response('pages/search.html', template_dict, context_instance = RequestContext(request))