import streamlit as st
from datetime import date

st.set_page_config(page_title="🎂 Arsalan Ali's Birthday 🎈", layout="centered")

# Sidebar with navigation
st.sidebar.title("🎉 Birthday App Menu")
menu = st.sidebar.radio("Choose a section:", ["🎈 Home", "📝 Send Wish", "📸 Birthday Picture", "🎶 Birthday Song"])

if menu == "🎈 Home":
    st.markdown("""
        <h1 style='text-align: center; font-size: 60px; color: #4c076f; text-shadow: 2px 2px #ff8000; '>🎉 Happy Birthday Arsalan Ali 🎂</h1>
        <h2 style='text-align: center; color: #063970;'>From <span style='background-color: yellow; padding: 4px; border-radius: 5px;'>Sumbul Jawed</span></h2>
        <p style='text-align: center; font-size: 24px;'>Celebrating your special day on <span style='color: #FF4500; font-weight: bold;'>31 July</span> with love and prayers!</p>
    """, unsafe_allow_html=True)

    if st.button("🎈 Release Balloons"):
        st.balloons()

elif menu == "📝 Send Wish":
    st.markdown(
    "<h2 style='text-align: left; color: #283593;'>📝 Special Birthday Wish for Arsalan Ali</h2>",
    unsafe_allow_html=True
)
    st.markdown(
    "<h3 style='text-align: left; color: #0277BD;'>🎂 Birthday Wish for Arsalan Ali</h3>",
    unsafe_allow_html=True
)
    st.markdown("""
    🌿 May Allah bless you with **a long, healthy, and happy life**,  
    🌟 Grant you **success in every step you take**,  
    🌸 And make you **a source of joy and pride for your parents** always.

    🤲 **My heartfelt dua for you:**  
     “Ya Allah, keep his in Your protection, grant him barakah in his life, ease every difficulty for him, guide him to serve and respect his parents with love, and grant him success and honor in every field. Ameen.”

    🕊️ *“May your days be bright, your heart always light,*  
    *May faith and kindness guide you day and night,*  
    *May your parents’ prayers keep you strong in every test,*  
    *In Allah’s mercy and love, may you always rest.”* 🌙✨

    🎈 Stay blessed and keep shining! 🌼
    """)

elif menu == "📸 Birthday Picture":
    st.subheader("📸 Birthday Picture for Arsalan Ali")
    st.image("arsalan.jpeg", use_container_width=True)

    st.markdown(
        "<h2 style='text-align: center; color: #800080;'>🎂 Happy Birthday Arsalan 🎈</h2>",
        unsafe_allow_html=True
    )

    st.success("May all your wishes and prayers come true!")
    st.success("Enjoy your special day!")

elif menu == "🎶 Birthday Song":
    st.subheader("🎶 Play a Birthday Song for Arsalan Ali")
    st.video("https://youtu.be/oKQONwcLHtM?si=NYOmnCli9HfZcF8i")
    st.info("Click play to listen to the Happy Birthday song and celebrate!")

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #C2185B; font-size: 16px;'>💌 Your well-wisher <b>Sumbul Jawed</b></p>",
    unsafe_allow_html=True
)

