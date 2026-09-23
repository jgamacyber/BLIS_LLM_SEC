# defenses/paraphrase_defense.py
import os
from openai import OpenAI
from dotenv import load_dotenv

# Força o caminho absoluto do .env
import pathlib
env_path = pathlib.Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)


class ParaphraseDefense:
    def __init__(self):
        api_key = os.getenv("OPENROUTER_API_KEY")
        model = os.getenv("MODEL")

        # Debug — remova após confirmar funcionamento
        print(f"   [DEBUG] API Key carregada: {'SIM' if api_key else 'NÃO'}")
        print(f"   [DEBUG] Model carregado: {model}")

        if not api_key:
            raise ValueError("OPENROUTER_API_KEY não encontrada no .env")
        if not model:
            raise ValueError("MODEL não encontrado no .env")

        self.model = model
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
            default_headers={
                "HTTP-Referer": "http://localhost",
                "X-Title": "BLIS-SECURITY",
            }
        )

    def paraphrase(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a text paraphrasing assistant. "
                        "Paraphrase the user's text preserving its meaning. "
                        "Return ONLY the paraphrased text, nothing else."
                    )
                },
                {
                    "role": "user",
                    "content": f"Paraphrase the following sentence:\n\n{prompt}"
                }
            ],
            temperature=0.7,
            max_tokens=200,
        )
        return response.choices[0].message.content.strip()

    def defend(self, prompt: str) -> dict:
        paraphrased = self.paraphrase(prompt)
        return {
            "original_prompt": prompt,
            "paraphrased_prompt": paraphrased,
        }
