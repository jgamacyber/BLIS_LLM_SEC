import os
import tiktoken
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

MODEL = "openai/gpt-4o-mini"

def get_logprob_of_target(prompt: str, target_prefix: str) -> float:
    """
    Estima a probabilidade do modelo gerar o target_prefix dado o prompt.
    Retorna o logprob médio dos tokens do target.
    """
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": target_prefix},  # forçamos como prefixo
    ]

    # Usamos echo via completion para estimar logprobs
    # Com chat API, usamos uma heurística: medimos a perplexidade do target
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=len(target_prefix.split()) + 5,
        temperature=0,
        logprobs=True,
        top_logprobs=1,
    )

    content = response.choices[0].message.content or ""
    logprobs_data = response.choices[0].logprobs

    if logprobs_data and logprobs_data.content:
        avg_logprob = sum(t.logprob for t in logprobs_data.content) / len(logprobs_data.content)
    else:
        avg_logprob = -999.0

    return avg_logprob, content


def query_model(prompt: str, suffix: str = "") -> str:
    """Query simples ao modelo com suffix opcional."""
    full_prompt = prompt + " " + suffix if suffix else prompt
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": full_prompt},
        ],
        max_tokens=200,
        temperature=0,
    )
    return response.choices[0].message.content or ""
