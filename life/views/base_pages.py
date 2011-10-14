from life.views.aux import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from life.models import TextElementTranslation

def landlords(request, lang_code):
	template_dict = generate_base_dict(lang_code, 'landlords')
	
	template_dict = add_testimonials(template_dict)
	template_dict = add_rows(template_dict, 'landlords')
	template_dict = add_simple_title(template_dict, 'landlords', lang_code)

	return render_to_response('pages/landlords.html', template_dict, context_instance = RequestContext(request))
	
def tenants(request, lang_code):
	template_dict = generate_base_dict(lang_code, 'tenants')
	
	template_dict = add_searchform(template_dict)
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)
	template_dict = add_rows(template_dict, 'tenants')
	template_dict = add_simple_title(template_dict, 'tenants', lang_code)

	return render_to_response('pages/tenants.html', template_dict, context_instance = RequestContext(request))

def buyers(request, lang_code):
	template_dict = generate_base_dict(lang_code, 'buyers')

	template_dict = add_searchform(template_dict)
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)
	template_dict = add_rows(template_dict, 'buyers')
	template_dict = add_simple_title(template_dict, 'buyers', lang_code)

	return render_to_response('pages/buyers.html', template_dict, context_instance = RequestContext(request))

def corporate(request, lang_code):
	template_dict = generate_base_dict(lang_code, 'corporate')

	template_dict = add_searchform(template_dict)
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)
	template_dict = add_rows(template_dict, 'corporate')
	template_dict = add_simple_title(template_dict, 'corporate', lang_code)

	return render_to_response('pages/corporate.html', template_dict, context_instance = RequestContext(request))
	
def currency_exchange(request, lang_code):
	template_dict = generate_base_dict(lang_code, 'currency_exchange')

	template_dict = add_searchform(template_dict)
	template_dict = add_testimonials(template_dict)
	template_dict = add_rows(template_dict, 'currency_exchange')
	template_dict = add_simple_title(template_dict, 'currency_exchange', lang_code)

	return render_to_response('pages/corporate.html', template_dict, context_instance = RequestContext(request))
