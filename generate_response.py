import google.generativeai as genai
from google.generativeai.types import GenerationConfig

genai.configure(api_key="gemini_api_key")

def generate_response_via_gemini(prompt, temperature, max_tokens, top_p):
    model = genai.GenerativeModel("gemini-2.0-flash")

    generation_config = GenerationConfig(
        temperature=temperature,
        max_output_tokens=max_tokens,
        top_p=top_p
    )

    response = model.generate_content(
        prompt, generation_config=generation_config
    )
    return response.text