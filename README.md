# Prompt Comparison Playground

A web-based tool built using Streamlit that allows you to compare responses from different LLMs (Large Language Models) like Google Gemini, Mistral, Claude, LLaMA, and Perplexity Sonar. It supports customizing temperature, top-p, and max tokens for each model to test how different settings impact the output.

## Key Features
* Input a single prompt and generate responses from two LLMs side-by-side.
* Customize temperature, top-p, and max tokens for each LLM.
* Currently working: ✅ Google Gemini & ✅ Mistral
* Supports: Google Gemini, Mistral, Anthropic Claude, Meta LLaMA, and Perplexity Sonar.
* Simple and interactive UI powered by Streamlit.

## Tech Stack
* Frontend - Streamlit
* LLM APIs - Google Gemini, Mistral, Claude, LLaMA, Perplexity
* HTTP Requests - `requests`
* Structure - Modular code with `playground.py` for UI and `generate_response.py` for API handling

## File Structure
📁 prompt-comparison-playground/

├── playground.py             # Main UI

├── generate_response.py      # Backend logic to call different LLM APIs

├── README.md                 # You're here!

## How It Works
1. Launch the Streamlit app in the same directory as the `playground.py` and `generate_response.py` files:

   `streamlit run .\playground.py`
3. Enter a prompt.
4. Select two LLMs from the dropdowns, adjust parameters, if needed.
5. Click **Generate Response** for each model and compare the results.
   
