def calculate_score(findings):
    score = 100

    penalties = {
        "ALTO": 40,
        "MÉDIO": 20,
        "BAIXO": 10
    }

    for finding in findings:
        score -= penalties.get(finding["risco"], 0)

    return max(0, score)
