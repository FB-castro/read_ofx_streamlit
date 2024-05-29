import streamlit as st
import pandas as pd
import sys
import os

# Adicionar o diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Agora podemos importar o módulo transform.utils
from transform.utils import parse_ofx_to_dict, getattr_safe


# Configuração da página
st.set_page_config(
    page_title="Convert OFX File",
    page_icon=":file:",
    layout="wide",
    initial_sidebar_state="expanded",
)


# Adicione o seletor de arquivo OFX
file = st.file_uploader("Escolha o arquivo OFX", type='.ofx')

if file is not None:
    # Chama a função para processar o OFX e retorna um dicionário
    data_dict = parse_ofx_to_dict(file)

    # Cria um DataFrame a partir do dicionário
    if "error" not in data_dict:
        df = pd.DataFrame(data_dict)
        st.write(df)
    else:
        st.write(data_dict["error"])
else:
    st.write("Nenhum arquivo OFX carregado.")
