
import streamlit as st
from generator import generate_idea, generate_name

st.title("🚀 Startup Idea Generator")

form = st.form(key="user_settings")
with form:
    industry_input = st.text_input("Industry", key="industry_input")
    generate_button = form.form_submit_button("Generate Idea")
    if generate_button:
        # Assume generate_idea and generate_name functions are defined elsewhere
        startup_idea = generate_idea(industry_input)
        startup_name = generate_name(startup_idea)
        st.markdown("##### " + startup_name)
        st.write(startup_idea)