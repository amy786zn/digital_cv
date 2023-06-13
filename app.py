from pathlib import Path

import streamlit as st
from PIL import Image

#---PATH SETTINGS---
current_dir = Path("C:/Users/User/Desktop/digital_cv") #Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file="C:/Users/User/Desktop/digital_cv/styles/main.css" #r"C:\Users\User\Desktop\digital_cv\styles\main.css"
resume_file = "C:/Users/User/Desktop/digital_cv/assets/CV - Anisa Mahomed Yusuf.pdf"#r"C:\Users\User\Desktop\digital_cv\assets\CV - Anisa Mahomed Yusuf.pdf"
profile_pic = "C:/Users/User/Desktop/digital_cv/assets/profile-pic (1).png"#r"C:\Users\User\Desktop\digital_cv\assets\profile-pic (1).png"
#linkedin_image =r"C:\Users\User\Desktop\digital_cv\assets\linkedin.png"
#toml_file = r"C:\Users\User\Desktop\digital_cv\.streamlit\config.toml"

#---GENERAL SETTINGS---
title = "Digital CV | Anisa Mahomed Yusuf" "ZA"
icon = "🙌"
Name= "Anisa Mahomed Yusuf"
Description="""
A South African Qualified Chartered Accountant with management and technology experience
"""
email= "anisamahomed@ymail.com"
social_media = "LinkedIn : https://za.linkedin.com/in/anisa-mahomed-yusuf-acca"
projects = {"🏆Sales Dasboard", 
            "🏆 Income and Expense Tracker"}

st.set_page_config(page_title=title, page_icon=icon)

#---LOAD CSS, PDF and PROFILE PIC ---
with open (css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


with open(resume_file, "rb") as pdf_file:
    PDFbyte=pdf_file.read()

profile_pic=Image.open(profile_pic)
#linkedin_image=Image.open(linkedin_image)


#---HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width =230 )

with col2:
    st.title(Name)
    st.write(Description)
    st.download_button(
        label="🗒️ Download Resume",
        data=PDFbyte,
        file_name=resume_file,
        mime="application/octet-stream",
    )
    st.write("📧:", email)
    st.write(social_media)


#---EXPERIENCE & QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write("---")
st.write(""" 
- ✅ 14 years management & leadership experience in the financial services industry & property development and management
- ✅ Experienced auditor in various industries including manufacturing, government bodies, airline and insurance
- ✅ Excellent in time management, report writing, trend analysis, investigating, research, team management & project management
- ✅ Qualified Accountant and member of Association of Chartered Certified Accountants (ACCA)
- ✅ Bachelor of Commerce, Honours, in Accounting
- ✅ Certificate in Business Systems Analysis and Design
- ✅ Completed a Certificate in Computer Science Fundamentals - Python Bootcamp

"""
)

# --- SKILLS---
st.write("#")
st.subheader("Skills")
st.write("---")
st.write("""
- 🧮Preparation & review of Financial Statements
- 🔢Preparation & review of reconciliations
- 🖥️Maintenance of general ledger and other applications/systems, including rollforwards and month end close offs
- ⚖️Preparation & submission of all SARS related returns, such as VAT, tax and dividends
- 🗒️Preparation of finance packs and dashboards
- 👩Recruiting and performance management of team
- 🔮Preparaton of budgets and forecasts



"""
)

st.write("#")
st.subheader("Other Skills")
st.write("---")
st.write("""
- 💻Basic coding in Python and libraries
- 🤖Basic Robotic Process Automation (RPA)
- 📊Data visualization and Dashboards

"""
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("---")

st.write("**Client Services Lead | IQVIA**")
st.write("06/2023 - Present")

st.write("**Manager - Finance Operatons | SA Home Loans Pty Ltd**")
st.write("04/2009 - 05/2023")

st.write("**Finance Manager | CityZone Properties**")
st.write("04/2008 - 01/2009")

st.write("**Financial Accountant | First Rand Bank Limited**")
st.write("12/2007 - 02/2008")

st.write("**Audit Clerk/Supervisor | Nkonki Incorporated**")
st.write("01/2004 - 06/2007")

# --- ACCOMPLISHMENTS AND AWARDS ---
st.write("#")
st.subheader("ACCOMPLISHMENTS AND AWARDS")
st.write("---")
st.write("""
- 🥇Awarded CEO Incentve Trip Award to Ireland - 2011
- 🥇IFA Lethu - Inhouse Management Programme - 2021
- 🥇Amazing Service Awards and Nominations - Quarterly and Monthly
- 🥇Bursary recipient of the Victor Daitz Trust Fund - 2003

"""
)

# --- PROJECTS ---
st.write("#")
st.subheader("PROJECTS")
st.write("---")
st.write("""
- 🏆Assisted with the implementation of a procurement system on Microsoft Dynamics Great Plains
- 🏆Migration of annual financial statements from excel spreadsheets to new system, Accounts Production-One Source
- 🏆Automated preparation of invoices and mailing directly to panel attorneys using VBA
- 🏆Automated intercompany invoicing processing, saving the team +/-3hrs of time spent in preparing manually.
- 🏆Facilitated proof of concept of Robotic Process Automation (RPA) project between team and supplier for the processing of deposits to clients’ accounts.
- 🏆Facilitated XBRL tagging of financial statements between SAHL and the service provider, obtaining quotes, negotiation of prices and discounts.



"""
)

# --- OTHER PROFESSIONAL DEVELOPMENT ---
st.write("#")
st.subheader("OTHER PROFESSIONAL DEVELOPMENT")
st.write("---")
st.write("""
- 💼Freecodecamp - Creating and Querying Databases using Bash Scripting and SQL
- 💼Coursera - Google Data Analytics Professional Certificate
- 💼Coursera - IBM Applied Artificial Intelligence (2020) (understanding & creating of chatbot using IBM Watson Studio)
- 💼Coursera - Prepare, Load and Transform Data using Power BI (Project Based)
- 💼Coursera - Application of Data Analysis for Business using R Programming (Project Based)
- 💼Coursera - SQL for Data Science
- 💼UiPath - Business Analyst Role
- 💼UiPath - RPA Developer Foundation Level
- 💼Teach English as a Foreign Language - Teach TEFL, South Africa
- 💼Knowledge of Applications/Languages:
        - Python
	    - R
        - Power BI
        - Tableau
        - SQL
- 💼Advanced Microsoft Excel (vlookups, power pivots, power query)




"""
)

































