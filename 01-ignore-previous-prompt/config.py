import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # lê o .env para chamar a minha API
 
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),  # pega do .env
    base_url="https://openrouter.ai/api/v1",
)

MODEL = "openai/gpt-4o-mini"  # usei este por ser mais atual; JUL24, para testes de segurança é barato;
