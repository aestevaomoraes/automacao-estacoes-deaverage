import subprocess
import sys
from pathlib import Path


print("\n================================")
print("INÍCIO DA AUTOMAÇÃO")
print("================================\n")


base_path = Path(__file__).parent

script_conversao = (
    base_path / "converter_xlsb_para_xlsx.py"
)

script_etl = (
    base_path / "atualizar_etl.py"
)


# ==========================
# CONVERSÃO
# ==========================

print("Executando conversão XLSB -> XLSX...\n")

subprocess.run(
    [sys.executable, str(script_conversao)],
    check=True
)


# ==========================
# ETL
# ==========================

print("\nExecutando atualização ETL...\n")

subprocess.run(
    [sys.executable, str(script_etl)],
    check=True
)


print("\n================================")
print("AUTOMAÇÃO CONCLUÍDA")
print("================================\n")