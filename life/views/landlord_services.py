from life.views.aux import *
from django.shortcuts import render_to_response
from django.template import RequestContext

def landlord_services(request, service_name, lang_code):
	template_dict = generate_base_dict(lang_code, '/landlord_services/' + service_name + '/')
	
	template_dict = add_rows(template_dict, 'landlord_services-' + service_name)
		
	return render_to_response('pages/landlord_services.html', template_dict, context_instance = RequestContext(request))