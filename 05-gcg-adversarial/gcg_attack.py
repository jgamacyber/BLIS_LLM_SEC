import random
import string
import numpy as np
from utils import get_logprob_of_target, query_model

# ── Configurações do GCG ──────────────────────────────────────────────────────
NUM_TOKENS = 10          # tamanho do suffix adversarial
TOP_K = 20               # candidatos por posição
BATCH_SIZE = 16          # avaliações por iteração
MAX_ITERATIONS = 30      # steps de otimização

# Vocabulário simplificado (tokens como palavras)
VOCAB = list(string.ascii_lowercase.split() + [
    "the", "a", "is", "to", "of", "and", "in", "that", "it", "was",
    "for", "on", "are", "as", "with", "his", "they", "at", "be", "this",
    "from", "or", "an", "but", "not", "what", "all", "were", "we", "when",
    "your", "can", "said", "there", "use", "each", "which", "she", "do",
    "how", "their", "if", "will", "up", "other", "about", "out", "many",
    "then", "them", "so", "some", "her", "would", "make", "like", "him",
    "into", "time", "has", "look", "two", "more", "write", "go", "see",
    "number", "no", "way", "could", "people", "my", "than", "first",
    "been", "call", "who", "find", "long", "down", "day", "did", "get",
    "come", "made", "may", "part", "sure", "here", "please", "answer",
    "tell", "explain", "describe", "show", "help", "provide", "give",
])

def initialize_suffix(n_tokens: int) -> list[str]:
    """Inicializa suffix com tokens aleatórios."""
    return [random.choice(VOCAB) for _ in range(n_tokens)]

def compute_loss(prompt: str, suffix: list[str], target: str) -> float:
    """
    Loss = negativo do logprob médio do target dado (prompt + suffix).
    Quanto menor, melhor o suffix.
    """
    suffix_str = " ".join(suffix)
    full_prompt = f"{prompt} {suffix_str}"
    logprob, _ = get_logprob_of_target(full_prompt, target)
    return -logprob  # minimizamos a loss (= maximizamos logprob)

def gcg_step(prompt: str, suffix: list[str], target: str) -> tuple[list[str], float]:
    """
    Um step do GCG:
    1. Para cada posição i do suffix, gera TOP_K candidatos aleatórios
    2. Amostras BATCH_SIZE substituições
    3. Seleciona a que minimiza a loss
    """
    best_suffix = suffix.copy()
    best_loss = compute_loss(prompt, suffix, target)

    # Gera candidatos: (posição, novo_token)
    candidates = []
    for i in range(len(suffix)):
        tokens = random.sample(VOCAB, min(TOP_K, len(VOCAB)))
        for tok in tokens:
            candidates.append((i, tok))

    # Amostra BATCH_SIZE candidatos
    sampled = random.sample(candidates, min(BATCH_SIZE, len(candidates)))

    for (pos, new_tok) in sampled:
        candidate = suffix.copy()
        candidate[pos] = new_tok
        loss = compute_loss(prompt, candidate, target)

        if loss < best_loss:
            best_loss = loss
            best_suffix = candidate.copy()

    return best_suffix, best_loss


def run_gcg(prompt: str, target: str) -> dict:
    """
    Executa o loop completo do GCG.
    
    Args:
        prompt: instrução original do usuário
        target: prefixo que queremos que o modelo gere (ex: "Sure, here is")
    
    Returns:
        dict com suffix otimizado, loss final e histórico
    """
    print(f"\n{'='*60}")
    print(f"[GCG] Prompt: {prompt}")
    print(f"[GCG] Target: {target}")
    print(f"{'='*60}\n")

    suffix = initialize_suffix(NUM_TOKENS)
    history = []

    for step in range(MAX_ITERATIONS):
        suffix, loss = gcg_step(prompt, suffix, target)
        suffix_str = " ".join(suffix)

        print(f"Step {step+1:02d}/{MAX_ITERATIONS} | Loss: {loss:.4f} | Suffix: {suffix_str}")
        history.append({"step": step + 1, "loss": loss, "suffix": suffix_str})

    # Avalia resultado final
    suffix_str = " ".join(suffix)
    _, final_response = get_logprob_of_target(
        f"{prompt} {suffix_str}", target
    )

    return {
        "original_prompt": prompt,
        "target": target,
        "optimized_suffix": suffix_str,
        "final_loss": loss,
        "history": history,
        "model_response": final_response,
    }
