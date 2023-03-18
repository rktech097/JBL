import frappe   
import datetime

def before_save(self, method=None):
    time = self.shift_actual_end
    frappe.db.set_value("Shift Type",self.shift,"last_sync_of_checkin", time+datetime.timedelta(minutes=5))
    
