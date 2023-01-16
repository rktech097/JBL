frappe.ui.form.on('Sales Order', {
	tolerance_allowed(frm) {
        if (frm.doc.tolerance_allowed != 0.5 && frm.doc.tolerance_allowed != 1.0 && frm.doc.tolerance_allowed != 1.5
        && frm.doc.tolerance_allowed != 2.0 && frm.doc.tolerance_allowed != 2.5){
            frappe.throw("Please enter a valid Tolerance Allowed")
            //frm.set_value("tolerance_allowed", null)
        }},
    validate(frm){
            $.each(frm.doc.items, function(i ,e){
                if (!e.prevdoc_docname){
                    frappe.throw("You can't create Sales Order directly, Please create Quotation first")
                }
            })
        },
    refresh(frm){
        
    setTimeout(() => {
        frm.remove_custom_button(('Work Order'),('Create')) 
        if(flt(frm.per_delivered, 6) < 100) {
						
			frm.add_custom_button(__('Work Order'), () => make_work_order(frm), __('Create'));
		}	
    })
    	
		}
});
    
    function make_work_order(frm) {
		
		me.frm.call({
		doc:cur_frm.doc,
        method: "get_work_order_items",
        callback: function(r) {
            console.log(r.message)
            if(!r.message) {
                frappe.msgprint({
                    title: __('Work Order not created'),
                    message: __('No Items with Bill of Materials to Manufacture'),
                    indicator: 'orange'
                });
                return;
            }
            else if(!r.message) {
                frappe.msgprint({
                    title: __('Work Order not created'),
                    message: __('Work Order already created for all items with BOM'),
                    indicator: 'orange'
                });
                return;
            } else {
                const fields = [{
                    label: 'Items',
                    fieldtype: 'Table',
                    fieldname: 'items',
                    description: __('Select BOM and Qty for Production'),
                    fields: [{
                        fieldtype: 'Read Only',
                        fieldname: 'item_code',
                        label: __('Item Code'),
                        in_list_view: 1
                    }, {
                        fieldtype: 'Link',
                        fieldname: 'bom',
                        options: 'BOM',
                        reqd: 1,
                        label: __('Select BOM'),
                        in_list_view: 1,
                        get_query: function (doc) {
                            return { filters: { item: doc.item_code } };
                        }
                    }, {
                        fieldtype: 'Float',
                        fieldname: 'pending_qty',
                        reqd: 1,
                        label: __('Qty'),
                        in_list_view: 1
                    }, {
                        fieldtype: 'Data',
                        fieldname: 'sales_order_item',
                        reqd: 1,
                        label: __('Sales Order Item')
                    },{
                        fieldtype: 'Data',
                        fieldname: 'drawing_no',
                        label: __('Drawing No')
                    
                    }],
                    data: r.message,
                    get_data: () => {
                        return r.message
                    }
                }]
                var d = new frappe.ui.Dialog({
                    title: __('Select Items to Manufacture'),
                    fields: fields,
                    primary_action: function() {
                        var data = {items: d.fields_dict.items.grid.get_selected_children()};
                        me.frm.call({
                            method: 'make_work_orders',
                            args: {
                                items: data,
                                company: me.frm.doc.company,
                                sales_order: me.frm.docname,
                                project: me.frm.project,
                                po_no:frm.doc.po_no,
                                po_date:frm.doc.po_date,
                                customer_name:frm.doc.customer_name,
                                sales_inspection:frm.doc.sales_inspection,
                                inspection_details:frm.doc.inspection_details
                                
                            },
                            freeze: true,
                            callback: function(r) {
                                if(r.message) {
                                    frappe.msgprint({
                                        message: __('Work Orders Created: {0}', [r.message.map(function(d) {
                                                return repl('<a href="/app/work-order/%(name)s">%(name)s</a>', {name:d})
                                            }).join(', ')]),
                                        indicator: 'green'
                                    })
                                }
                                d.hide();
                            }
                        });
                    },
                    primary_action_label: __('Create')
                });
                d.show();
            }
        }
    });
}


	




