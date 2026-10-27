# Automação de Atualização de Base Operacional

Projeto desenvolvido para automatizar a atualização de bases operacionais utilizadas em processos analíticos, eliminando processos manuais de conversão, atualização de ETL e atualização de consultas Power Query.

## Principais resultados

✅ Atualização automática de bases

✅ Execução invisível em segundo plano

✅ Atualização automática de ETL

✅ Registro completo em log

✅ Agendamento via Windows Scheduler

✅ Redução de atividades operacionais manuais

✅ Tempo médio de execução: 5 a 6 minutos


## Objetivo

Automatizar a atualização de uma base operacional utilizada em processos analíticos, eliminando atividades manuais de atualização de arquivos, redução de erros operacionais e aumento da confiabilidade das informações.

---

## Fluxo Automatizado

```text
SharePoint
↓
Base_Status_Estacoes_DeAverage.xlsb
↓
Conversão XLSB → XLSX
↓
estacoes_de_XXXX.xlsx
↓
Atualização automática do ETL
↓
ETL_Migrar_Circuitos_Estacoes.xlsx
↓
Registro em Log
```

---

## Arquitetura

```text
Power Automate
↓
Último arquivo XLSB
↓
Base_Status_Estacoes_DeAverage.xlsb

↓

Windows Scheduler
↓
executar_oculto.vbs

↓

iniciar_automacao.bat

↓

orquestrador.py

↓

converter_xlsb_para_xlsx.py

↓

atualizar_etl.py

↓

execucao.csv
```

---

## Tecnologias Utilizadas

- Python
- Pandas
- OpenPyXL
- PyXLSB
- PyWin32
- Power Automate
- SharePoint
- Excel
- Power Query
- Windows Task Scheduler

---

## Funcionalidades

✅ Conversão automática XLSB → XLSX

✅ Atualização automática de ETL

✅ Atualização de Power Query

✅ Execução silenciosa em segundo plano

✅ Registro de logs

✅ Recuperação automática após falhas

✅ Agendamento automático

---

## Estrutura do Projeto

```text
Automacao_Estacoes_DeAverage

├── config
├── docs
├── logs
├── scripts
├── iniciar_automacao.bat
├── iniciar_automacao_teste.bat
├── executar_oculto.vbs
└── README.md
```

---

## Monitoramento

Todos os eventos são registrados em:

```text
logs/execucao.csv
```

Informações registradas:

- Data/Hora início
- Data/Hora fim
- Duração em segundos
- Processo
- Status
- Mensagem

---

## Status

Projeto em produção.
