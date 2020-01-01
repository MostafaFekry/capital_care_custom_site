# -*- coding: utf-8 -*-
# Copyright (c) 2019, MostafaFekry and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.website.website_generator import WebsiteGenerator
from capital_care_custom_site.capital_care_custom_site.doctype.website_header_background.website_header_background import get_website_header_background_details

class PropertyType(WebsiteGenerator):
	website = frappe._dict(
		template = "templates/generators/property_details.html",
		condition_field = "publish",
		page_title_field = "property_type_name",
		no_cache = 1
	)
	
	def validate(self):
		if not self.route:
			self.route = 'property/' +self.scrub(self.property_type_name)
		super(PropertyType, self).validate()
	
	def get_context(self, context):
		context.main_section = self.main_section
		context.main_section_ar = self.main_section_ar
		context.title = self.property_type_name
		context.light_description = self.light_description or ""
		
		if self.page_header_background:
			context.update(get_website_header_background_details(self.page_header_background))
			
			
		
		if self.property_model_item:
		
			property_model_items = frappe.db.sql("""\
			select PM.property_model_name,PM.property_model_title, PM.description, PM.description_ar
			from `tabProperty Model` PM
			inner join `tabProperty Model Item` PMI on PMI.property_model = PM.property_model_name
			where PMI.parent = '{property_type_name}' order by PMI.idx asc""".format(property_type_name=self.name), as_dict=1)
			
			property_model_items = [d for d in property_model_items]
			property_model_items = adjust_property_model_item_details(property_model_items)
			
			context.property_model_items = property_model_items
		
		context.property_model_item = self.property_model_item
				
		context.parents = [
			{"name": frappe._("Home"), "route":"/"},{"name": frappe._("Property"), "route":"/#"}
		]
		
			
		return context


def adjust_property_model_item_details(data):
	adjusted_data = []

	for item in data:
		item['property_model_dimensions'] = [d for d in get_property_model_dimensions(item.get('property_model_name'))]
		item['property_model_photo'] = [d for d in get_property_model_photo(item.get('property_model_name'))]
		adjusted_data.append(item)

	return adjusted_data

def get_property_model_dimensions(model):
	return frappe.db.sql("""\
		select PMD.dimension_name,PMD.dimension, PMD.icon, PMD.total
		from `tabProperty Model Dimensions` PMD
		where PMD.parent = '{property_model_name}' order by PMD.idx asc""".format(property_model_name=model), as_dict=1)

def get_property_model_photo(model):
	return frappe.db.sql("""\
		select PMP.title,PMP.description, PMP.image, PMP.image_hover
		from `tabProperty Model Photo` PMP
		where PMP.parent = '{property_model_name}' order by PMP.idx asc""".format(property_model_name=model), as_dict=1)