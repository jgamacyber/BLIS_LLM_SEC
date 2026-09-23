# BLIS SECURITY — Estudos de Segurança em LLM

Reproduções práticas de artigos fundamentais sobre **segurança de modelos de linguagem (LLM)**: ataques de *prompt injection*, ataques adversariais e defesas. Cada pasta é um experimento autocontido, baseado em um paper específico.

> ⚠️ **Aviso de uso.** Este material é **educacional e defensivo**, voltado à pesquisa em segurança de IA. Os ataques aqui reproduzidos servem para entender e mitigar vulnerabilidades. Use apenas em modelos e ambientes próprios ou autorizados.

## Projetos

| Pasta | Tema | Paper de referência |
|-------|------|---------------------|
| [`01-ignore-previous-prompt`](./01-ignore-previous-prompt) | Goal hijacking e prompt leaking (framework PromptInject) | Perez & Ribeiro (2022), *Ignore Previous Prompt: Attack Techniques For Language Models* |
| [`02-agentdojo-injection`](./02-agentdojo-injection) | Ataque e defesa de *prompt injection* em agentes com ferramentas | Debenedetti et al. (2024), *AgentDojo* |
| [`03-baseline-defenses`](./03-baseline-defenses) | Defesas (perplexity filter, paraphrase, retokenization) | Jain et al. (2023), *Baseline Defenses for Adversarial Attacks Against Aligned Language Models* |
| [`04-indirect-prompt-injection`](./04-indirect-prompt-injection) | 7 labs de *indirect prompt injection* em apps integradas | Greshake et al. (2023), *Not What You've Signed Up For* |
| [`05-gcg-adversarial`](./05-gcg-adversarial) | Ataque adversarial GCG (sufixo universal e transferível) | Zou et al. (2023), *Universal and Transferable Adversarial Attacks on Aligned Language Models* |

## Como rodar

Cada projeto tem seu próprio `requirements.txt` e `.env.example`. O padrão é o mesmo:

```bash
cd 01-ignore-previous-prompt          # ou o projeto que quiser

python -m venv venv
source venv/bin/activate               # Linux / macOS
# venv\Scripts\activate                # Windows (PowerShell)

pip install -r requirements.txt

nano .env                   # e edite com sua chave
python 01_goal_hijacking.py            # veja o README de cada pasta
```

## Configuração da API

Os experimentos usam a [OpenRouter](https://openrouter.ai/) como gateway (compatível com o SDK da OpenAI). Copie `.env.example` para `.env` em cada projeto e preencha:

```
OPENROUTER_API_KEY=sua_chave_aqui
```

O modelo padrão usado nos testes foi `openai/gpt-4o-mini` (barato para experimentação de segurança).


## Papers

Os PDFs dos artigos **não** estão incluídos por questão de direitos autorais. As referências completas estão na tabela acima e no README de cada projeto.

## Licença

Ver [`LICENSE`](./LICENSE) (MIT).
