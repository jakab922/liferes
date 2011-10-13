from django.shortcuts import render_to_response, redirect
from life.views.aux import *
from life.models import *
from django.template import RequestContext

def faq(request, lang_code):
	template_dict = generate_base_dict(lang_code, '/faq/')
	
	template_dict = add_testimonials(template_dict)
	template_dict['faqs'] = FaqTranslation.objects.filter(language__lang_code = lang_code)

	return render_to_response('pages/faq.html', template_dict, context_instance = RequestContext(request))