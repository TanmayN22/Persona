import streamlit as st 

class Pages_switch():
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/Questions.py", label="Questionnaire")
    st.sidebar.page_link("pages/DashBoard.py", label="Dashboard")
    st.sidebar.page_link("pages/news.py", label="News & Trends")
    st.sidebar.page_link("pages/educational.py", label="Educational")
    st.sidebar.page_link("pages/aboutus.py", label="About us")


st.title("Educational Resources 🧑🏻‍💻")

# Create tabs for Blogs and YouTube Videos
tab1, tab2 = st.tabs(["Blogs", "YouTube Videos"])

# Sample Blog Data (you can replace these with actual blog data)
blogs = [
    {"title": "Investment Basics", "link": "https://www.stockal.com/blogs/category/investment-blogs-for-beginners", "description": "Learn the fundamentals of investing."},
    {"title": "Advanced Portfolio Management", "link": "https://indiainvestmentgrid.gov.in/blogs", "description": "Advanced strategies for managing your portfolio."},
    {"title": "Understanding Risk Profiles", "link": "https://online.wharton.upenn.edu/blog/investing-blogs-resources-for-beginners/", "description": "How to align investments with your risk tolerance."},
]

# Sample YouTube Video Data (replace with actual video data and thumbnails)
youtube_videos = [
    {"title": "10 Fundamentally Best Stocks To Buy Now at Heavy Discount | Stocks To Buy in Market Crash", "thumbnail": "https://i.ytimg.com/an_webp/D_7Bw6_yx5E/mqdefault_6s.webp?du=3000&sqp=CPqL8bgG&rs=AOn4CLAziQCBpEKXpB8_MIxmXZ0YaTOxRQ", "url": "https://youtu.be/D_7Bw6_yx5E?si=AAkcoiR-aZYLjinW"},
    {"title": "Time to Rebalance Mutual Fund Portfolio in this Market Situation 2024", "thumbnail": "https://i.ytimg.com/an_webp/7s5lRVoNIOg/mqdefault_6s.webp?du=3000&sqp=CND_8LgG&rs=AOn4CLC6KWwJyJ1qZaUHDoKb0mc1g62c3Q", "url": "https://youtu.be/7s5lRVoNIOg?si=wKGP7CNfH3d5knix"},
    {"title": "How to Start Investing in your 20s | CA Rachana Ranade", "thumbnail": "https://i.ytimg.com/an_webp/Xn7KWR9EOGQ/mqdefault_6s.webp?du=3000&sqp=CNSb8bgG&rs=AOn4CLCpNaYEjOlhauAbVsmEr3K-lt3x3w", "url": "https://youtu.be/Xn7KWR9EOGQ?si=eHi-SlgZxm5j9sgN"},
]

# Blog Section
with tab1:
    st.subheader("Blogs")
    for blog in blogs:
        st.markdown(f"### [{blog['title']}]({blog['link']})")
        st.write(blog['description'])
        st.write("---")

# YouTube Video Section
with tab2:
    st.subheader("YouTube Videos")
    for video in youtube_videos:
        # Display thumbnail with clickable link
        st.markdown(f"[![{video['title']}]({video['thumbnail']})]({video['url']})")
        st.markdown(f"**{video['title']}**")
        st.write("---")