# # Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and Contributors
# # License: GNU General Public License v3. See license.txt

# import json

# import frappe
# from dateutil.relativedelta import relativedelta
# from frappe import _
# from frappe.model.document import Document
# from frappe.model.mapper import get_mapped_doc
# from frappe.query_builder import Case
# from frappe.query_builder.functions import Sum
# from frappe.utils import (
# 	cint,
# 	date_diff,
# 	flt,
# 	get_datetime,
# 	get_link_to_form,
# 	getdate,
# 	nowdate,
# 	time_diff_in_hours,
# )

# from erpnext.manufacturing.doctype.bom.bom import (
# 	get_bom_item_rate,
# 	get_bom_items_as_dict,
# 	validate_bom_no,
# )
# from erpnext.manufacturing.doctype.manufacturing_settings.manufacturing_settings import (
# 	get_mins_between_operations,
# )
# from erpnext.stock.doctype.batch.batch import make_batch
# from erpnext.stock.doctype.item.item import get_item_defaults, validate_end_of_life
# from erpnext.stock.doctype.serial_no.serial_no import (
# 	auto_make_serial_nos,
# 	clean_serial_no_string,
# 	get_auto_serial_nos,
# 	get_serial_nos,
# )
# from erpnext.stock.stock_balance import get_planned_qty, update_bin_qty
# from erpnext.stock.utils import get_bin, get_latest_stock_qty, validate_warehouse_company
# from erpnext.utilities.transaction_base import validate_uom_is_integer


# def create_job_card(work_order, row, enable_capacity_planning=False, auto_create=False):
# 	doc = frappe.new_doc("Job Card")
# 	doc.update(
# 		{
# 			"work_order": work_order.name,
# 			"operation": row.get("operation"),
# 			"workstation": row.get("workstation"),
# 			"posting_date": nowdate(),
# 			"for_quantity": row.job_card_qty or work_order.get("qty", 0),
# 			"operation_id": row.get("name"),
# 			"bom_no": work_order.bom_no,
# 			"project": work_order.project,
# 			"company": work_order.company,
# 			"sequence_id": row.get("sequence_id"),
# 			"wip_warehouse": work_order.wip_warehouse,
# 			"hour_rate": row.get("hour_rate"),
# 			"serial_no": row.get("serial_no"),
# 		}
# 	)

# 	if work_order.transfer_material_against == "Job Card" and not work_order.skip_transfer:
# 		doc.get_required_items()

# 	if auto_create:
# 		doc.flags.ignore_mandatory = True
# 		if enable_capacity_planning:
# 			doc.schedule_time_logs(row)

# 		doc.insert()
# 		frappe.msgprint(
# 			_("Job card {0} created").format(get_link_to_form("Job Card", doc.name)), alert=True
# 		)

# 	if enable_capacity_planning:
# 		# automatically added scheduling rows shouldn't change status to WIP
# 		doc.db_set("status", "Open")

# 	return doc






