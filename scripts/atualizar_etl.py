import json
from pathlib import Path
from datetime import datetime

import win32com.client

from logger import registrar_log


# ==========================
# CARREGA CONFIGURAÇÃO
# ==========================

config_path = (
    Path(__file__).parent.parent
    / "config"
    / "config.json"
)

with open(
    config_path,
    "r",
    encoding="utf-8"
) as arquivo:

    config = json.load(arquivo)

arquivo_etl = config["arquivo_etl"]


# ==========================
# PROCESSAMENTO
# ==========================

inicio = datetime.now()

excel = None

try:

    print("\nAbrindo Excel...")

    excel = win32com.client.Dispatch(
        "Excel.Application"
    )

    excel.Visible = False
    excel.DisplayAlerts = False

    print("\nAbrindo ETL...")

    workbook = excel.Workbooks.Open(
        arquivo_etl
    )

    print("\nETL aberto com sucesso!")

    print(workbook)
    print(type(workbook))

    print("\nIniciando RefreshAll...")

    workbook.RefreshAll()

    excel.CalculateUntilAsyncQueriesDone()

    print("\nRefresh concluído!")

    workbook.Save()

    print("\nArquivo salvo!")

    workbook.Close(
        SaveChanges=True
    )

    excel.Quit()

    fim = datetime.now()

    registrar_log(
        processo="ATUALIZACAO_ETL",
        status="SUCESSO",
        mensagem="Refresh concluído com sucesso",
        data_hora_inicio=inicio,
        data_hora_fim=fim
    )

    print("\nExcel fechado com sucesso!")

except Exception as erro:

    fim = datetime.now()

    registrar_log(
        processo="ATUALIZACAO_ETL",
        status="ERRO",
        mensagem=str(erro),
        data_hora_inicio=inicio,
        data_hora_fim=fim
    )

    if excel is not None:
        try:
            excel.Quit()
        except:
            pass

    raise