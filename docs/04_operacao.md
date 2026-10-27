# 04 - Operação

## Execução Automática

A execução padrão ocorre através do Windows Task Scheduler.

Horários configurados:

- Terça-feira às 09:00
- Terça-feira às 14:00

---

## Execução Manual

### Opção 1 - Produção

Executar:

```text
iniciar_automacao.bat
```

A automação será executada e a janela será fechada automaticamente ao término.

---

### Opção 2 - Diagnóstico

Executar:

```text
iniciar_automacao_teste.bat
```

A automação será executada e permanecerá aberta ao final, permitindo visualizar mensagens e erros.

---

### Opção 3 - Execução Invisível

Executar:

```text
executar_oculto.vbs
```

A automação será executada em segundo plano sem exibir janelas.

---

## Como validar a execução

Verificar:

```text
logs/execucao.csv
```

Os registros devem apresentar:

```text
CONVERSAO_XLSB_XLSX
SUCESSO

ATUALIZACAO_ETL
SUCESSO
```

---

## Tempo médio de execução

### Conversão

Entre:

```text
2 e 3 minutos
```

### Atualização ETL

Entre:

```text
2 e 4 minutos
```

### Processo completo

Aproximadamente:

```text
5 a 6 minutos
```

---

## Resultado Esperado

Ao final da execução:

✅ estacoes_de_XXXX.xlsx atualizado

✅ ETL_Migrar_Circuitos_Estacoes.xlsx atualizado

✅ execucao.csv atualizado

✅ Processo executado sem intervenção manual
