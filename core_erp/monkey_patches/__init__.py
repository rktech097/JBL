from erpnext.selling.doctype.sales_order.sales_order import SalesOrder
from core_erp.core_erp.customization.sales_order.sales_order import get_work_order_items


SalesOrder.get_work_order_items = get_work_order_items
