# app.py

import streamlit as st
from PIL import Image

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Bhanu Mori | Portfolio",
    page_icon="👨‍💻",
    layout="wide"
)

# --- HERO SECTION ---
col1, col2 = st.columns([1, 2], gap="medium")

with col1:
    # IMPORTANT: Save your profile picture as 'profile.png' in the same folder as this script.
    try:
        profile_pic = Image.open('profile.png')
        st.image(profile_pic, width=230)
    except FileNotFoundError:
        st.error("Add a 'profile.png' image to your project folder.")

with col2:
    st.title("Mori Bhanu Venkata Gangadararao")
    st.subheader("Versatile Python Developer | Data Analyst")
    
    st.write(
        """
        A highly driven Python Developer with hands-on experience in web development, Data analysis, 
        and a solid understanding of Data Science practices.
        """
    
    
    st.write(f"📧 mbvgr2003@gmail.com | 📞 +917997542876")
    st.markdown(
        """
        [LinkedIn](#) | [GitHub](https://github.com/MBVGR)
        """,
        unsafe_allow_html=True
    )

# --- SKILLS ---
st.write("---")
st.header("Technical Skills")
st.write("##")

st.markdown(
    """
    - **Programming Languages:** Advanced Python, Intermediate java
    - **Full Stack Development:** HTML5, CSS, React.js
    - **Back-End Development:** SQLite, XAMPP
    - **Data Anlysis**,pandas,numpy,matplotlib
    """
)

# --- EXPERIENCE ---
st.write("---")
st.header("Experience")
st.write("##")

# --- NEWLY ADDED EXPERIENCE ---
st.subheader("Software Engineering Job Simulation | Accenture (Forage)")
st.write("**Completed:** July 2025") #
st.write(
    """
    - [cite_start]Completed a virtual work experience program simulating real-world software engineering tasks at Accenture. [cite: 1]
    - [cite_start]Gained practical experience in Agile methodologies, software architecture, programming, security, and testing. [cite: 1]
    """
)


# --- PROJECTS ---
st.write("---")
st.header("My Projects")
st.write("##")

col1, col2 = st.columns(2, gap="medium")

with col1:
    st.subheader("Speech Recognition System")
    st.write(
        """
        - Developed a system to transcribe audio from microphone input and local files using the Google Speech Recognition API.
        - Utilized **Python**, **PyAudio**, and **pydub** libraries for real-time and file-based audio processing.
        - Engineered solutions to overcome challenges like background noise and audio format compatibility.
        """
    )
    st.markdown("[View on GitHub...](#)", unsafe_allow_html=True)

with col2:
    st.subheader("Visakhapatnam Air Quality Dashboard")
    st.write(
        """
        - Built a full-stack web application using **Streamlit** to analyze and visualize air quality data.
        - Processed and cleaned raw data with **Pandas** and created interactive charts with **Matplotlib**.
        - Managed the end-to-end project lifecycle, from development to cloud deployment.
        """
    )
    st.markdown("[View Live App...](#)", unsafe_allow_html=True)

# --- CERTIFICATIONS ---
st.write("---")
st.header("Certifications")
st.write("##")
st.markdown(
    """
    - **Python Essentials** - Cisco
    - **Data Science** - Cisco
    - **Career Essential in Software Development** - Microsoft & LinkedIn
    - **Python Basics, SQL Basics, Java** - Hackerrank
    """
)

# --- EDUCATION ---
st.write("---")
st.header("Education")
st.write("##")
st.subheader("B.Tech | Raghu Engineering College, Visakhapatnam")
st.write("**CGPA:** 8.60 / 10.0 | **Graduating:** 2026")
st.subheader("Diploma | Swarnandra College of Engineering and Technology, Narsapur")
st.write("**CGPA:** 8.00 / 10.0")
st.subheader("High School | Nalanda E.M School, Kadali")
st.write("**GPA:** 10 / 10")
