# -*- coding: utf-8 -*-
# Copyright (c) 2019, MostafaFekry and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.website.website_generator import WebsiteGenerator
from capital_care_custom_site.capital_care_custom_site.doctype.website_header_background.website_header_background import get_website_header_background_details

class ProjectProgressItems(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/project_progress_details.html",
		condition_field = "publish",
		page_title_field = "project_progress_name",
		no_cache = 1
	)
	
	def validate(self):
		if not self.route:
			self.route = 'projectprogress/' +self.scrub(self.project_progress_name)
		super(ProjectProgressItems, self).validate()
		
		
	def get_context(self, context):
		context.title = self.project_progress_name
		context.light_description = self.light_description or ""
		context.description = self.description
		context.content = self.content
		
		if self.page_header_background:
			context.update(get_website_header_background_details(self.page_header_background))

		
		project_progress_Photo = frappe.db.sql("""\
		select I.media_title, I.media_photo, I.media_photo_hover
		from `tabProject Progress Media` I
		where I.parent = '{project_progress_name}' and I.media_type = 'Photo' order by I.idx asc""".format(project_progress_name=self.name), as_dict=1)
		
		project_progress_Photo = [d for d in project_progress_Photo]
		
		project_progress_Video = frappe.db.sql("""\
		select I.media_title, I.video_embed_url
		from `tabProject Progress Media` I
		where I.parent = '{project_progress_name}' and I.media_type = 'Video' order by I.idx asc""".format(project_progress_name=self.name), as_dict=1)
		
		project_progress_Video = [d for d in project_progress_Video]		
		
		context.update({
			"parents": [{"name": frappe._("Home"), "route":"/"},{"name": frappe._("Project Progress"), "route":"/projectprogress"}],
			"progress_starts_on": self.starts_on,
			"progress_ends_on": self.ends_on,
			"project_progress_Video": project_progress_Video,
			"project_progress_Photo": project_progress_Photo,
		})
		
			
		return context