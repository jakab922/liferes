from life.views.aux import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from life.models import TextElementTranslation as tet

def about_us(request, subpage, lang_code):
	template_dict = generate_base_dict(lang_code, '/about_us/' + subpage + '/')
	
	template_dict['subpage'] = subpage
	
	about_us = tet.objects.filter(element_name__element_name = 'title-about_us', language__lang_code = lang_code)[0].element_text

	if subpage == 'base':
		template_dict['header_text'] = '<h2>{0}</h2>'.format(about_us)
	elif subpage == 'recruitment':
		recruitment = tet.objects.filter(element_name__element_name = 'subtitle-about_us-recruitment', language__lang_code = lang_code)[0].element_text
		template_dict['container_class'] = '<h2>{0} <span>{1}</span></h2>'.format(about_us, recruitment)
	elif subpage == 'testimonials':
		testimonials = tet.objects.filter(element_name__element_name = 'subtitle-about_us-testimonials', language__lang_code = lang_code)[0].element_text
		template_dict['container_class'] = '<h2>{0} <span>{1}</span></h2>'.format(about_us, testimonials)
	else:
		our_staff = tet.objects.filter(element_name__element_name = 'subtitle-about_us-our_staff', language__lang_code = lang_code)[0].element_text
		template_dict['container_class'] = '<h2>{0} <span>{1}</span></h2>'.format(about_us, our_staff)
		
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)
	
	return render_to_response('pages/about_us.html', template_dict, context_instance = RequestContext(request))