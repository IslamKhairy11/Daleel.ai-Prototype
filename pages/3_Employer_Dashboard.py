# pages/3_Employer_Dashboard.py (Corrected with Two-Form Structure)
import streamlit as st
from mock_data import get_mock_candidates, get_mock_company
from openai import OpenAI


# --- Initialize session state for company and generated text ---
if 'company_profile' not in st.session_state:
    st.session_state['company_profile'] = get_mock_company()
if 'matches' not in st.session_state:
    st.session_state['matches'] = []
if 'generated_jd' not in st.session_state:
    st.session_state['generated_jd'] = ""

st.title(f"Employer Dashboard: {st.session_state.company_profile['name']}")

tab1, tab2, tab3 = st.tabs(["Hire New Talent", "Active Postings", "Company Profile"])

with tab1:
    st.header("Create a New Hiring Request")
    st.markdown("---")

    # --- FORM 1: GENERATE JOB DESCRIPTION ---
    st.subheader("Step 1: Generate Job Description (Optional)")
    with st.form("jd_generator_form", clear_on_submit=False):
        st.info("Fill in the details below and let our AI co-pilot write a professional job description for you.")
        col1, col2 = st.columns(2)
        with col1:
            position_gen = st.text_input("Position Title", "Senior BIM Architect")
        with col2:
            team_gen = st.selectbox("Assign to Team", options=list(st.session_state.company_profile['teams'].keys()))
        
        jd_text_gen = st.text_area("Enter key responsibilities or notes", "5+ years of Revit experience, strong understanding of construction documentation, collaborative mindset.", height=100)
        
        generate_button = st.form_submit_button("Generate with AI", use_container_width=True)

    if generate_button:
        with st.spinner("Daleel's AI co-pilot is writing..."):
            try:
                client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
                prompt = f"Write a professional job description for a '{position_gen}' at a top engineering firm. The role is for the '{team_gen}' team. Key notes: {jd_text_gen}"
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}]
                )
                # Save the generated JD to session state to pre-fill the next form
                st.session_state.generated_jd = response.choices[0].message.content
                st.success("AI-Generated Job Description:")
            except Exception as e:
                st.error(f"Could not connect to OpenAI. Please ensure your API key is set in st.secrets.")

    # Display the generated JD if it exists
    if st.session_state.generated_jd:
        st.text_area("Generated Job Description", st.session_state.generated_jd, height=250, key="jd_display")

    st.markdown("---")
    
    # --- FORM 2: FIND MATCHES ---
    st.subheader("Step 2: Find Your Top Matches")
    with st.form("match_finder_form"):
        st.info("Confirm the job details and budget, then run our matching engine.")
        # Pre-fill with data from the generator form if available
        final_position = st.text_input("Final Position Title", position_gen if 'position_gen' in locals() else "Senior BIM Architect")
        final_team = st.selectbox("Final Team", options=list(st.session_state.company_profile['teams'].keys()), index=list(st.session_state.company_profile['teams'].keys()).index(team_gen) if 'team_gen' in locals() else 0)
        final_jd = st.text_area("Final Job Requirements", st.session_state.generated_jd or jd_text_gen, height=150)
        
        col3, col4 = st.columns(2)
        with col3:
            budget_min = st.number_input("Salary Budget (Min EGP)", 15000, 100000, 20000, step=1000)
        with col4:
            budget_max = st.number_input("Salary Budget (Max EGP)", 15000, 100000, 35000, step=1000)

        find_matches_button = st.form_submit_button("Find Top 5 Matches", type="primary", use_container_width=True)

    if find_matches_button:
        with st.spinner("Running the Daleel Matching Engine..."):
            # Your existing matching logic here...
            candidates = get_mock_candidates()
            job_requirements = {'team_culture': st.session_state.company_profile['teams'][final_team]['culture'], 'budget': budget_max}
            scored_candidates = []
            for c in candidates:
                tech_score = c['tech_score']
                culture_fit_score = 100 if c['team_fit_preference'] == job_requirements['team_culture'] else 50
                budget_fit_score = 100 if c['salary_expectation'] <= job_requirements['budget'] else 30
                final_score = (0.6 * tech_score) + (0.3 * culture_fit_score) + (0.1 * budget_fit_score)
                scored_candidates.append({'candidate': c, 'score': round(final_score, 2)})
            
            top_5 = sorted(scored_candidates, key=lambda x: x['score'], reverse=True)[:5]
            st.session_state['matches'] = top_5
            st.success("Found your top 5 matches!")
            
    if st.session_state['matches']:
        st.header("Your Top 5 Matches")
        # Your existing match display logic here...
        for match in st.session_state['matches']:
            c = match['candidate']
            with st.expander(f"**{c['name']}** - {c['title']} | **Match Score: {match['score']}%**"):
                st.write(f"**Technical Score:** {c['tech_score']}%")
                st.write(f"**Preferred Culture:** {c['team_fit_preference'].capitalize()}")
                st.write(f"**Salary Expectation:** EGP {c['salary_expectation']:,}")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Schedule Interview", key=f"interview_{c['id']}"):
                        st.toast(f"Interview scheduled with {c['name']}!")
                with col2:
                    if st.button("Make Offer", key=f"offer_{c['id']}"):
                        st.toast(f"Offer extended to {c['name']}!")

with tab2:
    st.write("Active job postings will be listed here.")

with tab3:
    st.header("Manage Company Profile")
    st.text_input("Company Name", st.session_state.company_profile['name'])
    st.subheader("Manage Teams")
    st.json(st.session_state.company_profile['teams'])
