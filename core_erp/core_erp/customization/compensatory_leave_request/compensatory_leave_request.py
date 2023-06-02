import frappe

from frappe.utils import add_days, cint, date_diff, format_date, getdate

from hrms.hr.utils import (
	create_additional_leave_ledger_entry,
	get_holiday_dates_for_employee,
	get_leave_period,
	validate_active_employee,
	validate_dates,
	validate_overlap,
)

def validate(self):
    validate_active_employee(self.employee)
    validate_dates(self, self.work_from_date, self.work_end_date)
    if self.half_day:
        if not self.half_day_date:
            frappe.throw(_("Half Day Date is mandatory"))
        if (
            not getdate(self.work_from_date) <= getdate(self.half_day_date) <= getdate(self.work_end_date)
        ):
            frappe.throw(_("Half Day Date should be in between Work From Date and Work End Date"))
    validate_overlap(self, self.work_from_date, self.work_end_date)
    self.validate_holidays()
    # self.validate_attendance()
    if not self.leave_type:
        frappe.throw(_("Leave Type is madatory"))