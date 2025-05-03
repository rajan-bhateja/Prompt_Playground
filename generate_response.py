from google import generativeai as genai
from google.generativeai import GenerationConfig
from google.generativeai import client


def generate_response_via_gemini(prompt, temperature, max_tokens, top_p):
    client = genai.Client(api_key="gemini_api_key")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
        config=GenerationConfig(
            max_output_tokens=max_tokens, temperature=temperature, top_p=top_p)
        )
    return response.text