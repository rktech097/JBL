frappe.ui.form.on('Item', {
	onload(frm) {
		cur_frm.set_query("item_subgroup", function () {
			return {

				filters: [
					["Subgroup Master", "parent_group", "=", cur_frm.doc.item_group]
				]
			};
		});
	},
});



