import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

df = pd.read_csv("bank.csv")

st.title("Analyse de bank.csv")

# Distribution de l'âge

st.subheader("Histogramme de distribution de l'âge des clients")
fig1 = px.histogram(df, x='age', nbins=10)
fig1.update_layout(
    xaxis_title="Age des clients",
    yaxis_title="Nombre de clients",
    title_text="Histogramme de distribution de l'âge des clients",
    legend_title_text="Groupe d'âge",
    bargap=0.1
)
st.plotly_chart(fig1)

# Répartition par statut marital

st.subheader("Histogramme de Répartition par statut marital")
fig2 = px.histogram(df, x='marital', nbins=3)
fig2.update_layout(
    xaxis_title="Statut marital",
    yaxis_title="Nombre de clients",
    title_text="Histogramme de Répartition par statut marital",
    legend_title_text="Répartition marital",
    bargap=0.1
)
st.plotly_chart(fig2)

# Répartition par niveau d'éducation

st.subheader("Histogramme de Répartition par niveau d'éducation")
fig3 = px.histogram(df, x='education', nbins=4)
fig3.update_layout(
    xaxis_title="Niveau d'éducation",
    yaxis_title="Nombre de clients",
    title_text="Histogramme de Répartition par niveau d'éducation",
    legend_title_text="Répartition niveau d'éducation",
    bargap=0.1
)
st.plotly_chart(fig3)

# Répartition des soldes

st.subheader("Histogramme de Répartition par solde sur le compte")
fig4 = px.histogram(df, x='balance', nbins=5)
fig4.update_layout(
    xaxis_title="Solde sur le compte",
    yaxis_title="Nombre de clients",
    title_text="Histogramme de Répartition par solde sur le compte",
    legend_title_text="Répartition par solde sur le compte",
    bargap=0.1,
    xaxis_tickprefix="€"
)
st.plotly_chart(fig4)

# Répartition des soldes en fonction de l'âge, du statut marital, et le niveau d'éducation

st.subheader("Histogramme de Répartition des soldes en fonction de l'âge, du statut marital, et le niveau d'éducation")
balance_moyenne_all = df.groupby(['education', 'marital'])['balance'].mean().reset_index()
fig5 = px.bar(balance_moyenne_all, x='education', y='balance', color = 'marital', barmode ='group')
fig5.update_layout(
    xaxis_title="Niveau d'éducation",
    yaxis_title="Solde moyen ",
    title_text="Solde moyen par niveau d'éducation",
    yaxis_tickprefix="€",  # Ajout du symbole de l'euro pour le solde
    legend_title_text='Statut marital'
)
st.plotly_chart(fig5)

# Comparaison du solde prêt immo ou non
moyenne_balance_housing = df.groupby('housing')['balance'].mean().reset_index()

st.subheader("Histogramme de Répartition du solde par prêt")
fig6 = px.histogram(moyenne_balance_housing, x='housing',y='balance')
fig6.update_layout(
    xaxis_title="Prêt engagé ou non",
    yaxis_title="Solde sur le compte",
    title_text="Histogramme de Répartition du solde par prêt",
    bargap=0.1,
)
st.plotly_chart(fig6)

# Analyse de la durée des appels

st.subheader("Histogramme de Répartition des durées d'appels de la campagne Marketing")
fig7 = px.histogram(df, x='duration')
fig7.update_layout(
    xaxis_title="Durée de l'appel",
    yaxis_title="Nombre d'appels",
    title_text="Histogramme de Répartition des durées d'appels de la campagne Marketing",
    bargap=0.1,
)
st.plotly_chart(fig7)

# Analyse de la campagne par mois
nb_contact_mois = df['month'].value_counts().reset_index()
nb_contact_mois.columns = ['month', 'count']

month_order = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
nb_contact_mois['month'] = pd.Categorical(nb_contact_mois['month'], categories=month_order, ordered=True)
contacts_by_month = nb_contact_mois.sort_values('month')

st.subheader("Histogramme du nombre de contacts de la campagne marketing par mois")
fig8 = px.bar(contacts_by_month, x='month', y='count')

# Personnalisation des légendes
fig8.update_layout(
    xaxis_title="Mois",
    yaxis_title="Nombre de contacts",
    title_text="Histogramme du nombre de contacts de la campagne marketing par mois",
)

# Affichage du graphique
st.plotly_chart(fig8)

# Proportion de souscription par groupe

# Répartition des soldes en fonction du statut marital, et le niveau d'éducation

# Calculer le taux de souscription par niveau d'éducation et statut marital
deposit_summary = df.groupby(['education', 'marital', 'deposit']).size().reset_index(name='count')
total_summary = df.groupby(['education', 'marital']).size().reset_index(name='total')
deposit_summary = pd.merge(deposit_summary, total_summary, on=['education', 'marital'])
deposit_summary['proportion'] = deposit_summary['count'] / deposit_summary['total']

st.subheader("Histogramme de Répartition des soldes en fonction du statut marital, et le niveau d'éducation")
# Création du graphique à barres groupées
fig9 = px.bar(deposit_summary, x='education', y='proportion', color='deposit', barmode='group', facet_col='marital', title="Proportion de souscription par niveau d'éducation et statut marital")

# Personnalisation des légendes
fig9.update_layout(
    xaxis_title="Niveau d'éducation",
    yaxis_title="Proportion de souscription",
    title_text="Proportion de souscription par niveau d'éducation, statut marital et âge",
    legend_title_text='Souscription'
)
st.plotly_chart(fig9)







