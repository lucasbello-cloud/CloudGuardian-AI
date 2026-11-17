from src.analyzers.security_checker import analyze_config
from src.analyzers.recommendation_engine import generate_recommendations
from src.reports.pdf_report import generate_pdf
from src.core.risk_score import calculate_score
from src.core.classifier import classify_score
from src.core.database import init_db, save_audit

print("=" * 45)
print("       CLOUDGUARDIAN AI")
print("       AUDITORIA DE SEGURANÇA")
print("=" * 45)

init_db()

resultados = analyze_config("data/config.json")

if isinstance(resultados, dict):
    print(resultados["erro"])

else:
    for item in resultados:
        print(f"Risco: {item['risco']}")
        print(f"Problema: {item['problema']}")
        print(f"Recomendação: {item['recomendacao']}")
        print("-" * 35)
    recomendacoes = generate_recommendations(resultados)

    print("\nRECOMENDAÇÕES PRIORIZADAS")
    print("=" * 35)

    for item in recomendacoes:
        print(f"Prioridade: {item['prioridade']}")
        print(f"Problema: {item['problema']}")
        print(f"Ação recomendada: {item['acao']}")
        print("-" * 35)
    score = calculate_score(resultados)
    classificacao = classify_score(score)

    arquivo_pdf = generate_pdf(score, classificacao, resultados, recomendacoes)
    print(f"\nRelatório PDF gerado: {arquivo_pdf}")

    save_audit(score, classificacao, len(resultados))

    print(f"\nPONTUAÇÃO: {score}/100")
    print(f"CLASSIFICAÇÃO: {classificacao}")
    print("\nAuditoria salva no banco de dados!")

print("=" * 45)
