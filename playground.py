import streamlit as st
from streamlit import session_state

st.set_page_config(layout="wide", page_title="Prompt Comparison Playground")

st.title("Prompt Comparison Playground")
st.caption("Compare different LLM responses")

with st.container(key="form"):
    prompt = st.text_input("Enter your prompt:", placeholder="Explain Prompt Engineering to me like I'm a 10 year old kid.")
    st.session_state['prompt'] = prompt

col1, col2 = st.columns(2)

with col1:
    with st.container(key='llm1'):
        st.header("LLM 1:")

        available_llms_1 = ["None", "Google Gemini", "Anthropic Claude", "Meta Llama", "Mistral"]
        selected_llm_1 = st.selectbox(label="LLM:", options=available_llms_1, key="llm1_selection")
        if selected_llm_1=="None":
            st.warning("You forgot to select an LLM!")
        temperature_1 = st.slider(label="Temperature:", min_value=0.00, max_value=2.00, step=0.01, value=1.00, key="temp1", help="Controls randomness in the output — higher values make responses more creative.")
        top_p_1 = st.slider(label="Top-p:", min_value=0.00, max_value=1.00, step=0.01, value=1.00, key="top_p1", help="Limits the model to selecting from the top p% of likely words — encourages diversity while staying relevant.")
        max_tokens_1 = st.slider(label="Maximum No. of tokens:", min_value=10, max_value=2000, value=200, step=5, key="max_tokens1", help="Sets the maximum length of the output in tokens (words/subwords).")

        # save parameters to session_state for the 1st LLM
        st.session_state['selected_llm_1'] = selected_llm_1
        st.session_state['temperature_1'] = temperature_1
        st.session_state['top_p_1'] = top_p_1
        st.session_state['max_tokens_1'] = max_tokens_1


with col2:
    with st.container(key='llm2'):
        st.header("LLM 2:")

        available_llms_2 = ["None", "Google Gemini", "Anthropic Claude", "Meta Llama", "Mistral"]
        selected_llm_2 = st.selectbox(label="LLM:", options=available_llms_2, key="llm2_selection")
        if selected_llm_2=="None":
            st.warning("You forgot to select an LLM!")

        temperature_2 = st.slider(label="Temperature:", min_value=0.00, max_value=2.00, step=0.01, value=1.00, key="temp2", help="Controls randomness in the output — higher values make responses more creative.")
        top_p_2 = st.slider(label="Top-p:", min_value=0.00, max_value=1.00, step=0.01, value=1.00, key="top_p2", help="Limits the model to selecting from the top p% of likely words — encourages diversity while staying relevant.")
        max_tokens_2 = st.slider(label="Maximum No. of tokens:", min_value=10, max_value=2000, value=200, step=5, key="max_tokens2", help="Sets the maximum length of the output in tokens (words/subwords).")

        # save parameters to session_state for the 2nd LLM
        st.session_state['selected_llm_2'] = selected_llm_2
        st.session_state['temperature_2'] = temperature_2
        st.session_state['top_p_2'] = top_p_2
        st.session_state['max_tokens_2'] = max_tokens_2

st.button("Generate Responses", type="secondary")

with col1:
    with st.container(key="llm1_response"):
        st.subheader(f"{selected_llm_1} Response:")
        st.markdown(st.session_state)

with col2:
    with st.container(key="llm2_response"):
        st.subheader(f"{selected_llm_2} Response:")
        st.markdown(st.session_state)