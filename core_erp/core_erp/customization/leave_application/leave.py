import frappe
from datetime import datetime
from frappe.utils import date_diff

def validate(self, method = None):
    staff = frappe.db.get_value('Employee', self.employee, 'position')
    today_date = datetime.now().strftime('%Y-%m-%d')
    days_diff = frappe.utils.date_diff(self.to_date, self.from_date)
    today_days_diff = frappe.utils.date_diff(self.from_date, today_date)
    
    if staff == 'Staff':
        if days_diff < 3 and today_days_diff < 3 and self.is__compensatory == False and not self.is_emergency:
            frappe.throw("You have to create leave application in 3 Days advance.")
        elif days_diff >= 3 and today_days_diff < 15 and self.is__compensatory == False and not self.is_emergency:
            frappe.throw("You have to create leave application in 15 Days advance.")
                    
    elif staff == 'Worker':
        if days_diff < 3  and today_days_diff < 7 and self.is__compensatory == False and not self.is_emergency:
            frappe.throw("You have to create leave application in 7 Days advance.")
        elif days_diff >=3 and today_days_diff  < 30 and self.is__compensatory == False and not self.is_emergency:
            frappe.throw("You have to create leave application in 30 Days advance.")
