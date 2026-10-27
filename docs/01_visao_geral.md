# 01 - Visão Geral

## Objetivo

Automatizar o processo de atualização de bases operacionais utilizadas em análises e relatórios.

## Problema

Anteriormente o processo exigia:

- Download manual do arquivo
- Conversão manual de XLSB para XLSX
- Atualização manual do Power Query
- Atualização manual do ETL
- Risco de esquecimento
- Risco de utilização de bases desatualizadas

## Solução

Foi desenvolvida uma automação composta por:

- Power Automate
- Python
- Excel COM (PyWin32)
- Power Query
- Windows Task Scheduler

## Benefícios

✅ Redução de atividades manuais

✅ Padronização do processo

✅ Rastreabilidade através de logs

✅ Execução automática em horários programados

✅ Maior confiabilidade das análises

## Resultado

Após a implementação da automação:

- Eliminação da atualização manual dos arquivos.
- Redução do risco de erro operacional.
- Atualização automática de bases analíticas.
- Atualização automática do ETL.
- Registro completo das execuções em log.
- Execução programada e invisível em segundo plano.

Tempo médio de execução:

| Processo | Tempo Médio |
|-----------|------------|
| Conversão XLSB → XLSX | ~2m30s |
| Atualização ETL | ~3m00s |
| Tempo Total | ~5m30s |