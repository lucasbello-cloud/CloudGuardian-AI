def classify_score(score):

    if score <= 39:
        return "RISCO CRÍTICO"

    elif score <= 69:
        return "RISCO MODERADO"

    elif score <= 89:
        return "BOM NÍVEL DE SEGURANÇA"

    else:
        return "EXCELENTE NÍVEL DE SEGURANÇA"
