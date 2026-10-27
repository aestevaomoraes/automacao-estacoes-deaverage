# 07 - Publicação GitHub

## Objetivo

Disponibilizar uma versão pública do projeto preservando informações corporativas e dados sensíveis.

---

## Informações que NÃO devem ser publicadas

Remover ou anonimizar:

- Nome da empresa
- Endereços SharePoint
- Endereços OneDrive corporativos
- Endereços de e-mail corporativos
- Usuários corporativos
- Diretórios pessoais
- Credenciais
- Caminhos internos

---

## Arquivos que devem permanecer locais

### config.json

Não publicar.

Adicionar ao:

```text
.gitignore
```

---

## Criar arquivo exemplo

Criar:

```text
config.example.json
```

Exemplo:

```json
{
    "arquivo_xlsb": "<CAMINHO_XLSB>",
    "arquivo_xlsx": "<CAMINHO_XLSX>",
    "arquivo_etl": "<CAMINHO_ETL>",
    "arquivo_log": "<CAMINHO_LOG>"
}
```

---

## Estrutura pública recomendada

```text
README.md
docs/
scripts/
.gitignore
config.example.json
```

---

## Principais Destaques do Projeto

- Power Automate
- SharePoint
- Python
- Pandas
- OpenPyXL
- PyXLSB
- PyWin32
- Power Query
- Windows Task Scheduler

---

## Benefícios Gerados

- Redução de atividades manuais
- Padronização operacional
- Atualização automática de ETL
- Monitoramento por logs
- Execução invisível em segundo plano
- Melhoria da confiabilidade dos dados

---

## Material para LinkedIn

Foco da publicação:

Automação de atualização de bases operacionais utilizando Power Automate, Python e Excel.

Objetivos:

- Compartilhar conhecimento
- Demonstrar aplicação prática
- Apresentar arquitetura da solução
- Evidenciar benefícios operacionais
