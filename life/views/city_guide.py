def city_guide(request, area, lang_code):
	if area not in ['central']:
		area = 'all'
	
	template_dict = generate_base_dict(lang_code, '/city_guide/' + area + '/')
	
	template_dict['area_name'] = area
		
	template_dict['content_name'] = 'elements/city_guide_content/' + area + '.html'
	
	if area == 'all':
		template_dict['container_class'] = 'page guide'
	else:
		template_dict['container_class'] = 'page guide area'
		
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)
		
	return render_to_response('pages/city_guide.html', template_dict, context_instance = RequestContext(request))