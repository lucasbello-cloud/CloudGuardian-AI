from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, Image
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime
from src.reports.chart_generator import generate_risk_chart


def generate_pdf(score, classification, findings, recommendations):

    filename = "data/relatorio_cloudguardian.pdf"

    document = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    content = []

    content.append(Paragraph("CLOUDGUARDIAN AI", styles["Title"]))
    content.append(Paragraph(
        "Relatório de Auditoria de Segurança",
        styles["Heading2"]
    ))
    content.append(Spacer(1, 20))

    content.append(Paragraph(
        f"Data: {datetime.now().strftime('%d/%m/%Y %H:%M')}",
        styles["Normal"]
    ))
    content.append(Paragraph(
        f"Pontuação: {score}/100",
        styles["Normal"]
    ))
    content.append(Paragraph(
        f"Classificação: {classification}",
        styles["Normal"]
    ))

    content.append(Spacer(1, 15))
    content.append(Paragraph("RESUMO EXECUTIVO", styles["Heading2"]))
    content.append(Paragraph(
        f"A auditoria identificou {len(findings)} riscos de segurança "
        f"na configuração analisada. A pontuação obtida foi "
        f"{score}/100, com classificação: {classification}.",
        styles["Normal"]
    ))

    content.append(Spacer(1, 20))
    content.append(Paragraph(
        "Distribuição dos riscos",
        styles["Heading2"]
    ))

    chart_path = generate_risk_chart(findings)
    content.append(Image(chart_path, width=400, height=250))

    content.append(Spacer(1, 20))
    content.append(Paragraph(
        "Riscos identificados",
        styles["Heading2"]
    ))

    data = [["Risco", "Problema", "Recomendação"]]

    for item in findings:
        data.append([
            item["risco"],
            item["problema"],
            item["recomendacao"]
        ])

    table = Table(data, repeatRows=1)
    table.setStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#172338")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 8)
    ])

    content.append(table)
    content.append(Spacer(1, 20))

    content.append(Paragraph(
        "Recomendações priorizadas",
        styles["Heading2"]
    ))

    for item in recommendations:
        content.append(Paragraph(
            f"<b>{item['prioridade']}</b> - {item['problema']}",
            styles["Normal"]
        ))
        content.append(Paragraph(
            f"Ação: {item['acao']}",
            styles["Normal"]
        ))
        content.append(Spacer(1, 8))

    document.build(content)

    return filename
