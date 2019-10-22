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
			"label": _("Blog"),
			"items": [
				{
					"type": "doctype",
					"name": "Blog Post",
					"description": _("Single Post (article)."),
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Blogger",
					"description": _("A user who posts blogs."),
				},
				{
					"type": "doctype",
					"name": "Blog Category",
					"description": _("Categorize blog posts."),
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
				{
					"type": "doctype",
					"name": "About Us Settings",
					"description": _("Settings for About Us Page."),
				},
				{
					"type": "doctype",
					"name": "Contact Us Settings",
					"description": _("Settings for Contact Us Page."),
				},
			]
		},
		{
			"label": _("Portal"),
			"items": [
				{
					"type": "doctype",
					"name": "Portal Settings",
					"label": _("Portal Settings"),
					"onboard": 1,
				}
			]
		},
		{
			"label": _("Knowledge Base"),
			"items": [
				{
					"type": "doctype",
					"name": "Help Category",
				},
				{
					"type": "doctype",
					"name": "Help Article",
				},
			]
		},

	]