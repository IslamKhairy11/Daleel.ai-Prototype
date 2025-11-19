# pages/2_🧑‍💻_Talent_Dashboard.py
import streamlit as st
from streamlit_option_menu import option_menu
import pypdf
import io


with st.sidebar:
    st.title(f"Welcome, Islam!")

st.title(f"Welcome, Islam!")
st.header("Your Career Digital Twin")

# --- Initialize session state for twin data ---
if 'digital_twin' not in st.session_state:
    st.session_state['digital_twin'] = {
        'resume_text': '',
        'linkedin_data': '',
        'assessments': {'tech': None, 'culture': None},
        'experience_feedback': []
    }

# --- Navigation Menu ---
selected = option_menu(
    menu_title=None,
    options=["Build Your Twin", "My Profile", "Assessments"],
    icons=["tools", "person-badge", "clipboard-check"],
    orientation="horizontal",
)

# --- Tab 1: Build Your Twin ---
if selected == "Build Your Twin":
    st.subheader("Step 1: Upload Your Resume")
    uploaded_file = st.file_uploader("Upload your CV (PDF)", type="pdf")
    if uploaded_file:
        try:
            pdf_reader = pypdf.PdfReader(io.BytesIO(uploaded_file.getvalue()))
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            st.session_state.digital_twin['resume_text'] = text
            st.success("Resume parsed successfully!")
            with st.expander("See Extracted Text"):
                st.text_area("", text, height=200)
        except Exception as e:
            st.error(f"Error parsing PDF: {e}")

    st.subheader("Step 2: Connect Your LinkedIn Profile")
    linkedin_url = st.text_input("Enter your LinkedIn Profile URL")
    if st.button("Scrape & Analyze Profile (Simulated)"):
        with st.spinner("Analyzing profile... This is a simulation."):
            # SIMULATION: In reality, this is a complex scraping and NLP task.
            # Here, we just pretend it worked and add mock data.
            st.session_state.digital_twin['linkedin_data'] = {
                "summary": "Experienced BIM Specialist with a passion for construction technology.",
                "skills": ["BIM", "Revit", "AutoCAD", "Navisworks", "Project Management"]
            }
            st.success("LinkedIn profile analyzed!")
            st.write("Discovered Skills:", ", ".join(st.session_state.digital_twin['linkedin_data']['skills']))

    st.subheader("Step 3: Rate Past Experiences")
    st.write("This data helps our AI understand what kind of environment you thrive in.")
    # In a real app, this would come from the parsed resume/LinkedIn
    mock_past_jobs = ["Hassan Allam Holding", "Egyptian Engineering Company"]
    for i, job in enumerate(mock_past_jobs):
        st.markdown(f"--- \n **{job}**")
        satisfaction = st.slider(f"Your satisfaction at {job}", 1, 5, 3, key=f"sat_{i}")
        reason = st.text_area(f"What were the main reasons for this rating?", key=f"res_{i}")
        # We would save this data properly
    
    st.info("Go to the 'Assessments' tab to complete your Digital Twin.")


# --- Tab 2: My Profile ---
if selected == "My Profile":
    st.subheader("Your Current Digital Twin Snapshot")
    st.write("**Resume Data:**", "✅ Loaded" if st.session_state.digital_twin['resume_text'] else "❌ Missing")
    st.write("**LinkedIn Analysis:**", "✅ Complete" if st.session_state.digital_twin['linkedin_data'] else "❌ Missing")
    st.write("**Technical Assessment:**", f"{st.session_state.digital_twin['assessments']['tech']}%" if st.session_state.digital_twin['assessments']['tech'] else "❌ Pending")
    st.write("**Cultural Assessment:**", "✅ Complete" if st.session_state.digital_twin['assessments']['culture'] else "❌ Pending")
    if all(st.session_state.digital_twin.values()):
        st.success("Your Digital Twin is 100% complete and active!")
    else:
        st.warning("Your profile is incomplete. Complete all steps to be matched with opportunities.")

# --- Tab 3: Assessments ---
if selected == "Assessments":
    st.subheader("Complete Your Assessments")
    
    st.markdown("#### Technical Assessment (Simulated)")
    st.info("In a real scenario, you would be given a link to a take-home Revit project with instructions.")
    if st.button("Take Revit Test Now"):
        with st.spinner("Grading your submission..."):
            import time, random
            time.sleep(2)
            score = random.randint(85, 98)
            st.session_state.digital_twin['assessments']['tech'] = score
            st.success(f"Assessment Complete! Your Technical Score: {score}%")

    st.markdown("#### Cultural Assessment")
    st.write("Answer these questions to help us find the perfect team fit for you.")
    q1 = st.radio("I prefer to work in a:", ("Fast-paced, agile environment", "Steady, structured environment"))
    q2 = st.radio("When facing a challenge, I:", ("Prefer to collaborate with a team", "Prefer to solve it independently first"))
    if st.button("Submit Cultural Assessment"):
        st.session_state.digital_twin['assessments']['culture'] = {"pace": q1, "style": q2}
        st.success("Cultural profile saved!")
