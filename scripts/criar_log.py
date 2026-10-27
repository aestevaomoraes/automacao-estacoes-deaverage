import csv
import json
from pathlib import Path

# Carrega config
config_path = Path(__file__).parent.parent / "config" / "config.json"

with open(config_path, "r", encoding="utf-8") as arquivo:
    config = json.load(arquivo)

arquivo_log = config["arquivo_log"]

# Cria CSV se não existir
if not Path(arquivo_log).exists():

    with open(
        arquivo_log,
        "w",
        newline="",
        encoding="utf-8"
    ) as csvfile:

        writer = csv.writer(csvfile)

        writer.writerow([
            "data_hora_inicio",
            "data_hora_fim",
            "duracao_segundos",
            "processo",
            "status",
            "mensagem"
        ])

print("LOG OK")