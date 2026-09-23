"""
BLIS SECURITY — GCG Attack Labs Runner
"""
import json
import importlib
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

LABS = {
    "1": ("LAB 1 — GCG Básico (Single Prompt)",          "lab1_basic_gcg"),
    "2": ("LAB 2 — GCG Universal Multi-Prompt",          "lab2_multi_prompt"),
    "3": ("LAB 3 — Visualização Loss × ASR",             "lab3_visualization"),
    "4": ("LAB 4 — Transferabilidade do Suffix",         "lab4_transfer"),
    "5": ("LAB 5 — Defesas contra GCG",                  "lab5_defenses"),
}


def main():
    console.print(Panel(
        "[bold cyan]BLIS SECURITY[/bold cyan]\n"
        "[white]Universal Adversarial Attacks on Aligned LLMs[/white]\n"
        "[dim]Zou et al., 2023 — Reprodução Prática[/dim]",
        border_style="cyan",
    ))

    console.print("\n[bold]Labs disponíveis:[/bold]")
    for key, (name, _) in LABS.items():
        console.print(f"  [{key}] {name}")
    console.print("  [A] Executar todos\n")

    choice = Prompt.ask("Escolha", choices=[*LABS.keys(), "A", "a"], default="1")

    if choice.upper() == "A":
        for key, (name, module) in LABS.items():
            console.rule(f"[cyan]{name}[/cyan]")
            importlib.import_module(module).main()
    else:
        name, module = LABS[choice]
        console.rule(f"[cyan]{name}[/cyan]")
        importlib.import_module(module).main()


if __name__ == "__main__":
    main()
