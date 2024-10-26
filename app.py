import streamlit as st

class Pages_switch():
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/Questions.py", label="Questionnaire")
    st.sidebar.page_link("pages/DashBoard.py", label="Dashboard")
    st.sidebar.page_link("pages/news.py", label="News & Trends")
    st.sidebar.page_link("pages/educational.py", label="Educational")
    st.sidebar.page_link("pages/aboutus.py", label="About us")


# Load and display the logo image (make sure the path is correct)
# logo_image = "images/q.jpeg"  # Replace with your logo's path

# Create a two-column layout
col1, col2 = st.columns([1, 2])  # Adjust the ratio to your liking

# Display the logo in the first column
with col1:
    # st.image(logo_image, width=150)  # Adjust width as necessary

# Display the features in the second column
    with col2:
    # You can leave this empty or add something else if needed
        pass

# Center the title using HTML
st.markdown(
    """
    <h1 style="text-align: center;">Welcome to the Personalized Portfolio Builder</h1>
    <p style="text-align: center;">
    <br>
    This web application is designed to help you build a personalized investment portfolio based on your financial goals, risk tolerance, and investment preferences.
    </p>
    <br>
    """,
    unsafe_allow_html=True
)

# Create boxes for features
feature_titles = [
    "Questionnaire",
    "Dashboard",
    "News & Trends",
    "Educational Resources"
]

feature_descriptions = [
    "Answer a few questions to give us insights into your financial background, goals, and investment style. This forms the basis of your personalized portfolio recommendation.",
    "Visualize your investment portfolio with clear metrics and insights.",
    "Stay updated with the latest news and trends in the stock market.",
    "Access blogs and videos to enhance your financial literacy."
]

# Create a box for each feature
for title, description in zip(feature_titles, feature_descriptions):
    st.markdown(
        f"""
        <div style="border: 1px solid #ddd; border-radius: 5px; padding: 10px; margin-bottom: 10px;">
            <h4>{title}</h4>
            <p>{description}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


st.markdown("""
        <br><br><hr>
        <div style='text-align: center;'>
            Developed by HighOnCode
        </div>
    """, unsafe_allow_html=True)
# Add a footer
st.markdown(
    """
    <div style="text-align: center;">
    <br>
        &copy; 2024 Personalized Portfolio Builder. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True
)
