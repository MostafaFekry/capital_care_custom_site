# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import cint, fmt_money, flt, nowdate, getdate

no_cache = 1
no_sitemap = 1

def get_context(context):

	homepage = frappe.get_doc('Capital Care Website Settings')

	
	if homepage.slideshow:
		context.slideshow = homepage.slideshow
		context.update(get_slideshow_details(homepage.slideshow))
	return context

def get_slideshow_details(slideshow):

	slideshow = frappe.get_doc("Website Slideshow", slideshow)
	if not slideshow:
		return {}

	return {
		"slides": slideshow.get({"doctype":"Website Slideshow Item"}),
		"slideshow_header": slideshow.header or ""
	}

