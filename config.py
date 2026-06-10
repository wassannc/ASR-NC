FORMS = {
    "1.NF- Register": {
        "form_id": "NF- Register",
        "columns": ["plot_reg-date","plot_reg-block","plot_reg-gp","plot_reg-village","plot_reg-farmer_name","plot_reg-farmer_id","plot_reg-season","plot_reg-crop_model","plot_reg-plot_gps-Latitude","plot_reg-plot_gps-Longitude","plot_reg-main_crop","plot_reg-inter_crops","plot_reg-sowing_date"],
        "column_labels": {"plot_reg-date": "Date","plot_reg-block": "Block","plot_reg-gp": "GP","plot_reg-village": "Village","plot_reg-farmer_name": "Farmer name","plot_reg-farmer_id": "Farmer ID","plot_reg-season": "Season","plot_reg-crop_model": "Crop model","plot_reg-plot_gps-Latitude": "Plot GPS-Lat","plot_reg-plot_gps-Longitude": "Plot GPS-Long","plot_reg-main_crop": "Main crop","plot_reg-inter_crops": "Inter crops followed","plot_reg-sowing_date": "Date of sowing"},
        "block_col": "plot_reg-block"
    },
    "1.1 NF- Activities": {
        "form_id": "NF- Activities",
        "columns": ["Primary_details-date","Primary_details-block","Primary_details-gp","Primary_details-village","Primary_details-farmer_name","Primary_details-plot_ext","crop_activity","Nf_activites-nf_inputs","Nf_activites-Other_nf_input","Nf_activites-Qty_other_nfinput"],
        "column_labels": {"Primary_details-date": "Date","Primary_details-block": "Block","Primary_details-gp": "GP","Primary_details-village": "Village","Primary_details-farmer_name": "Farmer name","Primary_details-plot_ext": "Plot extent-acrs","crop_activity": "Crop activity","Nf_activites-nf_inputs": "NF Inputs applied","Nf_activites-Other_nf_input": "Other NF inputs","Nf_activites-Qty_other_nfinput": "Other NF input-qty"},
        "block_col": "Primary_details-block"
    },
    "2.Bio Resource Centers": {
        "form_id": "BRC_Units",
        "columns": ["SubmissionDate","table_list_pd-block","table_list_pd-brc_unit","table_list_pd-product_name","table_list_pd-brc_sale_date","table_list_pd-dj_sale_farmer","table_list_pd-gender","table_list_pd-sale_village","table_list_sd-sale_qty","table_list_sd-total_income","table_list_cd-crops","table_list_cd-crop_ext"],
        "column_labels": {"SubmissionDate": "Date","table_list_pd-block": "Block","table_list_pd-brc_unit": "BRC unit","table_list_pd-product_name": "Item name","table_list_pd-brc_sale_date": "Date of sale","table_list_pd-dj_sale_farmer": "Farmer/user","table_list_pd-gender": "Gender","table_list_pd-sale_village": "Village","table_list_sd-sale_qty": "Quantity-litrs","table_list_sd-total_income": "Income-rs","table_list_cd-crops": "Crops","table_list_cd-crop_ext": "Extent-acres"},
        "block_col": "table_list_pd-block"
    },
      "3.Livestock": {
        "form_id": "Livestock",
        "columns": ["table_list_df-Month","table_list_df-Monthly_MIS","table_list_df-block","table_list_df-gp","table_list_df-village","table_list_df-livestock_type","table_list_df-Farmer"],
        "column_labels": {"table_list_df-Month": "Month","table_list_df-Monthly_MIS": "Type of service","table_list_df-block": "Block","table_list_df-gp": "GP","table_list_df-village": "Village","table_list_df-livestock_type": "Livestock type","table_list_df-Farmer": "Farmer name"},
        "block_col": "table_list_df-block"
    },
    "4.Intensification of Orchards": {
        "form_id": "Orchards_Intensification",
        "columns": ["SubmissionDate","basic_info-block","basic_info-gp","basic_info-village","basic_info-orchard_type","basic_info-farmer_add","type"],
        "column_labels": {"SubmissionDate": "Date","basic_info-block": "Block","basic_info-gp": "GP","basic_info-village": "Village","basic_info-orchard_type": "Type of orchard","basic_info-farmer_add": "Farmer name","type": "Type"},
        "block_col": "basic_info-block"
    },
    "5.Micro Enterprizes": {
        "form_id": "Micro Enterprizes",
        "columns": ["SubmissionDate","table_list_pd-block","table_list_pd-gp","table_list_pd-village","table_list_pd1-farmer_name","table_list_pd1-processing_hub_tool","table_list_pd1-processing_date","table_list_pd1-processed_for","table_list_pd2-processing_farmer_village","table_list_pd2-processing_farmer","table_list_pd2-processing_qty_kgs","table_list_pd2-rent_amount","table_list_pd3-Data_sub_by"],
        "column_labels": {"SubmissionDate": "Date","table_list_pd-block": "Block","table_list_pd-gp": "GP","table_list_pd-village": "Village","table_list_pd1-farmer_name": "Farmer name","table_list_pd1-processing_hub_tool": "Machine type","table_list_pd1-processing_date": "Date of processing","table_list_pd1-processed_for": "Processed for","table_list_pd2-processing_farmer_village": "Village from","table_list_pd2-processing_farmer": "Processing farmer","table_list_pd2-processing_qty_kgs": "Processed qty-KGs","table_list_pd2-rent_amount": "Rent amount-rs","table_list_pd3-Data_sub_by": "Data entered by"},
        "block_col": "table_list_pd-block"
    },
    "6.Capacity Building": {
        "form_id": "Capacity_building",
        "columns": ["SubmissionDate","CB-info-block","CB-info-gp","CB-info-village","CB-info-cb_type","CB-info-Event_name","CB-info-Event_mode","Cb-info1-theme","Cb-info1-from_date","Cb-info1-to_date","Cb-info1-num_days","Cb-info1-male","Cb-info1-female","Cb-info1-total_members","Cb-info1-Event_place","Cb-info1-Data_sub_by"],
        "column_labels": {"SubmissionDate": "Date","CB-info-block": "Block","CB-info-gp": "GP","CB-info-village": "Village","CB-info-cb_type": "Type of event","CB-info-Event_name": "Name of the event","CB-info-Event_mode": "Which mode conducted","Cb-info1-theme": "Theme","Cb-info1-from_date": "From Date","Cb-info1-to_date": "To Date","Cb-info1-num_days": "No. of Days","Cb-info1-male": "Total male participants","Cb-info1-female": "Total female participants","Cb-info1-total_members": "Total participants","Cb-info1-Event_place": "Place of event","Cb-info1-Data_sub_by": "Data entered by"},
        "block_col": "CB-info-block"
    }
}
