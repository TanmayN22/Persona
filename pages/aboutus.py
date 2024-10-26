import streamlit as st
from PIL import Image  # Make sure to import Image from PIL

# Set the page title and icon
st.set_page_config(page_title="About Us", page_icon=":information_source:")

class Pages_switch():
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/Questions.py", label="Questionnaire")
    st.sidebar.page_link("pages/DashBoard.py", label="Dashboard")
    st.sidebar.page_link("pages/news.py", label="News & Trends")
    st.sidebar.page_link("pages/educational.py", label="Educational")
    st.sidebar.page_link("pages/aboutus.py", label="About us")

# Title of the About Us page
st.title("About Us")

# Brief introduction
st.write("""
    Welcome to the About Us page! We are a dedicated team of financial enthusiasts committed to helping you build a personalized investment portfolio.
    Here are the faces behind our project:
""")

# Team member data
team_members = [
    {
        "name": "Tanmay Nayak",
        "image": "images/tanmay.jpeg",
        "linkedin": "https://www.linkedin.com/in/tanmay-nayak-272532261/",
        "Github": "https://github.com/TanmayN22"
    },
    {
        "name": "Jay Kapadiya",
        "image": "images/jay.jpeg",  
        "linkedin": "https://www.linkedin.com/in/jay-kapadiya-2b9942246?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app",
        "Github": "https://github.com/jaykapadiya2004"
    },
    {
        "name": "Piyush Das",
        "image": "images/piyush2.jpeg",
        "linkedin": "https://www.linkedin.com/in/piyush-das-79a16b203/",
        "Github": "https://github.com/PiyushDas-2004"
    },
    {
        "name": "Jaydev Gupta",
        "image": "images/jaydev.jpeg",
        "linkedin": "https://www.linkedin.com/in/jaydev-gupta-017b04258/",
        "Github": "https://github.com/JaydevGupta22"
    },]

# Display team members
cols = st.columns(4)  # Create 4 columns for team members
for col, member in zip(cols, team_members):
    with col:
        # Open the image using PIL and resize it
        img = Image.open(member["image"]).resize((400,500))  # Resize to 150x150 pixels
        st.image(img)  # Display the resized image
        st.write(f"**{member['name']}**")
        st.markdown(f"[LinkedIn]({member['linkedin']}) | [Github]({member['Github']})")

# Footer
st.markdown("""
    <br><br><hr>
    <div style="text-align: center;">
        &copy; 2024 Personalized Portfolio Builder. All rights reserved.
    </div>
""", unsafe_allow_html=True)
