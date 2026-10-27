# 06 - Troubleshooting

## Objetivo

Documentar problemas encontrados durante o desenvolvimento e operação da automação.

---

## Erro: pandas não encontrado

Mensagem:

```text
ModuleNotFoundError: No module named 'pandas'
```

Causa:

Bibliotecas não instaladas no ambiente Python.

Solução:

```bash
pip install pandas pyxlsb openpyxl
```

---

## Erro: Open.Save

Mensagem:

```text
AttributeError: Open.Save
```

Causa:

Instabilidade na referência do Workbook durante a interação do Python com o Excel COM.

Solução:

Validar o objeto Workbook retornado pela abertura do arquivo e utilizar o método de salvamento que apresentou comportamento consistente nos testes.

---

## Erro: ActiveWorkbook

Mensagem:

```text
AttributeError: Excel.Application.ActiveWorkbook
```

Causa:

O Excel não manteve uma referência válida para o ActiveWorkbook durante a execução automatizada.

Solução:

Utilizar diretamente o Workbook retornado pelo comando Open.

---

## Erro: Scheduler executando janela visível

Problema:

Execução utilizando BAT exibia janela do Prompt de Comando.

Solução:

Implementação de:

```text
executar_oculto.vbs
```

com:

```vbscript
WshShell.Run ..., 0
```

permitindo execução invisível.

---

## Erro: pythonw.exe

Problema:

Execução utilizando pythonw.exe apresentou comportamento diferente do ambiente validado.

Solução:

Manter:

```text
python.exe
```

e executar de forma invisível utilizando:

```text
wscript.exe
+
executar_oculto.vbs
```

---

## Verificações recomendadas

Quando ocorrer uma falha:

1. Consultar:

```text
logs/execucao.csv
```

2. Verificar a coluna:

```text
mensagem
```

3. Executar:

```text
iniciar_automacao_teste.bat
```

4. Validar:

- disponibilidade da base XLSB
- existência do arquivo XLSX
- disponibilidade do ETL
- sincronização do OneDrive