import frappe

def before_save(self, method=None):
    name = ''
    for item in self.accounts:
        if item.party:
            if item.party_type == "Customer":
                name = frappe.db.get_value('Customer', item.party, 'customer_name')
            elif item.party_type == "Supplier":
                name = frappe.db.get_value('Supplier', item.party, 'supplier_name')
            item.party_name = name


