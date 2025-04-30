from email.policy import default

import streamlit as st

st.set_page_config(layout='wide', page_title='Prompt Playground')
st.title('Prompt Playground')
st.caption("Learn the basics of Prompt Engineering")

col1, col2 = st.columns(2)

with col2:
    with st.container():
        st.write("LLM parameters:")
        st.write("Mess around and see what works for you!")
        with st.form(key='form'):
            prompt = st.text_area('Prompt:', placeholder="Explain Prompt Engineering to me like I'm a 10 year old kid.")
            temperature = st.slider('Temperature:', min_value=0.00, max_value=2.00, step=0.01, value=1.00, help="Controls the 'creativity' of the response")
            top_p = st.slider('Top p:', min_value=0.0, max_value=1.0, step=0.01, help="Controls diversity via nucleus sampling: the model considers the smallest set of words whose cumulative probability is ≥ top_p. Lower values = more focused, higher values = more diverse.")
            max_tokens = st.slider('Max Tokens:', min_value=10, max_value=2500, step=50, value=100, help="The maximum number of tokens (words or word pieces) the model can generate. More tokens = longer responses.")
            frequency_pen = st.slider('Frequency Penalty:', min_value=-2.0, max_value=2.0, step=0.01, help="Penalizes repeated words based on how often they appear. Positive values reduce repetition, encouraging varied vocabulary.")
            presence_pen = st.slider('Presence Penalty:', min_value=-2.0, max_value=2.0, step=0.01, help="Penalizes repeated topics or phrases regardless of frequency. Encourages introducing new concepts.")

            submit_params = st.form_submit_button('Generate', type='primary')

            if submit_params:
                st.session_state['entered_prompt'] = prompt
                st.success("Prompt saved to session state!")

with col1:
    with st.container():
        with st.form(key='llm_selection'):
            st.write("Select an LLM from the list to continue:")
            selected_llm = st.selectbox(
                label="Select an LLM",
                options=[
                    "None selected",
                    "Google Gemini",
                    "Groq (Mixtral)",
                    "Perplexity Labs",
                    "Cohere Command R+",
                    "LLaMA 3 (via Open Source)"
                ]
            )

            submit_llm = st.form_submit_button('Generate', type='primary')

            if submit_llm:
                st.session_state['entered_prompt'] = prompt
                st.session_state['selected_llm'] = selected_llm
                st.success(f"LLM selected: {selected_llm}")