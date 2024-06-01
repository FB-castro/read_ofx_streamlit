import sys
import os
import streamlit as st
import pandas as pd

# Adicionar o diretório pai ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from transform.utils import parse_ofx_to_dict

# Configuração da página
st.set_page_config(
    page_title="Convert OFX File",
    page_icon=":file:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Adicione o seletor de arquivo OFX
file = st.file_uploader("Escolha o arquivo OFX", type=['ofx'])

if file is not None:
    try:
        # Chamar a função para processar o OFX e retornar um dicionário
        data_dict = parse_ofx_to_dict(file)
        
        # Verifique se ocorreu um erro durante o processamento
        if "error" not in data_dict:
            # Criar um DataFrame a partir do dicionário
            df = pd.DataFrame(data_dict)
            st.write(df)
        else:
            st.error(f"Erro ao processar o arquivo OFX: {data_dict['error']}")
    except Exception as e:
        st.error(f"Ocorreu um erro inesperado: {str(e)}")
else:
    st.info("Nenhum arquivo OFX carregado.")
