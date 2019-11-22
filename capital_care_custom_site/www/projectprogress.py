# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.doctype.website_slideshow.website_slideshow import get_slideshow
from capital_care_custom_site.capital_care_custom_site.doctype.website_header_background.website_header_background import get_website_header_background_details

no_cache = 1
no_sitemap = 1

def get_context(context):
	context.details = frappe.get_doc("Website Project Progress Settings", "Website Project Progress Settings")
	
	context.title = context.details.title or "Project Progress"
	context.main_section = context.details.main_section or ""
	context.light_description = context.details.light_description or ""
	
	if context.details.page_header_background:
		context.update(get_website_header_background_details(context.details.page_header_background))
	
	context.parents = [
		{ "name": frappe._("Home"), "route": "/" }
	]
	
	project_progress_items = frappe.db.sql("""\
	select PPI.name,PPI.project_progress_name,PPI.starts_on, PPI.ends_on, PPI.description, PPI.route, PPI.last_progress_start_on
	from `tabProject Progress Items` PPI
	where PPI.published = 1 order by PPI.starts_on desc""", as_dict=1)
	
	project_progress_items = [d for d in project_progress_items]
	project_progress_items = adjust_project_progress_items_media(project_progress_items)
	
	context.project_progress_items = project_progress_items

	return context

def adjust_project_progress_items_media(data):
	adjusted_data = []

	for item in data:
		item['project_progress_items_media'] = [d for d in get_project_progress_items_media(item.get('name'))]
		adjusted_data.append(item)

	return adjusted_data

def get_project_progress_items_media(parent):
	return frappe.db.sql("""\
		select PPM.media_title,PPM.media_type, PPM.media_photo, PPM.media_photo_hover, PPM.video_embed_url
		from `tabProject Progress Media` PPM
		where PPM.parent = '{project_progress_name}' and PPM.display_on_main_page = 1 order by PPM.idx asc""".format(project_progress_name=parent), as_dict=1)