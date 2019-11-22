from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Web Site"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Web Page",
					"description": _("Content web page."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Web Form",
					"description": _("User editable form on Website."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Website Header Background",
					"description": _("Embed image Header Background in website pages."),
				},
				{
					"type": "doctype",
					"name": "Website Slideshow",
					"description": _("Embed image slideshows in website pages."),
				},
				{
					"type": "doctype",
					"name": "Website Route Meta",
					"description": _("Add meta tags to your web pages"),
				},
			]
		},
		{
			"label": _("Pages"),
			"items": [
				{
					"type": "doctype",
					"name": "Website About Us Settings",
					"description": _("Settings for About Us Page."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Website Facilities Settings",
					"description": _("Settings for Facilities Page."),
				},
				{
					"type": "doctype",
					"name": "Website Location Settings",
					"description": _("Settings for Location Page."),
				},
				{
					"type": "doctype",
					"name": "Website Media Settings",
					"description": _("Settings for Media Page."),
				},
				{
					"type": "doctype",
					"name": "Website Landing Page Setting",
					"description": _("Settings for Landing Page."),
				},
				{
					"type": "doctype",
					"name": "Website Contact Us Settings",
					"description": _("Settings for Contact Us Page."),
					"onboard": 1,
				},
			]
		},
		{
			"label": _("Setup"),
			"icon": "fa fa-cog",
			"items": [
				{
					"type": "doctype",
					"name": "Website Settings",
					"description": _("Setup of top navigation bar, footer and logo."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Capital Care Website Settings",
					"description": _("Setup of Capital Care Website Settings."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Website Social Media",
					"description": _("List of Website Social Media."),
				},
			]
		},
		{
			"label": _("Property"),
			"items": [
				{
					"type": "doctype",
					"name": "Property Type",
					"label": _("Property Type"),
				},
				{
					"type": "doctype",
					"name": "Property Model",
					"label": _("Property Model"),
				},
			]
		},
		{
			"label": _("Project Progress"),
			"items": [
				{
					"type": "doctype",
					"name": "Website Project Progress Settings",
					"label": _("Website Project Progress Settings"),
				},
				{
					"type": "doctype",
					"name": "Project Progress Items",
					"label": _("Project Progress Items"),
				},
			]
		},
		{
			"label": _("Form"),
			"items": [
				{
					"type": "doctype",
					"name": "Broker Request",
					"label": _("Broker Request Form"),
				}	,
			]
		},

	]