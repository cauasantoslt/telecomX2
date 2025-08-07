# app.py - Versão futurista

import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from sklearn.metrics import confusion_matrix

# ====================================================================
# Configurações da página e CSS customizado
# ====================================================================

st.set_page_config(
    page_title="TelecomX",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Roboto+Mono:wght@400;700&display=swap');
    
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #07000e;
        color: #e0e0ff;
        font-family: 'Roboto Mono', monospace;
    }
    
    h1, h2, h3, h4, h5, h6, .st-emotion-cache-1j0z80v, .st-emotion-cache-163k44b {
        font-family: 'Orbitron', sans-serif;
        color: #00ffff; /* Ciano para os títulos */
    }
    
    .st-emotion-cache-16idsl9 h1, .st-emotion-cache-16idsl9 h2 {
        text-align: center;
        margin-bottom: 2rem;
    }

    [data-testid="stSidebar"] {
        background-color: #030105;
        border-right: 2px solid #00ffff;
        box-shadow: 5px 0 15px rgba(0,255,255,0.2);
    }
    
    [data-testid="stTabs"] [data-baseweb="tab-list"] button {
        color: #e0e0ff;
        border-bottom: 2px solid transparent;
        font-weight: bold;
    }
    
    [data-testid="stTabs"] [data-baseweb="tab-list"] button:hover {
        color: #00ffff;
    }
    
    [data-testid="stTabs"] [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #00ffff;
        border-bottom: 2px solid #00ffff;
    }

    /* Estilo para botões */
    div.stButton > button {
        background-color: #0c0c1e;
        color: #00ffff;
        border: 2px solid #00ffff;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s;
    }
    div.stButton > button:hover {
        background-color: rgba(0,255,255,0.2);
        color: #ffffff;
        box-shadow: 0 0 10px #00ffff, 0 0 20px #00ffff;
    }

    /* Estilo para o formulário */
    [data-testid="stForm"] {
        background-color: #000000;
        border: 1px solid #333366;
        border-radius: 10px;
        padding: 2rem;
        box-shadow: 0 0 15px rgba(0,0,0,0.5);
    }
            

</style>
""", unsafe_allow_html=True)


# ====================================================================
# Constantes e Carregamento de Recursos
# ====================================================================
CHURN_COLORS = {'0': "#1f78b4", '1': "#8b0eff"}
PLOTLY_CMAP = 'Cividis'

@st.cache_data
def load_data():
    """Carrega e pré-processa os dados para os gráficos."""
    try:
        df = pd.read_csv('dados_tratados.csv')
        df = df.dropna(subset=['Churn'])
        df = df.drop(columns=['customerID', 'Contas_Diarias'])
        
        # Correção: Converter para int e depois para str para evitar o '0.0'
        df['Churn'] = df['Churn'].astype(int).astype(str)
        
        churn_column = df['Churn']
        df_to_encode = df.drop(columns=['Churn'])
        df_encoded = pd.get_dummies(df_to_encode, drop_first=True)
        df_encoded['Churn'] = churn_column.values

        return df, df_encoded
    except FileNotFoundError:
        st.error("Erro: O arquivo 'dados_tratados.csv' não foi encontrado. Certifique-se de que ele está no diretório correto.")
        return None, None

@st.cache_resource
def load_model_resources():
    """Carrega os recursos do modelo salvos em arquivos .pkl."""
    try:
        model = joblib.load('random_forest_model.pkl')
        scaler = joblib.load('scaler.pkl')
        feature_columns = joblib.load('feature_columns.pkl')
        return model, scaler, feature_columns
    except FileNotFoundError:
        st.error("Erro: Arquivos do modelo (.pkl) não foram encontrados. Por favor, treine o modelo e salve-o primeiro no seu notebook.")
        return None, None, None

df_raw, df_encoded = load_data()
model, scaler, feature_columns = load_model_resources()

# ====================================================================
# Layout da Aplicação Streamlit
# ====================================================================
st.title('📡 Análise Preditiva de Churn - TelecomX')
st.markdown("### ")

# Sidebar
with st.sidebar:
    st.image('https://placehold.co/150x150/2d0553/00ffff?text=TelecomX ', use_container_width=True)
    st.markdown("## Interface de Controle")
    st.markdown("Use esta interface para explorar os dados e prever a evasão de clientes.")
    st.markdown(
        """
        <p >
            Este projeto foi desenvolvido por <a href="https://github.com/cauasantoslt" target="_blank" style="color: #8b0eff; text-decoration: none;">Cauã Santos</a> com fins didáticos, sem objetivos lucrativos.
        
        </p>
        """, 
        unsafe_allow_html=True
    )
    st.markdown("""
    <style>
        .footer-social-links {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 250px; /* Ajuste para a largura da sua sidebar */
            display: flex;
            justify-content: center;
            gap: 1.5rem;
            padding: 1rem 0;
            background-color: #030105; /* Cor de fundo da sidebar */
            z-index: 1000;
        }
        .footer-social-links img {
            height: 30px; /* Tamanho dos ícones */
            opacity: 0.7;
            transition: opacity 0.3s ease-in-out;
            filter: invert(100%); /* Garante que os ícones fiquem brancos, caso a imagem original não seja */
        }
        .footer-social-links img:hover {
            opacity: 1;
        }
    </style>
    <div class="footer-social-links">
        <a href="https://instagram.com/cauasantoslt" target="_blank">
            <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/instagram.svg" alt="Instagram">
        </a>
        <a href="https://linkedin.com/in/cauasantoslt" target="_blank">
            <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/linkedin-in.svg" alt="LinkedIn">
        </a>
        <a href="https://github.com/cauasantoslt" target="_blank">
            <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/brands/github.svg" alt="GitHub">
        </a>
    </div>
    """, unsafe_allow_html=True)

# ====================================================================
# Seção 1: Resumo Executivo e Métricas
# ====================================================================
st.header('🚀 Status do Sistema')
st.markdown("""
<div style="background-color: #46006e; padding: 1rem; border-radius: 10px; border: 1px solid #333366;">
    <p style="font-family: 'Roboto Mono', monospace; font-size: 1.1rem; color: #e0e0ff;">
        O modelo Random Forest está operacional e calibrado para prever a evasão de clientes (Churn).
        Sua precisão na identificação de clientes em risco é vital para as estratégias de retenção.
    </p>
</div>
""", unsafe_allow_html=True)

if df_raw is not None:
    total_customers = len(df_raw)
    total_churn = df_raw['Churn'].astype(int).sum()
    churn_rate = (total_churn / total_customers) * 100

    col_metric1, col_metric2 = st.columns(2)
    with col_metric1:
        st.metric(label="Total de Clientes", value=f"{total_customers}")
    with col_metric2:
        st.metric(label="Taxa de Churn Atual", value=f"{churn_rate:.2f}%", delta="Risco em Monitoramento")

st.markdown("---")

# ====================================================================
# Seção 2: Fatores Chave que Influenciam a Evasão
# ====================================================================
st.header('📊 Análise de Variáveis Críticas')
st.markdown("Explore a relevância dos fatores que mais impactam a decisão de evasão.")

if model and df_encoded is not None:
    X = df_encoded.drop('Churn', axis=1)
    importance_df = pd.DataFrame({
        'Importância': model.feature_importances_,
        'Variável': X.columns
    }).sort_values(by='Importância', ascending=False).head(10)

    fig_imp = px.bar(importance_df,
                      x='Importância',
                      y='Variável',
                      title='Top 10 Variáveis Mais Influentes',
                      color_discrete_sequence=px.colors.qualitative.Pastel)
    fig_imp.update_layout(plot_bgcolor="#09000e", paper_bgcolor="#09000e", font_color='#e0e0ff',
                          title_font_family="Orbitron", title_font_color="#00ffff")
    fig_imp.update_xaxes(showgrid=False, title_text="Impacto na Previsão")
    fig_imp.update_yaxes(title_text="Variável")
    st.plotly_chart(fig_imp, use_container_width=True)
    st.markdown("""
        <div style="text-align: center; color: #8888aa; font-style: italic;">
            Clientes com maior tempo de contrato e planos anuais tendem a ter menor probabilidade de evasão.
        </div>
    """, unsafe_allow_html=True)


st.markdown("---")

# ====================================================================
# Seção 3: Visualizações Detalhadas (Com Abas)
# ====================================================================
st.header('📈 Visualizações Interativas')
st.write('Navegue pelas abas para explorar a distribuição de dados.')

if df_raw is not None:
    tab1, tab2, tab3 = st.tabs(["Tempo de Contrato", "Gasto Total", "Matriz de Correlação"])

    with tab1:
        fig_tenure = px.box(df_raw,
                              x='Churn',
                              y='customer_tenure',
                              color='Churn',
                              color_discrete_map=CHURN_COLORS,
                              title='Distribuição de Tempo de Contrato por Evasão')
        fig_tenure.update_layout(plot_bgcolor='#09000e', paper_bgcolor='#09000e', font_color='#e0e0ff',
                                  title_font_family="Orbitron", title_font_color="#00ffff")
        st.plotly_chart(fig_tenure, use_container_width=True)

    with tab2:
        fig_total_charges = px.box(df_raw,
                                     x='Churn',
                                     y='account_Charges.Total',
                                     color='Churn',
                                     color_discrete_map=CHURN_COLORS,
                                     title='Distribuição de Gasto Total por Evasão')
        fig_total_charges.update_layout(plot_bgcolor='#09000e', paper_bgcolor='#09000e', font_color='#e0e0ff',
                                         title_font_family="Orbitron", title_font_color="#00ffff")
        st.plotly_chart(fig_total_charges, use_container_width=True)

    with tab3:
        corr_matrix = df_encoded.corr()
        fig_corr = px.imshow(corr_matrix,
                              labels=dict(x="Variáveis", y="Variáveis", color="Correlação"),
                              x=corr_matrix.columns,
                              y=corr_matrix.columns,
                              color_continuous_scale=PLOTLY_CMAP,
                              title='Matriz de Correlação Interativa')
        fig_corr.update_layout(plot_bgcolor='#09000e', paper_bgcolor='#09000e', font_color='#e0e0ff',
                                 title_font_family="Orbitron", title_font_color="#00ffff")
        st.plotly_chart(fig_corr, use_container_width=True)

st.markdown("---")

# ====================================================================
# Seção 4: Previsão de Novo Cliente (Funcionalidade Extra)
# ====================================================================
st.header('🔮 Módulo de Previsão')
st.write('Insira os dados de um cliente para obter uma previsão de risco de evasão em tempo real.')

if model and scaler and feature_columns:
    colunas_numericas = ['customer_tenure', 'account_Charges.Monthly', 'account_Charges.Total']
    
    with st.form("churn_prediction_form"):
        st.subheader("Entrada de Dados do Cliente")
        col1, col2 = st.columns(2)
        with col1:
            tenure = st.slider('Tempo de Contrato (meses)', min_value=1, max_value=72, value=12)
            monthly_charges = st.slider('Gasto Mensal', min_value=18.0, max_value=118.0, value=70.0)
            contract = st.selectbox('Tipo de Contrato', ['month-to-month', 'one year', 'two year'])
        with col2:
            total_charges = st.number_input('Gasto Total', min_value=0.0, value=1000.0)
            internet_service = st.selectbox('Serviço de Internet', ['dsl', 'fiber optic', 'no internet service'])
            online_security = st.selectbox('Segurança Online (1=Sim, 0=Não)', [0, 1])
            tech_support = st.selectbox('Suporte Técnico (1=Sim, 0=Não)', [0, 1])

        submitted = st.form_submit_button("Analisar Cliente 🚀")

        if submitted:
            input_data = pd.DataFrame([{
                'customer_tenure': tenure,
                'account_Charges.Monthly': monthly_charges,
                'account_Charges.Total': total_charges,
                'internet_OnlineSecurity_Yes': online_security,
                'internet_TechSupport_Yes': tech_support,
                'account_Contract_One year': 1 if contract == 'one year' else 0,
                'account_Contract_Two year': 1 if contract == 'two year' else 0,
                'internet_InternetService_Fiber optic': 1 if internet_service == 'fiber optic' else 0,
                'internet_InternetService_No internet service': 1 if internet_service == 'no internet service' else 0,
            }])

            for col in feature_columns:
                if col not in input_data.columns:
                    input_data[col] = 0

            input_data[colunas_numericas] = scaler.transform(input_data[colunas_numericas])

            churn_prediction = model.predict(input_data[feature_columns])
            churn_prob = model.predict_proba(input_data[feature_columns])[0][1]

            if churn_prediction[0] == 1:
                st.error(f'ALERTA: Este cliente tem alta probabilidade de evasão! Probabilidade: **{churn_prob:.2f}**')
            else:
                st.success(f'RELATÓRIO: Este cliente tem baixa probabilidade de evasão. Probabilidade: **{churn_prob:.2f}**')

else:
    st.warning("Não foi possível carregar os recursos necessários. Verifique se os arquivos `.pkl` existem.")
