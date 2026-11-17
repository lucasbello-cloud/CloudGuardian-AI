from src.core.database import init_db, get_audits

init_db()

audits = get_audits()

print("=" * 55)
print("       CLOUDGUARDIAN AI - HISTÓRICO")
print("=" * 55)

if not audits:
    print("Nenhuma auditoria registrada.")

else:
    for audit in audits:
        print(f"\nAuditoria #{audit[0]}")
        print(f"Pontuação: {audit[1]}/100")
        print(f"Classificação: {audit[2]}")
        print(f"Total de riscos: {audit[3]}")
        print(f"Data: {audit[4]}")
        print("-" * 40)

print("\nTotal de auditorias:", len(audits))
