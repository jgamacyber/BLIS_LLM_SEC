# 05 — GCG: Ataques Adversariais Universais

Reprodução prática (simplificada) do ataque **GCG (Greedy Coordinate Gradient)** — otimização de um sufixo adversarial universal e transferível — baseada em:

> Zou, A. et al. (2023). *Universal and Transferable Adversarial Attacks on Aligned Language Models.*

## Labs

| Arquivo | Tema |
|---------|------|
| `lab1_basic_gcg.py` | GCG básico em um único prompt |
| `lab2_basic_gcg.py` | GCG universal multi-prompt |
| `lab3_visualization.py` | Visualização Loss × ASR (attack success rate) |
| `lab4_transfer.py` | Transferabilidade do sufixo entre modelos/prompts |
| `lab5_defenses.py` | Defesas contra GCG |

Módulos de apoio:

- `gcg_attack.py` — núcleo do otimizador (inicialização do sufixo, loss = `-logprob` do target, busca gulosa por coordenada). Config principal: `NUM_TOKENS`, `TOP_K`, `BATCH_SIZE`, `MAX_ITERATIONS`.
- `utils.py` — `query_model`, `get_logprob_of_target`, etc.
- `evaluator.py` — avaliação de sucesso.
- `main.py` — runner interativo (usa `rich`) para escolher os labs.
- `results.json`, `results/lab5/result.json` — saídas de execuções.

## Como rodar

```bash
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                 # preencha OPENROUTER_API_KEY

python main.py                       # menu com todos os labs
```

> Esta é uma reprodução **didática**: usa um vocabulário reduzido e otimização por logprob via API, não o gradiente completo sobre pesos do modelo como no paper original.
