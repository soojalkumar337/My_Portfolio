import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

st.sidebar.title("Navigation")
st.sidebar.page_link("streamlit_app.py", label="🏠 Home / About Me")
st.sidebar.page_link("pages/projects.py", label="📂 Projects")
st.sidebar.page_link("pages/resume.py", label="📄 Resume")
st.sidebar.page_link("pages/contact.py", label="✉️ Contact")

st.title("👋 Welcome to My Portfolio")

col1, col2 = st.columns(2)

with col1:
    st.image("assets/profile.jpg", width=250)

with col2:
    st.header("Soojal Kumar")
    st.write("Aspiring Data Scientist with skills in Python, ML, EDA, Streamlit, and Data Science.")
    st.write("🎓 Education: BS(Hons) in Information Technology")
    st.write("🛠️ Skills: Microsoft Exel, Python, Streamlit, PowerBI, EDA, Data Preprocessing, Machine Learning")

st.markdown("---")
st.markdown("## 💡 Mission")
st.info("To deliver clean, effective, and professional solutions through code.")
