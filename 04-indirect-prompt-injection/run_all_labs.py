import sys, os
from colorama import Fore, Style, init

init(autoreset=True)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from labs import (
    lab1_info_gathering,
    lab2_fraud_phishing,
    lab3_ai_worm,
    lab4_remote_control,
    lab5_persistence,
    lab6_manipulated_content,
    lab7_defenses
)

LABS = [
    ("LAB 1 — Information Gathering",   lab1_info_gathering),
    ("LAB 2 — Fraud & Phishing",         lab2_fraud_phishing),
    ("LAB 3 — AI Worm",                  lab3_ai_worm),
    ("LAB 4 — Remote Control",           lab4_remote_control),
    ("LAB 5 — Persistence",              lab5_persistence),
    ("LAB 6 — Manipulated Content",      lab6_manipulated_content),
    ("LAB 7 — Defenses",                 lab7_defenses),
]

def main():
    print(f"\n{Fore.CYAN}{'#'*60}")
    print(f"  BLIS SECURITY — Indirect Prompt Injection Labs")
    print(f"  Baseado em: Greshake et al., 2023")
    print(f"{'#'*60}{Style.RESET_ALL}\n")

    print("Escolha um lab para executar:")
    for i, (name, _) in enumerate(LABS, 1):
        print(f"  {i}. {name}")
    print(f"  0. Executar TODOS\n")

    choice = input("Opção: ").strip()

    if choice == "0":
        for name, lab in LABS:
            try:
                lab.run()
            except Exception as e:
                print(f"{Fore.RED}Erro no {name}: {e}{Style.RESET_ALL}")
    elif choice.isdigit() and 1 <= int(choice) <= len(LABS):
        idx = int(choice) - 1
        LABS[idx][1].run()
    else:
        print(f"{Fore.RED}Opção inválida.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
