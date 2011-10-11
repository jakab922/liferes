def landlord_services(request, service_name, lang_code):
	if service_name not in ['property_management', 'tax_advice', 'furnishing', 'client_info', 'engagement_terms']:
		service_name = 'landlord_services' # put base in list and redirect to base if not in list...
		
	template_dict = generate_base_dict(lang_code, '/city_guide/' + service_name + '/')
	
	template_dict['service_name'] = service_name
		
	if service_name == 'property_management':
		template_dict['selflink_text'] = 'Property Management'
	elif service_name == 'tax_advice':
		template_dict['selflink_text'] = 'Tax Advice'
	elif service_name == 'furnishing':
		template_dict['selflink_text'] = 'Furnitures Sales/Rental'
	elif service_name == 'client_info':
		template_dict['selflink_text'] = 'Client Information'
	elif service_name == 'engagement_terms':
		template_dict['selflink_text'] = 'Terms of Engagement'
	else:
		template_dict['selflink_text'] = ''
		
	template_dict['content_name'] = 'elements/landlord_services_content/' + service_name + '.html'
		
	return render_to_response('pages/landlord_services.html', template_dict, context_instance = RequestContext(request))