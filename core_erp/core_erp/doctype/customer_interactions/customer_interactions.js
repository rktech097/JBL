// Copyright (c) 2023, Extension Technologies Pvt Ltd and contributors
// For license information, please see license.txt

frappe.ui.form.on('Customer Interactions', {
	validate: function (frm) {
		for(let i=0;i<frm.doc.actual.length;i++){
			let row=frm.doc.actual[i]
			if (row.follow_up_date && i== frm.doc.actual.length-1) {
				let child = frm.add_child('actual')
				child.scheduled_date = row.follow_up_date
				child.action_type = row.follow_up_action_type
				child.appointment_type = row.follow_up_appointment_type
				frm.set_value('date', row.follow_up_date)
			}
			frm.refresh_field('actual')
		};
	}
});



