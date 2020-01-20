# -*- coding: utf-8 -*-
# Copyright (c) 2020, MostafaFekry and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.website.website_generator import WebsiteGenerator
from frappe.website.render import clear_cache

class WebsiteBlogCategory(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/blog_category_details.html",
		condition_field = "published",
		page_title_field = "title",
		no_cache = 1
	)
	def autoname(self):
		# to override autoname of WebsiteGenerator
		self.name = self.category_name

	def on_update(self):
		clear_cache()

	def validate(self):
		if not self.route:
			self.route = 'blog/' + self.scrub(self.name)
		super(WebsiteBlogCategory, self).validate()