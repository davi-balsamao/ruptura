"""Abre o Simulador Elétrico no navegador: python rodar.py  (de qualquer pasta)."""
import os
import sys
from pathlib import Path

from streamlit.web import cli

AQUI = Path(__file__).resolve().parent
os.chdir(AQUI)  # o Streamlit lê .streamlit/config.toml (tema) da pasta atual
sys.argv = ["streamlit", "run", str(AQUI / "app.py"), *sys.argv[1:]]
sys.exit(cli.main())
