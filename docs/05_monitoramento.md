# 05 - Monitoramento

## Objetivo

Monitorar a execução da automação e registrar o histórico das operações executadas.

---

## Arquivo de Log

Localização:

```text
logs/execucao.csv
```

---

## Estrutura do Log

Campos registrados:

| Campo | Descrição |
|---------|---------|
| data_hora_inicio | Início da execução |
| data_hora_fim | Fim da execução |
| duracao_segundos | Tempo total da etapa |
| processo | Processo executado |
| status | Resultado da execução |
| mensagem | Detalhes da execução |

---

## Processos Monitorados

### Conversão XLSB → XLSX

```text
CONVERSAO_XLSB_XLSX
```

Responsável pela conversão do arquivo XLSB para XLSX.

---

### Atualização do ETL

```text
ATUALIZACAO_ETL
```

Responsável por atualizar as consultas do ETL.

---

## Exemplo de Sucesso

```csv
2026-10-26 15:43:25,
2026-10-26 15:45:45,
140,
CONVERSAO_XLSB_XLSX,
SUCESSO,
Arquivo convertido com sucesso
```

```csv
2026-10-26 15:45:54,
2026-10-26 15:48:58,
184,
ATUALIZACAO_ETL,
SUCESSO,
Refresh concluído com sucesso
```

---

## Indicadores Operacionais

Tempo médio observado:

| Processo | Tempo Médio |
|-----------|------------|
| CONVERSAO_XLSB_XLSX | 2 a 3 minutos |
| ATUALIZACAO_ETL | 2 a 4 minutos |
| Processo Completo | 5 a 6 minutos |

---

## Verificações Recomendadas

Verificar periodicamente:

- Presença de registros recentes.
- Status igual a SUCESSO.
- Ausência de mensagens de erro.
- Duração compatível com a média histórica.

---

## Tratamento de Erros

Sempre consultar a coluna:

```text
mensagem
```

para identificar a causa da falha registrada.