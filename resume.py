import streamlit as st

st.title("📄 Resume")

with open("resume/Your_Resume.pdf", "rb") as file:
    st.download_button(label="📥 Download My Resume", data=file, file_name="Your_Resume.pdf", mime="application/pdf")

st.markdown("Or preview below:")

st.markdown(
    f'<iframe src="resume/Your_Resume.pdf" width="700" height="800" type="application/pdf"></iframe>',
    unsafe_allow_html=True,
)
