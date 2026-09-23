import random
from transformers import GPT2TokenizerFast


class RetokenizationDefense:
    def __init__(self, dropout_rate: float = 0.4):
        self.dropout_rate = dropout_rate
        self.tokenizer = GPT2TokenizerFast.from_pretrained("gpt2")

    def apply_bpe_dropout(self, text: str) -> str:
        tokens = self.tokenizer.tokenize(text)
        result_tokens = []
        for token in tokens:
            clean = token.replace("Ġ", "").replace("Ċ", "")
            if not clean:
                continue
            if random.random() < self.dropout_rate and len(clean) > 2:
                split_point = random.randint(1, len(clean) - 1)
                result_tokens.append(clean[:split_point])
                result_tokens.append(clean[split_point:])
            else:
                result_tokens.append(clean)
        return " ".join(result_tokens)

    def defend(self, prompt: str) -> dict:
        retokenized = self.apply_bpe_dropout(prompt)
        return {
            "original_prompt": prompt,
            "retokenized_prompt": retokenized,
            "dropout_rate": self.dropout_rate,
        }
