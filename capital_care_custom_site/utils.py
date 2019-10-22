# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe import throw, msgprint, _
from frappe.utils import get_request_site_address, encode
from frappe.model.document import Document
from capital_care_custom_site.capital_care_custom_site.doctype.website_header_background.website_header_background import get_website_header_background_details

def update_website_context(context):
	website_settings = frappe.get_doc('Capital Care Website Settings')
	if website_settings.page_header_background:
		context.update(get_website_header_background_details(website_settings.page_header_background))
	
	context["website_social_media_item"] = website_settings.website_social_media_item
	
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