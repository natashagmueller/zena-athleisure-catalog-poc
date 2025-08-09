# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(f"Nat's Amazing Athleisure Catalog Prototype")

cnx = st.connection("snowflake")
session = cnx.session()

# In Snowflake, FQN stands for Fully Qualified Name  - df stands for dataframe
VIEW_FQN = "ZENAS_ATHLEISURE_DB.PRODUCTS.CATALOG_FOR_WEBSITE"

    # 1) Options for the select (colors/styles) - df stands for dataframe
options_df = (
    session.table(VIEW_FQN)
    .select(col("COLOR_OR_STYLE"))
    .distinct()
    .sort(col("COLOR_OR_STYLE"))
    .to_pandas()
)

# In Pandas, .dropna() removes any missing values (NaN = “Not a Number”) from a DataFrame or Series.
options = options_df["COLOR_OR_STYLE"].dropna().tolist()
if not options:
    st.error("No otion found in COLOR_OR_STYLE.")
    st.stop()

# 2) Selectbox
chosen_colourorstyle = st.selectbox("Pick a sweatsuit color or style:", options)

# 3) Search the corresponding record based on the color/style chosen
row_df = (
    session.table(VIEW_FQN)
    .filter(col("COLOR_OR_STYLE") == chosen_colourorstyle)
    .select("COLOR_OR_STYLE", "PRICE", "FILE_NAME", "FILE_URL", "SIZE_LIST", "UPSELL_PRODUCT_DESC")
    .limit(1)
    .to_pandas()
)

if row_df.empty:
    st.warning("Couldn't find data for this option.")
    st.stop()

# taking the first row from row_df and storing it in the variable row.
row = row_df.iloc[0]

# 4) Show image (if URL available)
if row.get("FILE_URL"):
    st.image(row["FILE_URL"], caption=f"Our warm, comfortable, {row['COLOR_OR_STYLE']} sweatsuit!")

# 5) Show price, sizes, and upsell
price = row.get("PRICE")
sizes_list = row.get("SIZE_LIST") or ""
upsell = row.get("UPSELL_PRODUCT_DESC") or ""

st.markdown(f"**Price:**  `{price:.2f}`" if price is not None else "**Price:**  N/A")
st.markdown(f"**Sizes Available:** {sizes_list}")
if upsell:
    st.markdown(f"**BONUS:** {upsell}")
