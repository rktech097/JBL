
from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
from frappe.model.naming import make_autoname, revert_series_if_last
from frappe.utils import cint, flt, get_link_to_form
from frappe.utils.data import add_days
from frappe.utils.jinja import render_template
from six import text_type
class Batch(Document):
    def autoname(self):
        if self.reference_doctype =="Purchase Receipt":
            docname = frappe.db.get_value("Purchase Receipt", self.reference_name, 'name')
            name_split = docname.split("-")
            abbr = name_split[3]
            self.abbr = abbr
            self.naming_series = "B-.{abbr}.-.###"
            self.batch_id = self.naming_series
