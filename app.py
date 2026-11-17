from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from src.core.database import init_db, get_audits
from html import escape
import subprocess
import sys

app = FastAPI(title="CloudGuardian AI")


@app.post("/executar")
def executar_auditoria():
    subprocess.run([sys.executable, "main.py"], check=True)
    return RedirectResponse(url="/", status_code=303)

@app.get("/relatorio")
def abrir_relatorio():
    from fastapi.responses import FileResponse

    return FileResponse(
        "data/relatorio_cloudguardian.pdf",
        media_type="application/pdf",
        filename="relatorio_cloudguardian.pdf"
    )
@app.get("/", response_class=HTMLResponse)
def dashboard():
    init_db()
    audits = get_audits()

    total = len(audits)
    total_risks = sum(audit[3] for audit in audits)

    if audits:
        latest = audits[0]
        score = latest[1]
        classification = escape(latest[2])
    else:
        score = 0
        classification = "Sem auditorias"

    rows = ""

    for audit in audits:
        rows += f"""
        <tr>
            <td>#{audit[0]}</td>
            <td>{audit[1]}/100</td>
            <td>{escape(audit[2])}</td>
            <td>{audit[3]}</td>
            <td>{escape(audit[4])}</td>
        </tr>
        """

    if not rows:
        rows = "<tr><td colspan='5'>Nenhuma auditoria registrada</td></tr>"

    return f"""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>CloudGuardian AI</title>
        <style>
            * {{ box-sizing: border-box; }}
            body {{
                margin: 0; padding: 35px;
                background: #0b1120; color: #e2e8f0;
                font-family: Arial, sans-serif;
            }}
            header {{ margin-bottom: 30px; }}
            header h1 {{ color: #38bdf8; }}
            button {{
                background: #0284c7; color: white;
                border: none; padding: 12px 20px;
                border-radius: 8px; cursor: pointer;
                font-size: 15px;
            }}
            button:hover {{ background: #0369a1; }}
            .cards {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
                gap: 18px;
            }}
            .card {{
                background: #172338;
                border: 1px solid #293b55;
                border-radius: 12px; padding: 22px;
            }}
            .number {{
                font-size: 32px; font-weight: bold;
                color: #38bdf8;
            }}
            .critical {{ color: #fb7185; }}
            table {{
                width: 100%; border-collapse: collapse;
                margin-top: 20px;
            }}
            th, td {{
                padding: 14px; text-align: left;
                border-bottom: 1px solid #293b55;
            }}
            th {{ color: #38bdf8; }}
            .history {{ margin-top: 25px; overflow-x: auto; }}
            footer {{ margin-top: 40px; color: #94a3b8; }}
        </style>
    </head>
    <body>
        <header>
            <h1>CLOUDGUARDIAN AI</h1>
            <p>Plataforma de auditoria e monitoramento de segurança</p>
            <form action="/executar" method="post">
                <button type="submit">Executar nova auditoria</button>
            </form>
            <p><a href="/relatorio" target="_blank" style="color: #38bdf8;">Abrir relatório PDF</a></p>
        </header>

        <section class="cards">
            <div class="card">
                <p>Pontuação de segurança</p>
                <div class="number">{score}/100</div>
            </div>
            <div class="card">
                <p>Classificação</p>
                <div class="number critical">{classification}</div>
            </div>
            <div class="card">
                <p>Total de auditorias</p>
                <div class="number">{total}</div>
            </div>
            <div class="card">
                <p>Riscos identificados</p>
                <div class="number">{total_risks}</div>
            </div>
        </section>

        <section class="card history">
            <h2>Histórico de auditorias</h2>
            <table>
                <tr>
                    <th>ID</th>
                    <th>Pontuação</th>
                    <th>Classificação</th>
                    <th>Riscos</th>
                    <th>Data</th>
                </tr>
                {rows}
            </table>
        </section>

        <footer>CloudGuardian AI | Python Security Project</footer>
    </body>
    </html>
    """
