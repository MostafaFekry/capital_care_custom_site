# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import throw, msgprint, _
from frappe.utils import get_request_site_address, encode
from frappe.model.document import Document
from capital_care_custom_site.capital_care_custom_site.doctype.website_header_background.website_header_background import get_website_header_background_details

def update_website_context(context):
	website_languages_request = frappe.form_dict._lang
	if website_languages_request:
		context["website_languages_request"] = website_languages_request
	else:
		default_website_languages_item = get_default_website_languages()
		if default_website_languages_item:
			for item in default_website_languages_item:
				if item.get("language"):
					context["mytestnew"] = item.get("language")
					context["website_languages_request"] = item.get("language")
					website_languages_request = item.get("language")
				else:
					context["mytest"] = "Fekry"
					context["website_languages_request"] = "en"
					website_languages_request = "en"
		else:
			context["website_languages_request"] = "en"
			website_languages_request = "en"
	
	context["website_languages_items"] = get_website_languages_items()
	if context["website_languages_items"]:
		context.update(get_website_languages_details(website_languages_request))
	
	website_settings = frappe.get_doc('Capital Care Website Settings')
	context["enable_multilanguage_support"] = website_settings.enable_multilanguage_support
	context["display_language_picker_in_top_bar"] = website_settings.display_language_picker_in_top_bar
	
	if website_settings.page_header_background:
		context.update(get_website_header_background_details(website_settings.page_header_background))
	
	context["website_social_media_item"] = website_settings.website_social_media_item

def get_default_website_languages():
	all_language_items = frappe.db.sql("""\
		select language from `tabWebsite Languages`
		where parent='Capital Care Website Settings' 
		order by idx asc LIMIT 1""", as_dict=1)
	if all_language_items:
		website_languages_items = [d for d in all_language_items]
	else:
		website_languages_items = []
	return website_languages_items

def get_website_languages_items():
	all_language_items = frappe.db.sql("""\
		select * from `tabWebsite Languages`
		where parent='Capital Care Website Settings' 
		order by idx asc""", as_dict=1)
	if all_language_items:
		website_languages_items = [d for d in all_language_items]
	else:
		website_languages_items = []
	return website_languages_items


def get_website_languages_details(website_languages_request="en"):
	website_languages_details = frappe.get_doc("Website Languages", website_languages_request)
	if not website_languages_details:
		return {}

	return {
		"website_languages_name": website_languages_details.language_name,
		"website_languages_flag": website_languages_details.language_flag,
		"main_page_title": website_languages_details.main_page_title,
		"hotline_title": website_languages_details.hotline_title,
		"hotline_details": website_languages_details.hotline_details,
		"slogan": website_languages_details.slogan,
		"download_brochure_title": website_languages_details.download_brochure_title,
		"download_brochure_link": website_languages_details.download_brochure_link,
		"developed_by_title": website_languages_details.developed_by_title,
		"hendaza_logo_description": website_languages_details.hendaza_logo_description,
		"eye_world_logo_description": website_languages_details.eye_world_logo_description,
		"website_languages_copyright": website_languages_details.copyright
	}
	
@frappe.whitelist(allow_guest=True)
def create_lead_for_item_inquiry(lead,mobile,email, subject, message):

	lead_doc = frappe.new_doc('Lead')
	lead_doc.lead_name = lead
	lead_doc.mobile_no = mobile
	lead_doc.email_id = email
	lead_doc.status = 'Lead'
	lead_doc.lead_owner = ''
	
	try:
		lead_doc.insert(ignore_permissions=True)
		lead_doc.save(ignore_permissions=True)
	except frappe.exceptions.DuplicateEntryError:
		frappe.clear_messages()
		lead_doc = frappe.get_doc('Lead', {'email_id': email})

	lead_doc.add_comment('Comment', text='''
		{subject}:{message}
	'''.format(subject=subject, message=message))

	return "okay"

@frappe.whitelist(allow_guest=True)
def create_lead_for_landingpage(lead,mobile,email, subject,interestedin, address,job):

	lead_doc = frappe.new_doc('Lead')
	lead_doc.lead_name = lead
	lead_doc.mobile_no = mobile
	lead_doc.email_id = email
	lead_doc.custom_address = address
	lead_doc.custom_job = job
	lead_doc.custom_interested_in = interestedin
	lead_doc.status = 'Lead'
	lead_doc.lead_owner = ''
	
	try:
		lead_doc.insert(ignore_permissions=True)
		lead_doc.save(ignore_permissions=True)
	except frappe.exceptions.DuplicateEntryError:
		frappe.clear_messages()
		lead_doc = frappe.get_doc('Lead', {'email_id': email})

	lead_doc.add_comment('Comment', text='''
		{subject}: \n Interested in :{message}
	'''.format(subject=subject, message=interestedin))

	return "okay"