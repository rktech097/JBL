frappe.ui.form.on("Purchase Receipt", {
    refresh(frm){
	if (frm.doc.po_type == "Import"){
 		    frm.set_value("currency", "USD")
    }}
})