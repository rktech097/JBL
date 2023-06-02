import frappe

def permission_query_expense_claim(user):
    if "Permission Manager" in frappe.get_roles(user):
        return
    else:
        return """`tabExpense Claim`.expense_approver = '{user}' or `tabExpense Claim`.owner = '{user}' """.format(user=user)
    
def permission_query_travel_request(user):
    if "Permission Manager" in frappe.get_roles(user):
        return
    else:
        return """`tabTravel Request`.travel_request_approver = '{user}' or `tabTravel Request`.owner = '{user}' """.format(user=user)
    
def permission_query_loan(user):
    if ["Loan Manager","Permission Manager"] in frappe.get_roles(user):
        return
    else:
        return None
    
def permission_query_advance(user):
    if ["Loan Manager","Permission Manager"] in frappe.get_roles(user):
        return
    else:
        return None

def permission_leave_application(user):
    if "Permission Manager" in frappe.get_roles(user):
        return
    else:
        return """`tabLeave Application`.leave_approver = '{user}' or `tabLeave Application`.owner = '{user}' """.format(user=user)
    
