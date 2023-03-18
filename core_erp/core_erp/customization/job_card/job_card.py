import frappe
# from frappe.model.utils import add_child

def validate(self,method=None):
    order = frappe.db.sql(f""" select * from `tabWork Order` where name='{self.work_order}' """,as_dict=1)
    work = frappe.db.sql(f"""select * from `tabWork Order Job` where parent='{self.work_order}' """,as_dict=1)
    # frappe.msgprint(str(work)) 
    operation = frappe.db.sql(f"""select distinct operation from `tabWork Order Operation` where parent='{self.work_order}' """,as_dict=1)
    for i in range(0, len(operation) ):
        if str(operation[i].operation) == 'Cutting':
            for doc in work:
                self.append("cutting_chart", {
                    'stack':doc.stack_per_limb,
                    'l_x_w':'L X W',
                    'planned_pieces': (float(doc.number_of_pieces_per_limb) * 2 * float(order[0].quantity)),
                    'planned_stack': (float(doc.stack_per_limb) * 2 * float(order[0].quantity)),
                    'planned': (float(doc.calculated_qty_a) * float(order[0].quantity))
                })
                
                self.append("cutting_chart_b", {
                    'stack':doc.stack_per_limb,
                    'l_x_w':'L X W',
                    'planned_pieces': (float(doc.number_of_pieces_per_limb) * 2 * float(order[0].quantity)),
                    'planned_stack': (float(doc.stack_per_limb) * float(order[0].quantity)),
                    'planned': (float(doc.calculated_qty_b) * float(order[0].quantity)),
                    'shifting_0':(float(doc.calculated_qty_b) * float(order[0].quantity)) * 5,
                    'shifting_10':(float(doc.calculated_qty_b) * float(order[0].quantity)) * 2/5,
                    'shifting_20':(float(doc.calculated_qty_b) * float(order[0].quantity)) * 2/5
                })
                
                self.append("cutting_chart_c", {
                    'stack':doc.stack_per_limb,
                    'l_x_w':'L X W',
                    'planned_pieces': (float(doc.number_of_pieces_per_limb) * 2 * float(order[0].quantity)),
                    'planned_stack': (float(doc.stack_per_limb) * 2 * float(order[0].quantity)),
                    'planned': (float(doc.calculated_qty_c) * float(order[0].quantity))
                })
                
        elif str(operation[i].operation) == 'Packing':
            for doc in work:
                self.append("jc_packing_a",{
                    "shape" : 'L X W X Shape',
                    "stack_mm" : (float(doc.stack_per_limb) * 2 * float(order[0].quantity)) / float(order[0].quantity),
                    "planned_qty" : (float(doc.calculated_qty_a) * float(order[0].quantity)) / float(order[0].quantity)
                })
                self.append('jc_packing_b',{
                    'shape':'L X W X Shape',
                    'stack_mm': (float(doc.stack_per_limb) * 2 * float(order[0].quantity)) / float(order[0].quantity) / 2,
                    'planned_qty': (float(doc.calculated_qty_b) * float(order[0].quantity)) / float(order[0].quantity)
                })
                self.append('jc_packing_c',{
                    'shape':'L X W X Shape',
                    'stack_mm': (float(doc.stack_per_limb) * 2 * float(order[0].quantity)) / float(order[0].quantity),
                    'planned_qty': (float(doc.calculated_qty_c) * float(order[0].quantity)) / float(order[0].quantity)
                })

                
        
            
        
        