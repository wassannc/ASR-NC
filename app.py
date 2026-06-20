import streamlit as st
from config import FORMS
from utils import load_data

st.sidebar.title("Menu")

main_section = st.sidebar.radio(
    "Select Section",
    ["MIS-Status", "MIS-Reports", "Dashboard"]
)

if main_section == "MIS-Reports":
    page = st.sidebar.radio(
        "Select Form",
        list(FORMS.keys())
    )
elif main_section == "Dashboard":
    page = "Dashboard"
else:
    page = "MIS-Status"
    
import pandas as pd
if page == "Dashboard":
    import pandas as pd
    import calendar
    st.title("📊 IINF Dashboard 2026-27")
    
    col1, col2 = st.columns(2)
    
    with col1:
        all_blocks = set()

        for form_name, config in FORMS.items():
            df_temp = load_data(config["form_id"])
            col = config.get("block_col")

            if col and col in df_temp.columns:
                all_blocks.update(df_temp[col].dropna().unique())

        all_blocks = sorted(all_blocks)

        selected_block = st.selectbox(
            "Select Block",
            ["All"] + list(all_blocks)
        )
    with col2:
        months = ["All"] + [calendar.month_name[i] for i in range(1, 13)]
        selected_month = st.selectbox(
            "Select Month",
            months
        )
    # Load NF Register
    nf_df = load_data(
        FORMS["1.NF- Register"]["form_id"]
    )
    activity_df = load_data(
        FORMS["1.1 NF- Activities"]["form_id"]
    )

    cb_df = load_data(
        FORMS["6.Capacity Building"]["form_id"]
    )

    brc_df = load_data(
        FORMS["2.Bio Resource Centers"]["form_id"]
    )
    block_col = "plot_reg-block"

    if (
        selected_block != "All"
        and block_col in nf_df.columns
    ):
        nf_df = nf_df[
            nf_df[block_col] == selected_block
        ]
        activity_df = activity_df[
            activity_df["Primary_details-block"]
            == selected_block
        ]
        cb_df = cb_df[
            cb_df["CB-info-block"]
            == selected_block
        ]
        brc_df = brc_df[
            brc_df["table_list_pd-block"]
            == selected_block
        ]
        
    total_farmers = nf_df[
        "plot_reg-farmer_id"
    ].nunique()
    total_area = pd.to_numeric(
        nf_df["plot_reg-area_"],
        errors="coerce"
    ).sum()
    # NF Activities
    pop_farmers = activity_df[
        "Primary_details-farmer_id"
    ].nunique()
    
    # Capacity Building
    total_events = cb_df[
        "CB-info-Event_name"
    ].count()
    
    # Participants
    participants = pd.to_numeric(
        cb_df["Cb-info1-total_members"],
        errors="coerce"
    ).sum()
    # BRC
    brc_units = brc_df[
        "table_list_pd-brc_unit"
    ].nunique()
    
    # Livestock
    livestock_df = load_data(
        FORMS["3.Livestock"]["form_id"]
    )
    vaccinated = pd.to_numeric(
        livestock_df["table_list_sd-stock_vaccinated"],
        errors="coerce"
    ).sum()
    # Micro Enterprise
    me_df = load_data(
        FORMS["5.Micro Enterprizes"]["form_id"]
    )
    rent_income = pd.to_numeric(
        me_df["table_list_pd2-rent_amount"],
        errors="coerce"
    ).sum()
    processing_income = pd.to_numeric(
        me_df[
            "table_list_md-millets_processed_amount_charged_rs"
        ],
        errors="coerce"
    ).sum()
    enterprise_income = rent_income + processing_income
    
    st.subheader("📈 Project Overview")
    col1, col2, col3, col4 = st.columns(4)
    col5, col6, col7, col8 = st.columns(4)
    with col1:
        st.metric(
        "👨‍🌾 Total Farmers Registered",
        total_farmers
    )
    with col2:
        st.metric(
            "🌾 Total Area (Acres)",
            round(total_area, 1)
        )
    with col3:
        st.metric(
            "🌱 POP Farmers",
            pop_farmers
        )
    with col4:
        st.metric(
            "🎓 Trainings",
            total_events
        )
    with col5:
        st.metric(
            "👥 Participants",
            int(participants)
        )
    with col6:
        st.metric(
            "🏢 BRC Units",
            brc_units
        )
    with col7:
        st.metric(
            "💉 Vaccinated",
            int(vaccinated)
        )
    with col8:
        st.metric(
            "💰 Enterprise Income",
            f"₹{enterprise_income:,.0f}"
        )
    
    st.markdown("---")
    st.subheader("🌾 Crop-wise Farmers")
    crop_summary = (
        nf_df.groupby("plot_reg-main_crop")
        .size()
        .reset_index(name="Farmers")
        .sort_values("Farmers", ascending=False)
    )

    st.bar_chart(
        crop_summary.set_index("plot_reg-main_crop")
    )
    st.subheader("📋 Crop Model Summary")
    crop_df = nf_df.copy()
    mask = (
        crop_df["plot_reg-crop_model"].isna() |
        (crop_df["plot_reg-crop_model"] == "")
    )
    crop_df.loc[mask, "crop_model_final"] = (
        crop_df["plot_reg-main_crop"].fillna("")
        + "-"
        + crop_df["plot_reg-crop_type"].fillna("")
    )
    
    crop_df.loc[
        ~mask,
        "crop_model_final"
    ] = crop_df.loc[
        ~mask,
        "plot_reg-crop_model"
    ]
    crop_df["plot_reg-area_"] = pd.to_numeric(
        crop_df["plot_reg-area_"],
        errors="coerce"
    )
    model_summary = (
        crop_df.groupby("crop_model_final")
        .agg(
            Farmers=("plot_reg-farmer_id", "nunique"),
            Area_Acres=("plot_reg-area_", "sum")
        )
        .reset_index()
    )
    model_summary.columns = [
        "Crop Model",
        "Farmers",
        "Area (Acres)"
    ]
    model_summary = model_summary.sort_values(
        "Farmers",
        ascending=False
    )
    st.dataframe(
        model_summary,
        use_container_width=True
    )
    st.markdown("---")
    st.subheader("🎓 Capacity Building Summary")
    cb_summary = (
        cb_df.groupby("CB-info-cb_type")
        .agg(
            Events=("CB-info-Event_name", "count"),
            Participants=("Cb-info1-total_members", "sum")
        )
        .reset_index()
    )

    cb_summary.columns = [
        "Event Type",
        "Events",
        "Participants"
    ]

    st.dataframe(
        cb_summary,
        use_container_width=True
    )

    st.markdown("---")
    st.subheader("🏢 BRC Summary")
    brc_summary = (
        brc_df.groupby("table_list_pd-brc_unit")
        .agg(
            Income=("table_list_sd-total_income", "sum")
        )
        .reset_index()
    )

    brc_summary.columns = [
        "BRC Unit",
        "Income"
    ]

    st.dataframe(
        brc_summary,
        use_container_width=True
    )

    st.markdown("---")
    st.subheader(" Livestock Summary")
    livestock_summary = (
        livestock_df.groupby("table_list_df-livestock_type")
        .agg(
            Vaccinated=("table_list_sd-stock_vaccinated", "sum")
        )
        .reset_index()
    )

    st.dataframe(
        livestock_summary,
        use_container_width=True
    )
    st.markdown("---")
    st.subheader("🏭 Micro Enterprise Summary")
    me_summary = (
        me_df.groupby("table_list_pd1-processing_hub_tool")
        .agg(
            Rent_Income=("table_list_pd2-rent_amount", "sum"),
            Processing_Income=(
                "table_list_md-millets_processed_amount_charged_rs",
                "sum"
            )
        )
        .reset_index()
    )

    st.dataframe(
        me_summary,
        use_container_width=True
    )
    st.stop()
    
if page == "MIS-Status":
    import pandas as pd
    import calendar

    st.title(" MIS Status")

    # ---------------- FILTERS ----------------
    col1, col2 = st.columns(2)

    with col1:
        all_blocks = set()

        for form_name, config in FORMS.items():
            df_temp = load_data(config["form_id"])
            col = config.get("block_col")

            if col and col in df_temp.columns:
                all_blocks.update(df_temp[col].dropna().unique())

        all_blocks = sorted(all_blocks)

        selected_block = st.selectbox(
            "Select Block",
            ["All"] + list(all_blocks)
        )

    with col2:
        months = ["All"] + [calendar.month_name[i] for i in range(1, 13)]
        selected_month = st.selectbox("Select Month", months)

    # ---------------- DATA DISPLAY ----------------
    forms_list = list(FORMS.items())
    cols_per_row = 2

    for i in range(0, len(forms_list), cols_per_row):
        cols = st.columns(cols_per_row)

        for j in range(cols_per_row):
            if i + j >= len(forms_list):
                break

            form_name, config = forms_list[i + j]
            df = load_data(config["form_id"])
            block_col = config.get("block_col")

            # -------- APPLY FILTERS --------

            # Block filter
            if selected_block != "All" and block_col in df.columns:
                df = df[df[block_col] == selected_block]

            # Month filter
            date_cols = ["SubmissionDate", "meta.SubmissionDate"]
            date_col = None

            for col in date_cols:
                if col in df.columns:
                    date_col = col
                    break

            if selected_month != "All" and date_col:
                df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
                month_num = list(calendar.month_name).index(selected_month)
                df = df[df[date_col].dt.month == month_num]

            # -------- UI --------
            with cols[j]:
                st.markdown(f"#### 📦 {form_name}")

                if df.empty:
                    st.write("No data")
                    continue

                st.caption(f"Total: {len(df)}")

                if block_col and block_col in df.columns:
                    grouped = (
                        df.groupby(block_col)
                        .size()
                        .reset_index(name="Count")
                        .sort_values("Count", ascending=False)
                    )

                    grouped.columns = ["Block", "Count"]

                    st.dataframe(grouped, use_container_width=True, height=200)

                else:
                    st.warning(f"{block_col} not found")

elif page in FORMS:
    st.title(f"📥 {page}")

    config = FORMS[page]
    df = load_data(config["form_id"])

    import pandas as pd
    import calendar
    # Filters
    col1, col2 = st.columns(2)
    block_col = config.get("block_col")
    with col1:
        if block_col and block_col in df.columns:
            selected_block = st.selectbox(
                "Select Block",
                ["All"] + sorted(df[block_col].dropna().unique().tolist())
            )
        else:
            selected_block = "All"
    with col2:
        months = ["All"] + [calendar.month_name[i] for i in range(1, 13)]
        selected_month = st.selectbox(
            "Select Month",
            months
        )

    if "plot_reg-crop_model" in df.columns:
        df["plot_reg-crop_model"] = df["plot_reg-crop_model"]
            
        # If Crop Model is None/blank/Others, combine Main Crop + Crop Type
        if (
            "plot_reg-crop_model" in df.columns and
            "plot_reg-main_crop" in df.columns and
            "plot_reg-crop_type" in df.columns
        ):
            mask = (
                (df["plot_reg-crop_model"].isna()) |
                (df["plot_reg-crop_model"] == "") |
                (df["plot_reg-crop_model"] == "None") |
                (df["plot_reg-crop_model"].str.lower().str.contains("others", na=False))
            )
            df.loc[mask, "plot_reg-crop_model"] = (
                df["plot_reg-main_crop"].fillna("") +
                " - " +
                df["plot_reg-crop_type"].fillna("")
            )
    # Apply Block Filter
    if (
        selected_block != "All"
        and block_col
        and block_col in df.columns
    ):
        df = df[df[block_col] == selected_block]
    # Apply Month Filter
    date_cols = ["SubmissionDate", "SubmissionDate"]
    date_col = None
    for col in date_cols:
        if col in df.columns:
            date_col = col
            break
    if selected_month != "All" and date_col:
        df[date_col] = pd.to_datetime(
            df[date_col],
            errors="coerce"
        )
        month_num = list(calendar.month_name).index(
            selected_month
        )
        df = df[
            df[date_col].dt.month == month_num
        ]
    if df.empty:
        st.warning("No data found")
    else:
        # Select only required columns
        columns = config.get("columns", [])
        available_cols = [col for col in columns if col in df.columns]

        df_filtered = df[available_cols]
        column_labels = config.get("column_labels", {})
        df_filtered = df_filtered.rename(columns=column_labels)

        st.dataframe(df_filtered, use_container_width=True)

        # Download button
        st.download_button(
            label="⬇ Download CSV",
            data=df_filtered.to_csv(index=False),
            file_name=f"{page}_report.csv",
            mime="text/csv"
        )
