# 02 - Arquitetura da Solução

## Visão Geral

A solução foi construída para automatizar o processo completo de atualização de bases utilizadas em análises operacionais.

## Fluxo da Solução

```text
SharePoint
↓
Base_Status_Estacoes_DeAverage.xlsb

↓

Power Automate
↓
Download automático da versão mais recente

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

estacoes_de_XXXXX.xlsx

↓

atualizar_etl.py

↓

ETL_Migrar_Circuitos_Estacoes.xlsx

↓

logs/execucao.csv
```

## Componentes

### Power Automate

Responsável pela obtenção automática da versão mais recente do arquivo XLSB armazenado no SharePoint.

### Conversão XLSB → XLSX

Realizada através do script:

```text
converter_xlsb_para_xlsx.py
```

Bibliotecas utilizadas:

- pandas
- pyxlsb
- openpyxl

### Atualização do ETL

Realizada através do script:

```text
atualizar_etl.py
```

Biblioteca utilizada:

```text
pywin32
```

O script executa:

- abertura do Excel
- atualização das consultas
- salvamento automático
- fechamento do arquivo

### Orquestração

Responsável por controlar a sequência de execução:

```text
orquestrador.py
```

Fluxo:

Conversão
↓

Atualização ETL
↓

Registro em Log

### Monitoramento

Todas as execuções são registradas em:

```text
logs/execucao.csv
```
