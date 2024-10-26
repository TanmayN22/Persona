import streamlit as st 
import json
import re
import matplotlib.pyplot as plt
import pandas as pd

# Set the title of the dashboard
st.title("Dashboard 📊")

# Sidebar navigation
class Pages_switch():
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/Questions.py", label="Questionnaire")
    st.sidebar.page_link("pages/DashBoard.py", label="Dashboard")
    st.sidebar.page_link("pages/news.py", label="News & Trends")
    st.sidebar.page_link("pages/educational.py", label="Educational")
    st.sidebar.page_link("pages/aboutus.py", label="About us")

if 'response' in st.session_state:
    try:
        # Extract JSON part of response using regex
        json_text_match = re.search(r'\{.*\}', st.session_state.response, re.DOTALL)
        if json_text_match:
            json_text = json_text_match.group(0)
            cleaned_response = re.sub(r'(\d+)%', r'\1', json_text)
            response_data = json.loads(cleaned_response)
            print(response_data)
            # Extract allocation percentages as floats
            allocation = {
                "Stocks": float(response_data.get("Stocks", 0)),
                "Bonds": float(response_data.get("Bonds", 0)),
                "Crypto": float(response_data.get("Crypto", 0))
            }

            # Create two columns for visualizations
            col1, col2 = st.columns(2)

            # 1. Pie Chart for Allocation
            with col1:
                st.write("### Investment Allocation Pie Chart")
                labels = allocation.keys()
                sizes = allocation.values()
                fig1, ax1 = plt.subplots()
                fig1.patch.set_facecolor('black')  # Set figure background to black
                ax1.set_facecolor('#262730') 
                ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
                ax1.axis('equal')
                for text in ax1.texts:
                    text.set_color('white')
                st.pyplot(fig1)

            # 2. Bar Chart for Allocation
            with col2:
                st.write("### Investment Allocation Breakdown")
                allocation_df = pd.DataFrame(list(allocation.items()), columns=['Investment Type', 'Percentage'])
                st.bar_chart(allocation_df.set_index('Investment Type'))

            # 3. Debt-to-Income Ratio Visualization (if data is available)
            income = float(response_data.get("Income", 0))
            total_debts = float(response_data.get("Total Debts", 0))
            if income > 0:  # Ensure income is non-zero to avoid division errors
                debt_to_income_ratio = (total_debts / income) * 100
                st.write("### Debt-to-Income Ratio")
                st.progress(debt_to_income_ratio / 100)  # Progress bar for ratio

                st.metric("Debt-to-Income Ratio (%)", f"{debt_to_income_ratio:.2f}%")


            current_savings = float(response_data.get("Current Savings", 0))
            savings_goal = float(response_data.get("Savings Goal", 0))
            if savings_goal > 0:
                savings_progress = (current_savings / savings_goal) * 100
                st.write("### Savings Goal Progress")
                st.progress(savings_progress / 100)

                
                st.metric("Savings Progress (%)", f"{savings_progress:.2f}%")


            st.markdown(f"<p style='font-size: 24px; font-weight: bold;'>Savings Strategy:</p> <p style='font-size: 20px;'>{response_data.get('Savings Strategy', 'Not specified')}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 24px; font-weight: bold;'>Debt Management:</p> <p style='font-size: 20px;'>{response_data.get('Debt Management', 'Not specified')}</p>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 24px; font-weight: bold;'>Emergency Fund Allocation:</p> <p style='font-size: 20px;'>{response_data.get('Emergency Fund Allocation', 'Not specified')}</p>", unsafe_allow_html=True)
        else:
            st.error("Could not extract JSON data. Please check the response format.")
    except json.JSONDecodeError:
        st.error("Error decoding JSON response. Please check the output format.")
    except Exception as e:
        st.error(f"An error occurred while processing the response: {e}")
else:
    st.write("Please complete the profile submission on the Questions page first.")
