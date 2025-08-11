# 🥤 Zena's Athleisure Catalog (Streamlit + Snowflake)

An interactive product catalog built with [Streamlit](https://streamlit.io) and powered by [Snowflake Snowpark](https://docs.snowflake.com/en/developer-guide/snowpark/python/index.html).  
This app reads from the Snowflake view `CATALOG_FOR_WEBSITE` to display product details such as **color/style**, **price**, **available sizes**, and **upsell descriptions**.

---

## 🚀 Features

- Dropdown to select a sweatsuit **color/style**
- Displays:
  - Product image (if available)
  - Price
  - Sizes available
  - Upsell product description
- Data loaded directly from a Snowflake view via Snowpark
- Ready to deploy on [Streamlit Community Cloud](https://share.streamlit.io)

---

## 📂 Project Structure

```
.
├── streamlit_app.py       # Main Streamlit application
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 🛠 Requirements

- Python 3.8+
- Snowflake account with access to:
  - Database: `ZENAS_ATHLEISURE_DB`
  - Schema: `PRODUCTS`
  - View: `CATALOG_FOR_WEBSITE`
- [Streamlit](https://streamlit.io)
- [Snowflake Snowpark Python](https://docs.snowflake.com/en/developer-guide/snowpark/python/index.html)

---

## 📦 Installation & Local Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/zenas-athleisure-catalog.git
   cd zenas-athleisure-catalog
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows use venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Streamlit secrets**
   Create a `.streamlit/secrets.toml` file in the project root:

   ```toml
   [connections.snowflake]
   account = "YOUR_FULL_ACCOUNT_ID"   # e.g., ab12345.ap-southeast-2
   user = "YOUR_USERNAME"
   password = "YOUR_PASSWORD"
   role = "SYSADMIN"
   warehouse = "COMPUTE_WH"
   database = "ZENAS_ATHLEISURE_DB"
   schema = "PRODUCTS"
   client_session_keep_alive = true
   ```

5. **Run the app locally**
   ```bash
   streamlit run streamlit_app.py
   ```

---

## ☁ Deploying to Streamlit Community Cloud

1. Push your project to a **public GitHub repository**.
2. Go to [Streamlit Community Cloud](https://share.streamlit.io) and log in.
3. Click **New App** and select your repository and branch.
4. Set the **Main file path** to:
   ```
   streamlit_app.py
   ```
5. Under **Advanced settings**, add your secrets (same content as `.streamlit/secrets.toml`).
6. Click **Deploy**.

---

## 📸 App Preview

*(Add a screenshot here once the app is running locally or in the cloud)*

---

## 📜 License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
