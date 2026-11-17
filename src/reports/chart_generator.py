import matplotlib.pyplot as plt
from pathlib import Path


def generate_risk_chart(findings):

    priorities = ["ALTO", "MÉDIO", "BAIXO"]

    quantities = [
        sum(1 for item in findings if item["risco"] == priority)
        for priority in priorities
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(priorities, quantities)

    plt.title("Distribuição de Riscos - CloudGuardian AI")
    plt.xlabel("Prioridade")
    plt.ylabel("Quantidade de riscos")

    plt.tight_layout()

    filename = Path("data/graficos/distribuicao_riscos.png")

    plt.savefig(filename)
    plt.close()

    return str(filename)
