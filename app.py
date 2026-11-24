from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse

from src.analyzers.security_checker import analyze_config
from src.analyzers.recommendation_engine import generate_recommendations
from src.reports.pdf_report import generate_pdf
from src.core.risk_score import calculate_score
from src.core.classifier import classify_score
from src.core.database import init_db, save_audit, get_audits

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="CloudGuardian AI")

init_db()


@app.get("/")
def dashboard():
    return FileResponse(BASE_DIR / "web" / "index.html")


@app.post("/api/audit")
def executar_auditoria():
    resultados = analyze_config("data/config.json")

    if isinstance(resultados, dict):
        return JSONResponse(resultados, status_code=400)

    recomendacoes = generate_recommendations(resultados)
    score = calculate_score(resultados)
    classificacao = classify_score(score)

    generate_pdf(score, classificacao, resultados, recomendacoes)
    save_audit(score, classificacao, len(resultados))

    return {
        "score": score,
        "classificacao": classificacao,
        "resultados": resultados,
        "recomendacoes": recomendacoes
    }


@app.get("/api/audits")
def historico():
    return [list(audit) for audit in get_audits()]


@app.get("/api/report")
def abrir_relatorio():
    arquivo = BASE_DIR / "data" / "relatorio_cloudguardian.pdf"

    if not arquivo.exists():
        return JSONResponse(
            {"erro": "Relatório ainda não foi gerado."},
            status_code=404
        )

    return FileResponse(
        arquivo,
        media_type="application/pdf",
        filename="relatorio_cloudguardian.pdf"
    )
