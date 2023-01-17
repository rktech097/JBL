frappe.ui.form.on('Opportunity', {
    onload(frm) {
        frm.set_query('item_code', 'items', () => {
            return {
                filters: {
                    item_group: 'Finished Goods'
                }
            }
        })
        frappe.call({
            method: "frappe.client.get_list",
            args: {
                doctype: "Building Factor Reference Table",
                fields: ['job_weight_kgs', 'job_weight_kg', 'building_factor', 'type_of_order']
            },

            callback: function(r) {
                if (r.message) {
                    $.each(r.message, function(i, row) { // row can be anything, it is merely a name
                        var child_add = frm.add_child("building_factor_items"); // child_add can be anything
                        child_add.job_weight_kgs = row.job_weight_kgs;
                        child_add.job_weight_kg = row.job_weight_kg;
                        child_add.building_factor = row.building_factor;
                        child_add.type_of_order = row.type_of_order;
                    });
                    frm.refresh_fields("building_factor_items");
                }
            }

        })
    },
   
}),
frappe.ui.form.on('Opportunity Item', {
    quantity(frm, cdt, cdn) {
        var d = locals[cdt][cdn];
        if (d.quantity) {
            frappe.model.set_value(cdt, cdn, "qty", d.weight_per_job * d.quantity)
        }
    },
    no_load_losses(frm, cdt, cdn) {
        var d = locals[cdt][cdn];
        $.each(frm.doc.building_factor_items, function(i, e) {
            if (d.weight_per_job > e.job_weight_kgs && d.no_load_losses < e.job_weight_kg) {
                console.log(e.building_factor)
                // frm.set_value("builing_factor", "e.building_factor")
                let bf = e.building_factor;
                console.log(bf)
                let b = (d.no_load_losses / d.weight_per_job / (1 + bf)).toFixed(3)
                frappe.model.set_value(cdt, cdn, "guaranteed_core_losses", b)
            }
        })
    }

})