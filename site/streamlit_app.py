import streamlit as st
import requests as req

API_URL = st.secrets['API_URL']

st.title("Cálculo Retorno de Ações 📈")

# Inputs
enterprise = st.selectbox('Empresa', ['AAPL - Apple' ])
volume = st.text_input('Volume', value="", placeholder='ex. 8500')
prev_close = st.text_input('Valor último fechamento', value="", placeholder='ex. 240.00')

if (st.button('Calcular previsão')):
    
    payload = {
        "ticker": enterprise.split(" - ")[0],
        "volume": float(volume),
        "prev_close": float(prev_close)
    }
    
    try:
        response = req.post(f"{API_URL}/predict", json=payload)
        result = response.json()
        
        st.success(f'Previsão de retorno: {result["prediction"]:0.2f}')
    except Exception as e:
        st.error(f'Erro ao calcular previsão: {e}') 
