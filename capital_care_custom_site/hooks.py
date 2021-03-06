# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "capital_care_custom_site"
app_title = "Capital Care Custom Site"
app_publisher = "MostafaFekry"
app_description = "Custom Capital Care site"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "mostafa.fekry@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/capital_care_custom_site/css/capital_care_custom_site.css"
# app_include_js = "/assets/capital_care_custom_site/js/capital_care_custom_site.js"

# include js, css files in header of web template
# web_include_css = "/assets/capital_care_custom_site/css/capital_care_custom_site.css"
# web_include_js = "/assets/capital_care_custom_site/js/capital_care_custom_site.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

website_route_rules = [
	{"from_route": "/blog/<category>", "to_route": "Website Blog Category"},
]

# Website user home page (by function)
# get_website_user_home_page = "capital_care_custom_site.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# website
update_website_context = "capital_care_custom_site.utils.update_website_context"


# before_install = "capital_care_custom_site.install.before_install"
# after_install = "capital_care_custom_site.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "capital_care_custom_site.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"capital_care_custom_site.tasks.all"
# 	],
# 	"daily": [
# 		"capital_care_custom_site.tasks.daily"
# 	],
# 	"hourly": [
# 		"capital_care_custom_site.tasks.hourly"
# 	],
# 	"weekly": [
# 		"capital_care_custom_site.tasks.weekly"
# 	]
# 	"monthly": [
# 		"capital_care_custom_site.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "capital_care_custom_site.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "capital_care_custom_site.event.get_events"
# }

# fixtures
fixtures = [{"dt": "Custom Field", "filters": [["name", "in", [
		"Lead-custom_interested_in",
		"Lead-custom_address",
		"Lead-custom_job",
		"Website Slideshow Item-position",
		"Website Slideshow Item-link_path"
	]]]},
	{"dt": "Translation"},
    {"dt": "Website Languages"},
    {"dt": "Web Page", "filters": [["name", "like", 
        "registration-done"
    ]]}
	]


