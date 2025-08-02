import streamlit as st
import pandas as pd

# Load data
final_report = pd.read_csv('final_data_report.csv')
summary_report = pd.read_csv('Summary_final_report.csv')

# App config
st.set_page_config(page_title="AI Financial Chatbot", page_icon="💹", layout="wide")

# Header
st.markdown("""
    <style>
        .main-title {
            font-size: 40px;
            font-weight: 700;
            color: #4B8BBE;
        }
        .subtitle {
            font-size: 18px;
            color: #666;
        }
        .box-style {
            padding: 20px;
            border-radius: 12px;
            background-color: #F5F5F5;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>💬 AI-Driven Financial Chatbot</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Ask financial queries about Apple, Tesla, or Microsoft for fiscal years 2021-2023</div>", unsafe_allow_html=True)
st.markdown("---")

# Sidebar filters
with st.sidebar:
    st.header("📊 Select Parameters")
    company_input = st.selectbox("Company", ["Apple", "Microsoft", "Tesla"])
    fiscal_year = st.selectbox("Fiscal Year", [2023, 2022, 2021])
    st.markdown("---")
    st.markdown("💡**Try asking:**\n- What is the total revenue?\n- What is the Net Income?\n- What is the revenue growth(%) ?\n- What is the year by year average revenue growth rate(%)?\n")

# Chat UI
st.markdown("### 🔍 Query Input")
user_query = st.text_input("Type your question below:", placeholder="e.g., What is the Net Income?")

# Logic
def financial_chatbot(user_query, company_input, fiscal_year):
    try:
        df = final_report[(final_report['Year'] == fiscal_year) & (final_report['Company'] == company_input)]
        summary = summary_report[summary_report['Company'] == company_input]

        if user_query == "What is the total revenue?":
            return f"**Total Revenue:** ${df['Total Revenue'].values[0]:,.2f}"

        elif user_query == "What is the Net Income?":
            return f"**Net Income:** ${df['Net Income'].values[0]:,.2f}"

        elif user_query == "What is the sum of total assets?":
            return f"**Total Assets:** ${df['Total Assets'].values[0]:,.2f}"

        elif user_query == "What is the sum of total liabilities?":
            return f"**Total Liabilities:** ${df['Total Liabilities'].values[0]:,.2f}"

        elif user_query == "What is cash flow from operating activities?":
            return f"**Cash Flow from Operations:** ${df['Cash Flow from Operating Activities'].values[0]:,.2f}"

        elif user_query == "What is the revenue growth(%) ?":
            return f"**Revenue Growth:** {df['Revenue Growth (%)'].values[0]:.2f}%"

        elif user_query == "What is the net income growth(%) ?":
            return f"**Net Income Growth:** {df['Net Income Growth (%)'].values[0]:.2f}%"

        elif user_query == "What is the assets growth(%) ?":
            return f"**Assets Growth:** {df['Assets Growth (%)'].values[0]:.2f}%"

        elif user_query == "What is the liabilities growth(%) ?":
            return f"**Liabilities Growth:** {df['Liabilities Growth (%)'].values[0]:.2f}%"

        elif user_query == "What is the cash flow from operations growth(%) ?":
            return f"**Cash Flow Ops Growth:** {df['Cash Flow from Operations Growth(%)'].values[0]:.2f}%"

        elif user_query == "What is the year by year average revenue growth rate(%)?":
            return f"**Avg Revenue Growth (2021–2023):** {summary['Revenue Growth (%)'].values[0]:.2f}%"

        elif user_query == "What is the year by year average net income growth rate(%)?":
            return f"**Avg Net Income Growth (2021–2023):** {summary['Net Income Growth (%)'].values[0]:.2f}%"

        elif user_query == "What is the year by year average assets growth rate(%)?":
            return f"**Avg Assets Growth (2021–2023):** {summary['Assets Growth (%)'].values[0]:.2f}%"

        elif user_query == "What is the year by year average liabilities growth rate(%)?":
            return f"**Avg Liabilities Growth (2021–2023):** {summary['Liabilities Growth (%)'].values[0]:.2f}%"

        elif user_query == "What is the year by year average cash flow from operations growth rate(%)?":
            return f"**Avg Cash Flow Ops Growth (2021–2023):** {summary['Cash Flow from Operations Growth(%)'].values[0]:.2f}%"

        else:
            return "❌ Unsupported query. Please try one from the suggestions above."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"

# Output
if user_query:
    with st.container():
        st.markdown("### 💡 Response")
        response = financial_chatbot(user_query, company_input, fiscal_year)
        st.success(response)

# Footer
st.markdown("---")
st.markdown("Developed by Venkat Ramana Guntupalli © • Powered by Streamlit & Pandas")
