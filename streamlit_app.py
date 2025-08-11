# streamlit_app.py — SniS (Streamlit app version for outside Snowflake)
import streamlit as st
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

st.set_page_config(page_title="Zena's Athleisure Catalog", layout="centered")
st.title("Zena's Amazing Athleisure Catalog")

# --- Create Snowpark session from Streamlit secrets ---
# Expect: [connections.snowflake] in secrets
cfg = dict(st.secrets["connections"]["snowflake"])

current_database = cfg.get("database", "ZENAS_ATHLEISURE_DB")
current_schema = cfg.get("schema", "PRODUCTS")

session = Session.builder.configs({
    **cfg,
    "database": current_database,
    "schema": current_schema,
}).create()

VIEW_FQN = f"{current_database}.{current_schema}.CATALOG_FOR_WEBSITE"

# 1) Options for the select (colors/styles)
options_df = (
    session.table(VIEW_FQN)
    .select(col("COLOR_OR_STYLE"))
    .distinct()
    .sort(col("COLOR_OR_STYLE"))
    .to_pandas()
)

options = options_df["COLOR_OR_STYLE"].dropna().tolist()
if not options:
    st.error("No COLOR_OR_STYLE options found in the view.")
    st.stop()

# 2) Selectbox
choice = st.selectbox("Pick a sweatsuit color or style:", options)

# 3) Fetch the matching row
row_df = (
    session.table(VIEW_FQN)
    .filter(col("COLOR_OR_STYLE") == choice)
    .select("COLOR_OR_STYLE", "PRICE", "FILE_NAME", "FILE_URL", "SIZE_LIST", "UPSELL_PRODUCT_DESC")
    .limit(1)
    .to_pandas()
)

if row_df.empty:
    st.warning("No data found for this selection.")
    st.stop()

row = row_df.iloc[0]

# 4) Display image (if URL exists)
file_url = row.get("FILE_URL")
if file_url:
    st.image(file_url, caption=f"Our warm, comfortable, {row['COLOR_OR_STYLE']} sweatsuit!")

# 5) Display price, sizes, and upsell 
price = row.get("PRICE")
sizes_raw = row.get("SIZE_LIST") or ""
upsell = row.get("UPSELL_PRODUCT_DESC") or ""

st.markdown(f"**Price:** `{price}`")
st.markdown(f"**Sizes Available:** {sizes_raw}")
if upsell:
    st.markdown(upsell)

# Optional: close the session when the script ends
session.close()
