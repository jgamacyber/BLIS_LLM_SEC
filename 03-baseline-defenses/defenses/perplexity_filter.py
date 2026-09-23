import math
import torch
from transformers import GPT2LMHeadModel, GPT2TokenizerFast


class PerplexityFilter:
    def __init__(self, threshold: float = 200.0, window_size: int = 10):
        self.threshold = threshold
        self.window_size = window_size
        print("Carregando modelo GPT-2 para perplexidade...")
        self.tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
        self.model.eval()

    def compute_perplexity(self, text: str) -> float:
        inputs = self.tokenizer(text, return_tensors="pt")
        input_ids = inputs["input_ids"]
        with torch.no_grad():
            outputs = self.model(input_ids, labels=input_ids)
            loss = outputs.loss
        return math.exp(loss.item())

    def compute_window_perplexity(self, text: str) -> float:
        tokens = self.tokenizer.encode(text)
        max_ppl = 0.0
        for i in range(0, len(tokens), self.window_size):
            window = tokens[i:i + self.window_size]
            if len(window) < 2:
                continue
            window_text = self.tokenizer.decode(window)
            ppl = self.compute_perplexity(window_text)
            max_ppl = max(max_ppl, ppl)
        return max_ppl

    def is_adversarial(self, prompt: str) -> dict:
        ppl = self.compute_perplexity(prompt)
        win_ppl = self.compute_window_perplexity(prompt)
        return {
            "perplexity": round(ppl, 2),
            "window_perplexity": round(win_ppl, 2),
            "blocked_by_ppl": ppl > self.threshold,
            "blocked_by_window": win_ppl > self.threshold,
            "is_adversarial": ppl > self.threshold or win_ppl > self.threshold,
        }
