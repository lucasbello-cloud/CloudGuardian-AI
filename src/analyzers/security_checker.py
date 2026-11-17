import json
from pathlib import Path


def analyze_config(file_path):
    path = Path(file_path)

    if not path.exists():
        return {"erro": "Arquivo não encontrado"}

    with path.open("r", encoding="utf-8") as file:
        config = json.load(file)

    findings = []

    checks = [
        ("public_access", True, "ALTO",
         "Acesso público habilitado",
         "Revisar as permissões de acesso."),

        ("encryption", False, "ALTO",
         "Criptografia desabilitada",
         "Habilitar criptografia."),

        ("mfa_enabled", False, "ALTO",
         "Autenticação multifator desabilitada",
         "Habilitar autenticação multifator."),

        ("backup_enabled", False, "MÉDIO",
         "Backup desabilitado",
         "Configurar backups periódicos."),

        ("logging_enabled", False, "MÉDIO",
         "Registro de atividades desabilitado",
         "Habilitar registros de atividades.")
    ]

    for key, unsafe_value, risk, problem, recommendation in checks:
        if config.get(key) is unsafe_value:
            findings.append({
                "risco": risk,
                "problema": problem,
                "recomendacao": recommendation
            })

    return findings
