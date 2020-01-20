# -*- coding: utf-8 -*-
# Copyright (c) 2020, MostafaFekry and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class WebsiteBlogger(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/blogger_details.html",
		condition_field = "publish",
		page_title_field = "full_name",
		no_cache = 1
	)
	
	def validate(self):
		if not self.route:
			self.route = 'blogger/' +self.scrub(self.short_name)
		super(WebsiteBlogger, self).validate()
	
	def get_context(self, context):
		context.title = self.full_name
		context.bio = self.bio
		context.avatar = self.avatar
		context.posts = self.posts
