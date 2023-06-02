import frappe
from frappe.model.document import Document

class Batch(Document):
    def autoname(self):
        if self.reference_doctype =="Purchase Receipt":
            docname = frappe.db.get_value("Purchase Receipt", self.reference_name, 'name')
            name_split = docname.split("/")
            abbr = name_split[2]
            self.abbr = abbr
            self.naming_series = "B-.{abbr}.-.###"
            self.batch_id = self.naming_series
