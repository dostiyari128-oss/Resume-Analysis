from dotenv import load_dotenv
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space as avs
import google.generativeai as genai
import os
import PyPDF2
from PIL import Image

# Load environment variables and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel(model_name='models/gemini-1.5-pro')

# Function to get response from Gemini
def get_gemini_response(input_prompt):
    try:
        response = model.generate_content([input_prompt])
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Function to extract text from PDF
def input_pdf_text(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page in reader.pages:
        text += str(page.extract_text())
    return text.strip()

# Prompt Template
input_prompt = """
As an experienced ATS (Applicant Tracking System), proficient in the technical domain encompassing
Software Engineering, Data Science, Data Analysis, Big Data Engineering, Web Developer, Mobile App
Developer, DevOps Engineer, Machine Learning Engineer, Cybersecurity Analyst, Cloud Solutions Architect,
Database Administrator, Network Engineer, AI Engineer, Systems Analyst, Full Stack Developer, UI/UX
Designer, IT Project Manager, and additional specialized areas, your objective is to meticulously assess
resumes against provided job descriptions. In a fiercely competitive job market, your expertise is crucial
in offering top-notch guidance for resume enhancement. Assign precise matching percentages based on the JD
(Job Description) and meticulously identify any missing keywords with utmost accuracy.

resume: {text}
description: {jd}

I want the response in the following structure:
### ✅ Match Percentage:
% Match

---

### 🔑 Missing Keywords:
- keyword1
- keyword2
- ...

---

### 🧑‍💼 Profile Summary:
A concise and tailored professional summary based on the resume and job description.
"""

# Streamlit App Layout
st.set_page_config(page_title="CareerCraft: ATS Resume Analyzer", layout="wide")
avs(3)

# Section 1: Introduction
col1, col2 = st.columns([3, 2])
with col1:
    st.title("CareerCraft")
    st.header("Navigate the job market with confidence! 🚀")
    st.markdown("""
        <p style='text-align: justify;'>
        <b>CareerCraft</b> is an ATS-Optimized Resume Analyzer—your solution for optimizing
        job applications and accelerating career growth. We provide job seekers with insights into
        their resumes' compatibility with job descriptions. Streamline your job
        applications, enhance your skills, and navigate your career path with confidence.
        </p>
    """, unsafe_allow_html=True)
with col2:
    st.image("images/icon4.png", use_container_width=True)

avs(6)

# Section 2: Offerings
col1, col2 = st.columns([3, 2])
with col2:
    st.header("💼 Wide Range of Offerings")
    offerings = [
        'ATS-Optimized Resume Analysis',
        'Resume Optimization',
        'Skill Enhancement',
        'Career Progression Guidance',
        'Tailored Profile Summaries',
        'Streamlined Application Process',
        'Personalized Recommendations',
        'Efficient Career Navigation'
    ]
    for item in offerings:
        st.write(f"✅ {item}")
with col1:
    img1 = Image.open("images/icon1.png")
    st.image(img1, use_container_width=True)

avs(6)

# Section 3: Resume Upload & Result
st.markdown("<h1 style='text-align:center;'>📤 Embark on Your Career Adventure</h1>", unsafe_allow_html=True)
col1, col2 = st.columns([3, 2])

with col1:
    jd = st.text_area("📄 Paste the Job Description", height=180)
    uploaded_file = st.file_uploader("📎 Upload Your Resume (PDF)", type="pdf", help="Only PDF files supported")

    if st.button("🚀 Submit"):
        if uploaded_file and jd:
            with st.spinner("🔍 Analyzing Resume..."):
                text = input_pdf_text(uploaded_file)
                final_prompt = input_prompt.format(text=text, jd=jd)
                response = get_gemini_response(final_prompt)

            st.success("✅ Analysis Complete!")
            st.markdown("---")
            st.markdown(response, unsafe_allow_html=True)
        else:
            st.warning("⚠️ Please upload a resume and paste the job description.")

with col2:
    img2 = Image.open("images/icon2.png")
    st.image(img2, use_container_width=True)

avs(6)

# Section 4: FAQ
col1, col2 = st.columns([3, 2])
with col2:
    st.markdown("<h1 style='text-align:center;'>❓ FAQ</h1>", unsafe_allow_html=True)
    st.write("**Q1: How does CareerCraft analyze resumes and job descriptions?**")
    st.write("CareerCraft uses advanced Gemini AI to compare your resume with job descriptions, identifying keyword matches and compatibility.")
    avs(2)
    st.write("**Q2: Can CareerCraft suggest improvements for my resume?**")
    st.write("Yes! It provides personalized suggestions for improvement, including missing keywords and alignment strategies.")
    avs(2)
    st.write("**Q3: Is CareerCraft suitable for both entry-level and experienced professionals?**")
    st.write("Absolutely. It offers tailored insights whether you're just starting out or looking for a senior role.")
with col1:
    img3 = Image.open("images/icon3.png")
    st.image(img3, use_container_width=True)

avs(4)
