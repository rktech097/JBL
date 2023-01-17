frappe.ui.form.on('Quotation', {
	refresh(frm) {
		frm.set_value("offer_validity",frappe.datetime.add_days(frm.doc.transaction_date, 7))
	},
	 validate:function(frm){
            if (!frm.doc.opportunity){
                frappe.throw("You can't create Quotation directly.\n Please create through Opportunity ")
            }
        }
})