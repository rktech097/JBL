
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
            sup = frappe.db.get_value("Purchase Receipt", self.reference_name, 'name')
            a = sup.split("-")
            b = a[3]
            frappe.msgprint(self.reference_name)
            frappe.msgprint(sup)
            self.abbr = b
            self.naming_series = "B-.{abbr}.-.###"
            frappe.msgprint(self.naming_series)
            self.batch_id = self.naming_series