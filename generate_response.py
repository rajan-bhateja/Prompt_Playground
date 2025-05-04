# gemini
import google.generativeai as genai
from google.generativeai.types import GenerationConfig

def generate_response_via_gemini(prompt, temperature, max_tokens, top_p):
    gemini_api_key = "gemini_api_key"
    genai.configure(api_key=gemini_api_key)
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


# anthropic
import anthropic

def generate_response_via_claude(prompt, temperature, max_tokens, top_p):
    anthropic_api_key = "anthropic_api_key"
    client = anthropic.Anthropic(api_key=anthropic_api_key)

    message = client.messages.create(
        model="claude-2.1",
        max_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p,
        messages=[
            {
                "role":"user",
                "content":[
                    {
                        "type": "text",
                        "text": prompt
                    }
                ]
            }
        ]
    )
    return message.content


# llama
from llama_api_client import LlamaAPIClient

def generate_response_via_llama(prompt, temperature, max_tokens, top_p):
    llama_api_key= ""
    client = LlamaAPIClient(api_key=llama_api_key)

    response = client.chat.completions.create(
        model="Llama-4-Maverick-17B-128E-Instruct-FP8",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_completion_tokens=max_tokens,
        temperature=temperature,
        top_p=top_p
    )
    return response


# mistral
from mistralai import Mistral

def generate_response_via_mistral(prompt, temperature, max_tokens, top_p):
    mistral_api_key = "mistral_api_key"

    client = Mistral(api_key=mistral_api_key)

    chat_response = client.chat.complete(
        model="mistral-large-latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p
    )
    return chat_response.choices[0].message.content


# perplexity
import requests

def generate_response_via_sonar(prompt, temperature, max_tokens, top_p):
    perplexity_api_key = ""
    url = r"https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p
    }
    headers = {
        "Authorization": "Bearer <token>",
        "Content-Type": "application/json"
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return response.text