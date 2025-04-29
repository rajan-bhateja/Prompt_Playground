from email.policy import default

import streamlit as st

st.set_page_config(layout='wide', page_title='Prompt Playground')
st.title('Prompt Playground')
st.caption("Learn the basics of Prompt Engineering")

col1, col2 = st.columns(2)

with col1:
    with st.container():
        with st.form(key='form'):
            prompt = st.text_area('Prompt:', placeholder="Explain Prompt Engineering to me like I'm a 10 year old kid.")
            temperature = st.slider('Temperature:', min_value=0.00, max_value=2.00, step=0.01, value=1.00, help="Controls the 'creativity' of the response")
            top_p = st.slider('Top p:', min_value=1, max_value=10, step=1)
            max_tokens = st.slider('Max Tokens:', min_value=10, max_value=2500, step=50, value=100)
            frequency_pen = st.slider('Frequency Penalty:', min_value=-2.0, max_value=2.0, step=0.01)
            presence_pen = st.slider('Presence Penalty:', min_value=-2.0, max_value=2.0, step=0.01)

            submit = st.form_submit_button('Generate', type='primary')

print(dir(st.sidebar()))