import streamlit as st
import generate_response

st.set_page_config(layout="wide", page_title="Prompt Comparison Playground")

st.title("Prompt Comparison Playground")
st.caption("Compare different LLM responses")

with st.container(key="form"):
    prompt = st.text_input("Enter your prompt:", placeholder="Explain Prompt Engineering to me like I'm a 10 year old kid.")

    if not prompt:
        st.warning("Enter a prompt to continue!")

col1, col2 = st.columns(2)

available_llms = ["---", "Google Gemini", "Anthropic Claude", "Meta Llama", "Mistral", "Perplexity Sonar"]

response = ""

with col1:
    with st.container(key='llm1'):
        with st.form(key="form1"):
            st.header("LLM 1:")
            selected_llm_1 = st.selectbox(label="LLM:", options=available_llms, key="llm1_selection")

            temperature_1 = st.slider(label="Temperature:", min_value=0.00, max_value=2.00, step=0.01, value=1.00, key="temp1", help="Controls randomness in the output — higher values make responses more creative.")
            top_p_1 = st.slider(label="Top-p:", min_value=0.00, max_value=1.00, step=0.01, value=1.00, key="top_p1", help="Limits the model to selecting from the top p% of likely words — encourages diversity while staying relevant.")
            max_tokens_1 = st.slider(label="Maximum No. of tokens:", min_value=10, max_value=2000, value=200, step=5, key="max_tokens1", help="Sets the maximum length of the output in tokens (words/subwords).")

            submitted1 = st.form_submit_button("Generate Response")


with col2:
    with st.container(key='llm2'):
        with st.form(key='form2'):
            st.header("LLM 2:")
            selected_llm_2 = st.selectbox(label="LLM:", options=available_llms, key="llm2_selection")

            temperature_2 = st.slider(label="Temperature:", min_value=0.00, max_value=2.00, step=0.01, value=1.00, key="temp2", help="Controls randomness in the output — higher values make responses more creative.")
            top_p_2 = st.slider(label="Top-p:", min_value=0.00, max_value=1.00, step=0.01, value=1.00, key="top_p2", help="Limits the model to selecting from the top p% of likely words — encourages diversity while staying relevant.")
            max_tokens_2 = st.slider(label="Maximum No. of tokens:", min_value=10, max_value=2000, value=200, step=5, key="max_tokens2", help="Sets the maximum length of the output in tokens (words/subwords).")

            submitted2 = st.form_submit_button("Generate Response")

with col1:
    with st.container(key="llm1_response"):
        st.subheader("LLM1 Response:")
        if selected_llm_1 == "---":
            st.warning("Select an LLM to continue!")

        elif selected_llm_1 == "Google Gemini":
            response = generate_response.generate_response_via_gemini(prompt, temperature_1, max_tokens_1, top_p_1)

        elif selected_llm_1 == "Anthropic Claude":
            response = generate_response.generate_response_via_claude(prompt, temperature_1, max_tokens_1, top_p_1)

        elif selected_llm_1 == "Meta Llama":
            response = generate_response.generate_response_via_llama(prompt, temperature_1, max_tokens_1, top_p_1)

        elif selected_llm_1 == "Mistral":
            response = generate_response.generate_response_via_mistral(prompt, temperature_1, max_tokens_1, top_p_1)

        elif selected_llm_1 == "Perplexity Sonar":
            response = generate_response.generate_response_via_sonar(prompt, temperature_1, max_tokens_1, top_p_1)

        else:
            st.error("Error occurred! Please try again!")

        st.markdown(response)

with col2:
    with st.container(key="llm2_response"):
        st.subheader("LLM2 Response:")
        if selected_llm_1 == "---":
            st.warning("Select an LLM to continue!")

        elif selected_llm_2 == "Google Gemini":
            response = generate_response.generate_response_via_gemini(prompt, temperature_2, max_tokens_2, top_p_2)

        elif selected_llm_2 == "Anthropic Claude":
            response = generate_response.generate_response_via_claude(prompt, temperature_2, max_tokens_2, top_p_2)

        elif selected_llm_2 == "Meta Llama":
            response = generate_response.generate_response_via_llama(prompt, temperature_2, max_tokens_2, top_p_2)

        elif selected_llm_2 == "Mistral":
            response = generate_response.generate_response_via_mistral(prompt, temperature_2, max_tokens_2, top_p_2)

        elif selected_llm_2 == "Perplexity Sonar":
            response = generate_response.generate_response_via_sonar(prompt, temperature_2, max_tokens_2, top_p_2)

        else:
            st.error("Error occurred! Please try again!")

        st.markdown(response)