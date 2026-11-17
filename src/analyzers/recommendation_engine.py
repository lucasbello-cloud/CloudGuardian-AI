def generate_recommendations(findings):
    recommendations = []

    priority = {
        "ALTO": 1,
        "MÉDIO": 2,
        "BAIXO": 3
    }

    ordered_findings = sorted(
        findings,
        key=lambda item: priority.get(item["risco"], 4)
    )

    for item in ordered_findings:
        recommendations.append({
            "prioridade": item["risco"],
            "problema": item["problema"],
            "acao": item["recomendacao"]
        })

    return recommendations
