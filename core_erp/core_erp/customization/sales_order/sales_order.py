import json

import frappe
import frappe.utils
from frappe import _
from frappe.contacts.doctype.address.address import get_company_address
from frappe.desk.notifications import clear_doctype_notifications
from frappe.model.mapper import get_mapped_doc
from frappe.model.utils import get_fetch_values
from frappe.utils import add_days, cint, cstr, flt, get_link_to_form, getdate, nowdate, strip_html

from erpnext.accounts.doctype.sales_invoice.sales_invoice import (
	unlink_inter_company_doc,
	update_linked_doc,
	validate_inter_company_party,
)
from erpnext.accounts.party import get_party_account
from erpnext.controllers.selling_controller import SellingController
from erpnext.manufacturing.doctype.production_plan.production_plan import (
	get_items_for_material_requests,
)
from erpnext.selling.doctype.customer.customer import check_credit_limit
from erpnext.setup.doctype.item_group.item_group import get_item_group_defaults
from erpnext.stock.doctype.item.item import get_item_defaults
from erpnext.stock.get_item_details import get_default_bom
from erpnext.stock.stock_balance import get_reserved_qty, update_bin_qty

form_grid_templates = {"items": "templates/form_grid/item_grid.html"}

@frappe.whitelist()
def make_work_orders(items, sales_order, company,customer_name,po_no,po_date,sales_inspection=None,inspection_details=None, project=None):
	"""Make Work Orders against the given Sales Order for the given `items`"""
	items = json.loads(items).get("items")
	out = []

	for i in items:
		if not i.get("bom"):
			frappe.throw(_("Please select BOM against item {0}").format(i.get("item_code")))
		if not i.get("pending_qty"):
			frappe.throw(_("Please select Qty against item {0}").format(i.get("item_code")))

		work_order = frappe.get_doc(
			dict(
				doctype="Work Order",
				production_item=i["item_code"],
				bom_no=i.get("bom"),
				qty=i["pending_qty"],
				company=company,
				sales_order=sales_order,
				sales_order_item=i["sales_order_item"],
				project=project,
				fg_warehouse=i["warehouse"],
				description=i["description"],
				#added custom fields
				sales_inspection=sales_inspection if sales_inspection else None,
				inspection_details=inspection_details if inspection_details else None,
				customer_name=customer_name,
				po_no=po_no,
				po_date=po_date,
				drawing_no=i["drawing_no"] if i["drawing_no"] else 0,
				job_rating=i["job_rating"] if i["job_rating"] else 0,
				guaranteed_core_losses=i["guaranteed_core_losses"] if i["guaranteed_core_losses"] else 0,
				weight_per_job=i["weight_per_job"] if i["weight_per_job"] else 0,
				quantity=i["quantity"] if i["quantity"] else 0,
				no_load_losses=i["no_load_losses"] if i["no_load_losses"] else 0,
				design_flux_density=i["design_flux_density"] if i["design_flux_density"] else 0,
			)
		).insert()
		work_order.set_work_order_operations()
		work_order.flags.ignore_mandatory = True
		work_order.save()
		out.append(work_order)

	return [p.name for p in out]

@frappe.whitelist()
def get_work_order_items(self, for_raw_material_request=0):
	"""Returns items with BOM that already do not have a linked work order"""
	items = []
	item_codes = [i.item_code for i in self.items]
	product_bundle_parents = [
		pb.new_item_code
		for pb in frappe.get_all(
			"Product Bundle", {"new_item_code": ["in", item_codes]}, ["new_item_code"]
		)
	]

	for table in [self.items, self.packed_items]:
		for i in table:
			bom = get_default_bom(i.item_code)
			stock_qty = i.qty if i.doctype == "Packed Item" else i.stock_qty

			if not for_raw_material_request:
				total_work_order_qty = flt(
					frappe.db.sql(
						"""select sum(qty) from `tabWork Order`
					where production_item=%s and sales_order=%s and sales_order_item = %s and docstatus<2""",
						(i.item_code, self.name, i.name),
					)[0][0]
				)
				pending_qty = stock_qty - total_work_order_qty
			else:
				pending_qty = stock_qty

			if pending_qty and i.item_code not in product_bundle_parents:
				items.append(
					dict(
						name=i.name,
						item_code=i.item_code,
						description=i.description,
						bom=bom or "",
						warehouse=i.warehouse,
						pending_qty=pending_qty,
						required_qty=pending_qty if for_raw_material_request else 0,
						sales_order_item=i.name,
						drawing_no=i.drawing_no,
						job_rating=i.job_rating,
						guaranteed_core_losses=i.guaranteed_core_losses,
						weight_per_job=i.weight_per_job,
						quantity=i.quantity,
						no_load_losses=i.no_load_losses,
						design_flux_density=i.design_flux_density,
					)
				)

	return items


