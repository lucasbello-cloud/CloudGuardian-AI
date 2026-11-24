# CloudGuardian AI

Projeto de auditoria local de configurações de segurança em nuvem, desenvolvido em Python.

## Objetivo

Identificar configurações inseguras, calcular uma pontuação de risco e apresentar recomendações de segurança.

## Funcionalidades

- Análise de configurações JSON.
- Identificação de riscos de acesso público.
- Verificação de criptografia e MFA.
- Verificação de backups e registros de atividades.
- Pontuação e classificação de riscos.
- Recomendações organizadas por prioridade.
- Dashboard web responsivo.
- Interface com tema claro e escuro.
- Histórico de auditorias com SQLite.
- Relatórios em PDF com gráficos.
- Testes automatizados com Pytest.

## Interface

O dashboard apresenta:

- Pontuação de segurança.
- Classificação dos riscos.
- Resultados da auditoria.
- Recomendações de segurança.
- Histórico de auditorias.
- Acesso ao relatório em PDF.

## Tecnologias

- Python
- FastAPI
- HTML, CSS e JavaScript
- SQLite
- Matplotlib
- ReportLab
- Pytest
- Linux / Ubuntu WSL

## Estrutura do projeto

```text
CloudGuardian-AI/
├── app.py
├── data/
├── evidencias/
├── src/
├── tests/
├── web/
└── README.md
```

## Como executar

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

Inicie o servidor:

```bash
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Acesse no navegador:

```text
http://127.0.0.1:8000
```

## Testes

Execute:

```bash
python -m pytest -v
```

## Evidências

As capturas de tela do desenvolvimento e da execução estão disponíveis na pasta `evidencias/`.

## Observação

Projeto educacional de auditoria local, baseado em regras e configurações de exemplo. Não está conectado a contas ou recursos reais da AWS.

## Autor

Projeto desenvolvido para portfólio na área de Computação em Nuvem e Segurança em Nuvem.
