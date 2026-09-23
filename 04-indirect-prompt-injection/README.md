# 04 — Indirect Prompt Injection (7 Labs)

Sete laboratórios demonstrando *indirect prompt injection* em aplicações integradas a LLMs, baseados em:

> Greshake, K. et al. (2023). *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection.* AISec @ CCS.

A ideia central: o payload malicioso **não** vem do usuário, mas de **dados externos** que o agente consome (uma página web, um e-mail, um documento) e trata como instrução.

## Labs

| Lab | Tema |
|-----|------|
| `lab1_info_gathering.py` | Coleta de informação / reconhecimento |
| `lab2_fraud.py` | Fraude e phishing |
| `lab3_ai_worm.py` | "Verme" de IA que se auto-propaga entre agentes |
| `lab4_remote_controle.py` | Controle remoto do agente |
| `lab5_persistence.py` | Persistência via memória do agente |
| `lab6_manipulated_content.py` | Manipulação do conteúdo entregue ao usuário |
| `lab7_defenses.py` | Defesas: separação dados/instruções e outras mitigações |

- `agent_core.py` — agente simulado com ferramentas (`search`, `read_email`, `send_email`, `read_memory`, `write_memory`, `retrieve_url`) e helpers de saída.
- `run_all_labs.py` — menu interativo para escolher e rodar os labs.

## Como rodar

```bash
python -m venv venv
source venv/bin/activate            # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env                 # preencha OPENROUTER_API_KEY

python run_all_labs.py               # menu com todos os labs
# ou rode um lab isolado, ex.:
python labs/lab1_info_gathering.py
```

> **Nota:** os nomes de alguns módulos importados em `run_all_labs.py` (ex.: `lab2_fraud_phishing`, `lab4_remote_control`) diferem levemente dos nomes de arquivo (`lab2_fraud.py`, `lab4_remote_controle.py`). Se for rodar via `run_all_labs.py`, alinhe os imports aos nomes reais dos arquivos.
