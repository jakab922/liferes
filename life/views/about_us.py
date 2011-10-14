from life.views.aux import *
from django.shortcuts import render_to_response
from django.template import RequestContext
from life.models import TextElementTranslation as tet
from life.models import *
from collections import namedtuple

def about_us(request, subpage, lang_code):
	template_dict = generate_base_dict(lang_code, 'about_us-' + subpage)
	
	template_dict['subpage'] = subpage
	
	about_us = tet.objects.filter(element_name__element_name = 'title-about_us', language__lang_code = lang_code)[0].element_text

	if subpage == 'our_staff':
		our_staff = tet.objects.filter(element_name__element_name = 'subtitle-about_us-our_staff', language__lang_code = lang_code)[0].element_text
		template_dict['header_text'] = '<h2>{0} <span>- {1}</span></h2>'.format(about_us, our_staff)
		template_dict['container_class'] = "page staff"
		
		# Adding members and branches
		Member = namedtuple("Member", "name, position, email, linkedin_link, thumbnail, languages, introduction")

		template_dict['branches'] = Branch.objects.all()
		for branch in template_dict['branches']:
			branch.members = []
		
		for mof in MemberOf.objects.all():
			for branch in template_dict['branches']:
				if mof.branch.code == branch.code:
					m = Member(mof.staff.name, mof.staff.position, mof.staff.email, mof.staff.linkedin_link, mof.staff.thumbnail, mof.staff.language.all(), mof.staff.introduction)
					branch.members.append(m)
					break
		
	elif subpage == 'recruitment':
		recruitment = tet.objects.filter(element_name__element_name = 'subtitle-about_us-recruitment', language__lang_code = lang_code)[0].element_text
		template_dict['header_text'] = '<h2>{0} <span>- {1}</span></h2>'.format(about_us, recruitment)
		template_dict = add_rows(template_dict, 'about_us-recruitment')
		template_dict['container_class'] = "page about recruitment"
	elif subpage == 'testimonials':
		testimonials = tet.objects.filter(element_name__element_name = 'subtitle-about_us-testimonials', language__lang_code = lang_code)[0].element_text
		template_dict['header_text'] = '<h2>{0} <span>- {1}</span></h2>'.format(about_us, testimonials)
	else:
		template_dict['header_text'] = '<h2>{0}</h2>'.format(about_us)
		template_dict = add_rows(template_dict, 'about_us-base')
		template_dict['container_class'] = "page about"
		
	template_dict = add_staff(template_dict)
	template_dict = add_testimonials(template_dict)
	
	return render_to_response('pages/about_us.html', template_dict, context_instance = RequestContext(request))