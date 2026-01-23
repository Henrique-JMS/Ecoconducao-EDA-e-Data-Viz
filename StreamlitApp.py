import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Ecocondução - Análise Exploratória", layout="wide")

st.title("Ecocondução, Hábitos e Eficiência de Combustível: Uma Análise Exploratória")

st.markdown(
"""
Este projeto apresenta uma **Análise Exploratória de Dados (EDA)** sobre ecocondução,
explorando a relação entre comportamento de condução, consumo de combustível
e eficiência energética.


Os resultados aqui apresentados são complementares ao notebook técnico do projeto
e têm como foco **visualização e interpretação dos dados**.

Acesse o notebook em: 
"""
)

plt.style.use('ggplot')

df = pd.read_csv('eco_driving_score.csv')

bins = [0, 40, 70, 100]
labels = ["Ruim", "Mediano", "Bom"]


df["eco_category"] = pd.cut(
df["eco_score"],
bins=bins,
labels=labels,
include_lowest=True
)

st.header("Visão Geral do Dataset")

st.markdown(
"""
| Coluna                  | Descrição                                                |
|-------------------------|----------------------------------------------------------|
| rpm_variation           | Grau de variação da rotação do motor durante a condução. |
| harsh_braking_count     | Número de eventos de frenagem brusca.                    |
| idling_time             | Tempo total com o veículo em marcha lenta.               |
| fuel_consumption        | Consumo de combustível no período analisado.             |
| acceleration_smoothness | Nível de suavidade nas acelerações do veículo.           |
| eco_score               | Pontuação de eficiência da condução (0 a 100).           |
| eco_category            | Categoria de cada motorista baseado no eco_score         |
"""
)

st.markdown("**Amostra dos dados:**")
st.dataframe(df.head())


st.markdown("**Resumo estatístico:**")
st.dataframe(df.describe())

st.header("Distribuição do Eco Score")


fig, ax = plt.subplots()
sns.histplot(df["eco_score"], bins=20, kde=True, ax=ax)
ax.set_xlabel("Eco Score")
ax.set_ylabel("Frequência")
ax.set_title("Distribuição do Eco Score")
st.pyplot(fig, width=600)

st.header("Segmentação por Categoria de Ecocondução")


col1, col2 = st.columns(2)

with col1:
    st.markdown("**Quantidade de motoristas por categoria:**")
    st.dataframe(df["eco_category"].value_counts())


with col2:
    st.markdown("**Consumo médio de combustível por categoria:**")
    st.dataframe(
        df.groupby("eco_category")["fuel_consumption"].mean().round(2)
)

fig, ax = plt.subplots()
df['eco_category'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
ax.set_ylabel(" ")
ax.set_title("Contagem de categorias")
st.pyplot(fig, width=600)

st.header("Comparação de Métricas por Categoria")


features = [
    "fuel_consumption",
    "harsh_braking_count",
    "rpm_variation",
    "idling_time",
    "acceleration_smoothness"
]


selected_feature = st.selectbox(
    "Selecione a métrica para visualização",
    features
)


fig, ax = plt.subplots()
sns.boxplot(
    data=df,
    x="eco_category",
    y=selected_feature,
    ax=ax
)
ax.set_xlabel("Categoria de Ecocondução")
ax.set_ylabel(selected_feature.replace("_", " ").title())
ax.set_title(f"{selected_feature.replace('_', ' ').title()} por Categoria")
st.pyplot(fig, width=600)

st.markdown("- Gráfico de violino entre Consumo de combustivel e Categoria")

fig, ax = plt.subplots(figsize=(6, 4))
sns.violinplot(x=df.eco_category, y=df.fuel_consumption, inner='quartile', color='lightgreen', ax=ax)
ax.set_xlabel('Categoria Eco')
ax.set_ylabel('Consumo de combustivel')
st.pyplot(fig, width=600)

st.header("Análise de Correlação")

corr = df[[
"eco_score",
"acceleration_smoothness",
"idling_time",
"rpm_variation",
"harsh_braking_count",
"fuel_consumption"
]].corr()


fig, ax = plt.subplots(figsize=(7, 5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='seismic', ax=ax)
ax.set_title("Matriz de Correlação")
st.pyplot(fig, width=600)


st.header("Conclusões")


st.markdown(
"""
- Motoristas classificados na categoria `Bom` apresentaram um consumo médio de combustível **19,4%** menor em relação aos motoristas da categoria `Mediano` e **33,6%** menor quando comparados aos da categoria `Ruim`
- A **frenagem brusca** é o comportamento mais negativamente associado ao *eco_score*.
- A **suavidade de aceleração** é o hábito mais fortemente associado a uma condução eficiente.


Os resultados reforçam a importância de práticas de direção suaves e antecipatórias
para a redução do consumo de combustível e melhoria da eficiência energética.
"""
)

st.markdown(
"""
Fonte do dataset: https://www.kaggle.com/datasets/sonalshinde123/eco-driving-behavior-dataset/data
"""
)

st.caption("Projeto de Análise Exploratória de Dados – Ecocondução")