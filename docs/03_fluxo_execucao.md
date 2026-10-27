# 03 - Fluxo de Execução

## Agendamento

A automação é executada automaticamente pelo Windows Task Scheduler.

Horários programados:

- Terça-feira às 09:00
- Terça-feira às 14:00

---

## Sequência de Execução

```text
Agendador de Tarefas
↓
wscript.exe
↓
executar_oculto.vbs
↓
iniciar_automacao.bat
↓
orquestrador.py
```

---

## Etapa 1 - Conversão XLSB para XLSX

Script:

```text
converter_xlsb_para_xlsx.py
```

Fluxo:

```text
Base_Status_Estacoes_DeAverage.xlsb
↓
estacoes_de_avarage.xlsx
```

Objetivo:

Converter automaticamente o arquivo XLSB recebido para o formato XLSX utilizado pelas consultas analíticas.

---

## Etapa 2 - Atualização do ETL

Script:

```text
atualizar_etl.py
```

Fluxo:

```text
ETL_Migrar_Circuitos_Estacoes.xlsx
↓
RefreshAll()
↓
Salvar
↓
Fechar
```

Objetivo:

Atualizar todas as consultas e conexões do ETL automaticamente.

---

## Etapa 3 - Registro de Log

Arquivo:

```text
logs/execucao.csv
```

Informações registradas:

- Data/Hora início
- Data/Hora fim
- Duração
- Processo
- Status
- Mensagem

---

## Resultado Final

```text
Base XLSB atualizada
↓
Base XLSX atualizada
↓
ETL atualizado
↓
Logs atualizados
```

Sem necessidade de intervenção manual.