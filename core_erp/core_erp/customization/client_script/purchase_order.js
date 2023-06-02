frappe.ui.form.on('Purchase Order', {
	validate(frm) {
		if (frm.doc.po_type == "General" && frm.doc.cost_center == "Noida J1 - JBL") {
			frm.set_value("naming_series", "PO/GEN/J1/.FY./");
		}
		if (frm.doc.po_type == "General" && frm.doc.cost_center == "Surajpur J2 - JBL") {
			frm.set_value("naming_series", "PO/GEN/J2/.FY./");
		}
		if (frm.doc.po_type == "Raw Material - Domestic" && frm.doc.cost_center == "Noida J1 - JBL") {
			frm.set_value("naming_series", "PO/RM/J1/.FY./");
		}
		if (frm.doc.po_type == "Raw Material - Domestic" && frm.doc.cost_center == "Surajpur J2 - JBL") {
			frm.set_value("naming_series", "PO/RM/J2/.FY./");
		}
		if (frm.doc.po_type == "Import" && frm.doc.cost_center == "Surajpur J2 - JBL") {
			frm.set_value("naming_series", "PO/IM/J2/.FY./");
		}
		if (frm.doc.po_type == "Import" && frm.doc.cost_center == "Noida J1 - JBL") {
			frm.set_value("naming_series", "PO/IM/J1/.FY./");
		}},
	cost_center(frm){
		if (frm.doc.cost_center == "Surajpur J2 - JBL") {
			frm.set_value("billing_address", "JBL-Surajpur G.Noida-Billing")
			frm.set_value("shipping_address", "JBL-Surajpur G.Noida-Billing")
		}
		if (frm.doc.cost_center == "Noida J1 - JBL") {
			frm.set_value("billing_address", "JBL-Noida-Billing")
			frm.set_value("shipping_address", "JBL-Noida-Billing")
		}

	},
	po_type(frm) {
		if (frm.doc.po_type == "General" && frm.doc.cost_center == "Noida J1 - JBL") {
			frm.set_value("naming_series", "PO/GEN/J1/.FY./");
		}
		if (frm.doc.po_type == "General" && frm.doc.cost_center == "Surajpur J2 - JBL") {
			frm.set_value("naming_series", "PO/GEN/J2/.FY./");
		}
		if (frm.doc.po_type == "Raw Material - Domestic" && frm.doc.cost_center == "Noida J1 - JBL") {
			frm.set_value("naming_series", "PO/RM/J1/.FY./");
		}
		if (frm.doc.po_type == "Raw Material - Domestic" && frm.doc.cost_center == "Surajpur J2 - JBL") {
			frm.set_value("naming_series", "PO/RM/J2/.FY./");
		}
		if (frm.doc.po_type == "Import" && frm.doc.cost_center == "Surajpur J2 - JBL") {
			frm.set_value("naming_series", "PO/IM/J2/.FY./");
		}
		if (frm.doc.po_type == "Import" && frm.doc.cost_center == "Noida J1 - JBL") {
			frm.set_value("naming_series", "PO/IM/J1/.FY./");
		}
		if (frm.doc.po_type == "Import") {
			frm.set_value("currency", "USD")
		}
	},
	onload_post_render(frm) {
		frm.fields_dict['items'].grid.get_field('item_code').get_query = function (doc, cdt, cdn) {
			var child = locals[cdt][cdn];
			return { filters: [['Item', 'item_subtype', '=', frm.doc.po_subtype]] }
		}
	}


})
