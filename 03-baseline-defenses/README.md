# 03 — Baseline Defenses

Implementação das defesas baseline contra ataques adversariais em LLMs alinhados, do paper:

> Jain, N. et al. (2023). *Baseline Defenses for Adversarial Attacks Against Aligned Language Models.*

## Defesas implementadas

| Módulo | Defesa | Ideia |
|--------|--------|-------|
| `defenses/perplexity_filter.py` | **Perplexity filter** | Rejeita entradas com perplexidade anormalmente alta (típica de sufixos adversariais tipo GCG) |
| `defenses/paraphrase_defense.py` | **Paraphrase** | Parafraseia a entrada antes de processá-la, quebrando o gatilho adversarial |
| `defenses/retokenization.py` | **Retokenization** | Re-tokeniza o texto (ex.: BPE-dropout) para dissolver o sufixo malicioso |
| `main.py` | Harness | Roda os prompts de teste passando por cada defesa e compara |

## Como rodar

```bash
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                 # preencha OPENROUTER_API_KEY e MODEL

python main.py
```

> Neste projeto o `.env` também define a variável `MODEL` (além da `OPENROUTER_API_KEY`) — veja o `.env.example`.
