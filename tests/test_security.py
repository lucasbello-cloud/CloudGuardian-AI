from src.analyzers.security_checker import analyze_config


def test_detects_public_access(tmp_path):
    config = tmp_path / "config.json"

    config.write_text(
        '{"public_access": true}',
        encoding="utf-8"
    )

    findings = analyze_config(config)

    assert any(
        item["problema"] == "Acesso público habilitado"
        for item in findings
    )
def test_detects_disabled_encryption(tmp_path):
    config = tmp_path / "config.json"

    config.write_text(
        '{"encryption": false}',
        encoding="utf-8"
    )

    findings = analyze_config(config)

    assert any(
        item["problema"] == "Criptografia desabilitada"
        for item in findings
    )
from src.core.risk_score import calculate_score


def test_calculates_security_score():
    findings = [
        {"risco": "ALTO"},
        {"risco": "MÉDIO"}
    ]

    score = calculate_score(findings)

    assert score == 40
from src.core.classifier import classify_score


def test_classifies_critical_risk():
    classification = classify_score(20)

    assert classification == "RISCO CRÍTICO"
from src.analyzers.recommendation_engine import generate_recommendations


def test_prioritizes_high_risks():
    findings = [
        {"risco": "MÉDIO", "problema": "Backup desabilitado",
         "recomendacao": "Configurar backup."},
        {"risco": "ALTO", "problema": "Criptografia desabilitada",
         "recomendacao": "Habilitar criptografia."}
    ]

    recommendations = generate_recommendations(findings)

    assert recommendations[0]["prioridade"] == "ALTO"
def test_handles_missing_config_file(tmp_path):
    config = tmp_path / "arquivo_inexistente.json"

    result = analyze_config(config)

    assert result == {"erro": "Arquivo não encontrado"}
