frappe.ui.form.on('Purchase Invoice', {
// //     refresh(frm){
// //       if(frm.doc.__islocal){
// //        frm.set_value("total_rm_cost_value", parseInt(frm.doc.total) + parseInt(frm.doc._custom_duty) + parseInt(frm.doc.loading_unloading_charges)
// //        + parseInt(frm.doc.stamp_duty) + parseInt(frm.doc.sims_charges) + parseInt(frm.doc.inland_haulage_freight_cost) + parseInt(frm.doc.commission)
// //        + parseInt(frm.doc.custom_clearance_charges) + parseInt(frm.doc.local_freight_cost) + parseInt(frm.doc.detention_demurrage_yard_cahrges))
// //        frm.set_value("landed_price_inr_kg", parseInt(frm.doc.total_rm_cost_value)/parseInt(frm.doc.total_qty))
// //    }},
   cost_center(frm){
//        if (frm.doc.cost_center == "Surajpur J2 - JBL"){
//            frm.set_value("billing_address", "JBL-Surajpur G.Noida-Billing")
//            frm.set_value("shipping_address", "JBL-Surajpur G.Noida-Billing")
//        }
//        if (frm.doc.cost_center == "Noida J1 - JBL"){
//            frm.set_value("billing_address",  "JBL-Noida-Billing")
//            frm.set_value("shipping_address",  "JBL-Noida-Billing")
//        }

//        if (frm.doc.po_type=="General" && frm.doc.cost_center=="Noida J1 - JBL"){
//            frm.set_value("naming_series","PI/GEN/J1/.FY./");
//        }
//        if (frm.doc.po_type=="General" && frm.doc.cost_center=="Surajpur J2 - JBL"){
//            frm.set_value("naming_series","PI/GEN/J2/.FY./");
//        }
//        if (frm.doc.po_type=="Raw Material - Domestic" && frm.doc.cost_center=="Noida J1 - JBL"){
//            frm.set_value("naming_series","PI/RM/J1/.FY./");
//        }
//        if (frm.doc.po_type=="Raw Material - Domestic" && frm.doc.cost_center=="Surajpur J2 - JBL"){
//            frm.set_value("naming_series","PI/RM/J2/.FY./");
//        }
//        if (frm.doc.po_type=="Import" && frm.doc.cost_center=="Surajpur J2 - JBL"){
//            frm.set_value("naming_series","PI/IM/J2/.FY./");
//        }
//        if (frm.doc.po_type=="Import" && frm.doc.cost_center=="Noida J1 - JBL"){
//            frm.set_value("naming_series","PI/IM/J1/.FY./");
//        }
       if (frm.doc.cost_center == "Surajpur J2 - JBL"){
           frm.set_value("billing_address", "JBL-Surajpur G.Noida-Billing")
           frm.set_value("shipping_address", "JBL-Surajpur G.Noida-Billing")
       }
       if (frm.doc.cost_center == "Noida J1 - JBL"){
           frm.set_value("billing_address",  "JBL-Noida-Billing")
           frm.set_value("shipping_address",  "JBL-Noida-Billing")
       }
       
   },
   PI_type(frm){
//        if (frm.doc.po_type=="General" && frm.doc.cost_center=="Noida J1 - JBL"){
//            frm.set_value("naming_series","PI/GEN/J1/.FY./");
//        }
//        if (frm.doc.po_type=="General" && frm.doc.cost_center=="Surajpur J2 - JBL"){
//            frm.set_value("naming_series","PI/GEN/J2/.FY./");
//        }
//        if (frm.doc.po_type=="Raw Material - Domestic" && frm.doc.cost_center=="Noida J1 - JBL"){
//            frm.set_value("naming_series","PI/RM/J1/.FY./");
//        }
//        if (frm.doc.po_type=="Raw Material - Domestic" && frm.doc.cost_center=="Surajpur J2 - JBL"){
//            frm.set_value("naming_series","PI/RM/J2/.FY./");
//        }
//        if (frm.doc.po_type=="Import" && frm.doc.cost_center=="Surajpur J2 - JBL"){
//            frm.set_value("naming_series","PI/IM/J2/.FY./");
//        }
//        if (frm.doc.po_type=="Import" && frm.doc.cost_center=="Noida J1 - JBL"){
//            frm.set_value("naming_series","PI/IM/J1/.FY./");
//        }
   if (frm.doc.po_type == "Import"){
            frm.set_value("currency", "USD")
   }
   },
       
   
})