import csv
import json
from pathlib import Path


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

ARQUIVO_LOG = config["arquivo_log"]


# ==========================
# FUNÇÃO DE LOG
# ==========================

def registrar_log(
    processo,
    status,
    mensagem,
    data_hora_inicio,
    data_hora_fim
):
    """
    Registra execução no CSV.
    """

    duracao = (
        data_hora_fim - data_hora_inicio
    ).total_seconds()

    with open(
        ARQUIVO_LOG,
        mode="a",
        newline="",
        encoding="utf-8"
    ) as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            data_hora_inicio,
            data_hora_fim,
            int(duracao),
            processo,
            status,
            mensagem
        ])