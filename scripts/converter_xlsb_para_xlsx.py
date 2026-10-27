import json
from pathlib import Path
from datetime import datetime

import pandas as pd
from pyxlsb import open_workbook

from logger import registrar_log


# ==========================
# CARREGAR CONFIGURAÇÃO
# ==========================

config_path = (
    Path(__file__).parent.parent
    / "config"
    / "config.json"
)

with open(config_path, "r", encoding="utf-8") as arquivo:
    config = json.load(arquivo)

arquivo_xlsb = config["arquivo_xlsb"]
arquivo_xlsx = config["arquivo_xlsx"]


# ==========================
# PROCESSAMENTO
# ==========================

inicio = datetime.now()

try:

    print("\nIniciando conversão...")

    with pd.ExcelWriter(
        arquivo_xlsx,
        engine="openpyxl"
    ) as writer:

        with open_workbook(arquivo_xlsb) as wb:

            for nome_aba in wb.sheets:

                print(f"Lendo aba: {nome_aba}")

                with wb.get_sheet(nome_aba) as sheet:

                    dados = []

                    for row in sheet.rows():

                        dados.append(
                            [
                                item.v
                                if item is not None
                                else None
                                for item in row
                            ]
                        )

                df = pd.DataFrame(dados)

                df.to_excel(
                    writer,
                    sheet_name=nome_aba[:31],
                    index=False,
                    header=False
                )

    fim = datetime.now()

    registrar_log(
        processo="CONVERSAO_XLSB_XLSX",
        status="SUCESSO",
        mensagem="Arquivo convertido com sucesso",
        data_hora_inicio=inicio,
        data_hora_fim=fim
    )

    print("\nConversão concluída com sucesso!")

except Exception as erro:

    fim = datetime.now()

    registrar_log(
        processo="CONVERSAO_XLSB_XLSX",
        status="ERRO",
        mensagem=str(erro),
        data_hora_inicio=inicio,
        data_hora_fim=fim
    )

    raise