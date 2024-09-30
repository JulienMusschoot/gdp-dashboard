import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

df = pd.read_csv("bank.csv")

st.title("Analyse de bank.csv")
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Aller à", ["Analyse Campagne Marketing", "Analyse Données Démographiques", "Analyse Variable 'deposit'","Analyse Variable 'Default'" ,"Analyse de la variable 'balance'","Analyse de la variable 'duration'", "Analyse de la variable 'solde'", "Crédits"])

if selection == "Analyse Campagne Marketing":
    st.title("Analyse de la campagne Marketing")
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

    st.title("Analyse de la variable 'duration'")
    fig30 = go.Figure()
    fig30.add_trace(go.Box(
        x=df["duration"],
        name="Duration (min)",
        marker_color="#222A2A",
        opacity=0.7
    ))
    fig30.update_layout(
        title="Distribution de la variable duration",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )
    st.plotly_chart(fig30)
elif selection == "Analyse Données Démographiques":
    st.title("Données Démographiques")
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

    # Distribution de l'âge
    st.subheader("Distribution de la variable Age")
    fig24 = go.Figure()
    fig24.add_trace(go.Box(
    x=df["age"],
    name="Âge",
    marker_color="#222A2A",
    opacity=0.7
    ))
    fig24.update_layout(
    title="Distribution de la variable âge",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=False),
    yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )
    st.plotly_chart(fig24)

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

    # Répartition par niveau d'éducation

    st.subheader("Distribution de la variable education par job")
    colors = ["#19D3F3", "#4B4B4B", "#1E90FF", "#060808"]

    category_order = ["primary", "secondary", "tertiary", "unknown"]

    fig25 = go.Figure()

    for i, education in enumerate(category_order):
        if education in df["education"].unique():
            fig25.add_trace(go.Histogram(
                x=df[df["education"] == education]["job"],
                name=education,
                marker_color=colors[i],
                opacity=0.7
            ))

    fig25.update_layout(
    title="Distribution de la variable education par job",
    xaxis_title="Job",
    yaxis_title="Nombre de clients",
    barmode="group",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=False),
    yaxis=dict(gridcolor="rgba(210,210,210,0.5)"),
    showlegend=True
    )

    st.plotly_chart(fig25)
elif selection == "Analyse Variable 'deposit'":
    st.title("Analyse Variable 'deposit'")

    st.subheader("Distribution de la variable deposit")

    fig29= go.Figure()


    counts = df['deposit'].value_counts()

    fig29.add_trace(go.Bar(
        x=counts.index,
        y=counts.values,
        marker_color=['#19D3F3', '#4B4B4B'],
        opacity=0.7
    ))

    fig29.update_layout(
        title="Distribution des dépôts",
        xaxis_title="Dépôt",
        yaxis_title="Nombre de clients",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)"),
        showlegend=False
    )
    st.plotly_chart(fig29)

    st.subheader("Histogramme de Souscription au dépôt selon l'âge du client")

    # Histogramme deposit / âge du client
    fig10 = go.Figure()

    fig10.add_trace(go.Histogram(
        x=df[df["deposit"] == "no"]["age"],
        name="No",
        marker_color="#222A2A",
        opacity=0.7,
        nbinsx=75
    ))

    fig10.add_trace(go.Histogram(
        x=df[df["deposit"] == "yes"]["age"],
        name="Yes",
        marker_color="#19D3F3",
        opacity=0.7,
        nbinsx=75
    ))

    fig10.update_layout(
        title="Souscription au dépôt selon l'âge du client",
        xaxis_title="Âge",
        yaxis_title="Nombre de clients",
        barmode="group",
        legend_title="Souscription",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )

    st.plotly_chart(fig10)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------


    # Histogramme deposit / job
    st.subheader("Histogramme de Souscription au dépôt selon l'emploi")

    fig11 = go.Figure()

    fig11.add_trace(go.Histogram(
        x=df[df["deposit"] == "no"]["job"],
        name="No",
        marker_color="#222A2A",
        opacity=0.7,
        nbinsx=12
    ))

    fig11.add_trace(go.Histogram(
        x=df[df["deposit"] == "yes"]["job"],
        name="Yes",
        marker_color="#19D3F3",
        opacity=0.7,
        nbinsx=12
    ))

    fig11.update_layout(
        title="Souscription au dépôt selon l'emploi",
        xaxis_title="Emploi",
        yaxis_title="Nombre de clients",
        barmode="group",
        legend_title="Souscription",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )

    st.plotly_chart(fig11)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------


    # Histogramme deposit / balance
    st.subheader("Souscription au dépôt selon les économies personnelles")

    fig12 = go.Figure()

    fig12.add_trace(go.Histogram(
        x=df[(df["deposit"] == "no") & (df["balance"] > -800) & (df["balance"] < 4000)]["balance"],
        name="No",
        marker_color="#222A2A",
        opacity=0.7,
        nbinsx=25
    ))

    fig12.add_trace(go.Histogram(
        x=df[(df["deposit"] == "yes") & (df["balance"] > -800) & (df["balance"] < 4000)]["balance"],
        name="Yes",
        marker_color="#19D3F3",
        opacity=0.7,
        nbinsx=25,
    ))

    fig12.update_layout(
        title="Souscription au dépôt selon les économies personnelles",
        xaxis_title="Balance",
        yaxis_title="Nombre de clients",
        barmode="group",
        legend_title="Souscription",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )

    st.plotly_chart(fig12)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------


    # Histogramme deposit / statut marital
    st.subheader("Souscription au dépôt selon le statut marital")

    fig13 = go.Figure()

    fig13.add_trace(go.Histogram(
        x=df[df["deposit"] == "no"]["marital"],
        name="No",
        marker_color="#222A2A",
        opacity=0.7,
        nbinsx=12
    ))

    fig13.add_trace(go.Histogram(
        x=df[df["deposit"] == "yes"]["marital"],
        name="Yes",
        marker_color="#19D3F3",
        opacity=0.7,
        nbinsx=12
    ))

    fig13.update_layout(
        title="Souscription au dépôt selon le statut marital",
        xaxis_title="Statut marital",
        yaxis_title="Nombre de clients",
        barmode="group",
        legend_title="Souscription",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )

    st.plotly_chart(fig13)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------


    # Histogramme deposit / education
    st.subheader("Souscription au dépôt selon le niveau d'études")

    fig14 = go.Figure()

    fig14.add_trace(go.Histogram(
        x=df[df["deposit"] == "no"]["education"],
        name="No",
        marker_color="#222A2A",
        opacity=0.7,
        nbinsx=12
    ))

    fig14.add_trace(go.Histogram(
        x=df[df["deposit"] == "yes"]["education"],
        name="Yes",
        marker_color="#19D3F3",
        opacity=0.7,
        nbinsx=12
    ))

    fig14.update_layout(
        title="Souscription au dépôt selon le niveau d'études",
        xaxis_title="Niveau d'études",
        yaxis_title="Nombre de clients",
        barmode="group",
        legend_title="Souscription",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )

    st.plotly_chart(fig14)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------


    # Histogramme deposit / prêt maison
    st.subheader("Souscription au dépôt selon si le client a un prêt immobilier")

    fig16 = go.Figure()

    fig16.add_trace(go.Histogram(
        x=df[df["deposit"] == "no"]["housing"],
        name="No",
        marker_color="#222A2A",
        opacity=0.7,
        nbinsx=30
    ))

    fig16.add_trace(go.Histogram(
        x=df[df["deposit"] == "yes"]["housing"],
        name="Yes",
        marker_color="#19D3F3",
        opacity=0.7,
        nbinsx=30
    ))

    fig16.update_layout(
        title="Souscription au dépôt selon si le client a un prêt immobilier",
        xaxis_title="A un prêt immobilier",
        yaxis_title="Nombre de clients",
        barmode="group",
        legend_title="Souscription",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )

    st.plotly_chart(fig16)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------


    # Histogramme deposit / prêt personnel
    st.subheader("Souscription au dépôt selon si le client a un prêt personnel")

    fig17 = go.Figure()

    fig17.add_trace(go.Histogram(
        x=df[df["deposit"] == "no"]["loan"],
        name="No",
        marker_color="#222A2A",
        opacity=0.7,
        nbinsx=30
    ))

    fig17.add_trace(go.Histogram(
        x=df[df["deposit"] == "yes"]["loan"],
        name="Yes",
        marker_color="#19D3F3",
        opacity=0.7,
        nbinsx=30
    ))

    fig17.update_layout(
        title="Souscription au dépôt selon si le client a un prêt personnel",
        xaxis_title="A un prêt personnel",
        yaxis_title="Nombre de clients",
        barmode="group",
        legend_title="Souscription",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )

    st.plotly_chart(fig17)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------


    # Histogramme deposit / nombre d'appels
    st.subheader("Souscription au dépôt selon le nombre d'appels")

    fig18 = go.Figure()

    fig18.add_trace(go.Histogram(
        x=df[df["deposit"] == "no"][df["campaign"] <= 8]["campaign"],
        name="No",
        marker_color="#222A2A",
        opacity=0.7,
        nbinsx=8
    ))

    fig18.add_trace(go.Histogram(
        x=df[df["deposit"] == "yes"][df["campaign"] <= 8]["campaign"],
        name="Yes",
        marker_color="#19D3F3",
        opacity=0.7,
        nbinsx=8
    ))

    fig18.update_layout(
        title="Souscription au dépôt selon le nombre d'appels",
        xaxis_title="Nombre d'appels",
        yaxis_title="Nombre de clients",
        barmode="group",
        legend_title="Souscription",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )

    st.plotly_chart(fig18)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------


    # Histogramme deposit / mois de l'appel

    #Création d'un ordre calendaire pour clarifier le graphique suivant
    month_order = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    df['month'] = pd.Categorical(df['month'], categories=month_order, ordered=True)
    df['month_numeric'] = df['month'].cat.codes

    st.subheader("Souscription au dépôt selon le mois de l'appel")

    fig19 = go.Figure()

    fig19.add_trace(go.Histogram(
        x=df[df["deposit"] == "no"]['month_numeric'],
        name="No",
        marker_color="#222A2A",
        opacity=0.7,
        nbinsx=len(month_order)
    ))

    fig19.add_trace(go.Histogram(
        x=df[df["deposit"] == "yes"]['month_numeric'],
        name="Yes",
        marker_color="#19D3F3",
        opacity=0.7,
        nbinsx=len(month_order)
    ))

    fig19.update_layout(
        title="Souscription au dépôt selon le mois de l'appel",
        xaxis_title="Mois de l'appel",
        yaxis_title="Nombre de clients",
        barmode="group",
        legend_title="Souscription",
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)"),
        xaxis=dict(showgrid=False, 
            tickvals=list(range(len(month_order))),
            ticktext=month_order
        )
    )

    st.plotly_chart(fig19)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------


    # Histogramme deposit / Nombre de contacts pré_campagne
    st.subheader("Souscription au dépôt selon le nombre de contacts avant cette campagne")

    fig20 = go.Figure()

    fig20.add_trace(go.Histogram(
        x=df[df["deposit"] == "no"][df["previous"]<10]["previous"],
        name="No",
        marker_color="#222A2A",
        opacity=0.7,
        nbinsx=10
    ))

    fig20.add_trace(go.Histogram(
        x=df[df["deposit"] == "yes"][df["previous"]<10]["previous"],
        name="Yes",
        marker_color="#19D3F3",
        opacity=0.7,
        nbinsx=10
    ))

    fig20.update_layout(
        title="Souscription au dépôt selon le nombre de contacts avant cette campagne",
        xaxis_title="Nombre de contacts pré-campagne",
        yaxis_title="Nombre de clients",
        barmode="group",
        legend_title="Souscription",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )

    st.plotly_chart(fig20)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------


    # Histogramme deposit / délai dernier contact
    st.subheader("Souscription au dépôt selon le délai depuis le dernier contact")

    fig21 = go.Figure()

    fig21.add_trace(go.Histogram(
        x=df[df["deposit"] == "no"]["pdays"],
        name="No",
        marker_color="#222A2A",
        opacity=0.7,
        nbinsx=10
    ))

    fig21.add_trace(go.Histogram(
        x=df[df["deposit"] == "yes"]["pdays"],
        name="Yes",
        marker_color="#19D3F3",
        opacity=0.7,
        nbinsx=10
    ))

    fig21.update_layout(
        title="Souscription au dépôt selon le délai depuis le dernier contact",
        xaxis_title="Nombre de jours depuis le dernier contact",
        yaxis_title="Nombre de clients",
        barmode="group",
        legend_title="Souscription",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )

    st.plotly_chart(fig21)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------


    # Histogramme deposit / Résultat de la campagne précédente
    st.subheader("Souscription au dépôt selon le résultat de la campagne précédente")

    fig22 = go.Figure()

    fig22.add_trace(go.Histogram(
        x=df[df["deposit"] == "no"]["poutcome"],
        name="No",
        marker_color="#222A2A",
        opacity=0.7,
        nbinsx=10
    ))

    fig22.add_trace(go.Histogram(
        x=df[df["deposit"] == "yes"]["poutcome"],
        name="Yes",
        marker_color="#19D3F3",
        opacity=0.7,
        nbinsx=10
    ))

    fig22.update_layout(
        title="Souscription au dépôt selon le résultat de la campagne précédente",
        xaxis_title="Résultat de la campagne précédente",
        yaxis_title="Nombre de clients",
        barmode="group",
        legend_title="Souscription",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )

    st.plotly_chart(fig22)

    #------------------------------------------------------------
    #------------------------------------------------------------
    #------------------------------------------------------------


    # Histogramme deposit / jour de l'appel
    st.subheader("Souscription au dépôt selon le jour de l'appel")

    fig23 = go.Figure()

    fig23.add_trace(go.Histogram(
        x=df[df["deposit"] == "no"]["day"],
        name="No",
        marker_color="#222A2A",
        opacity=0.7,
        nbinsx=31
    ))

    fig23.add_trace(go.Histogram(
        x=df[df["deposit"] == "yes"]["day"],
        name="Yes",
        marker_color="#19D3F3",
        opacity=0.7,
        nbinsx=31
    ))

    fig23.update_layout(
        title="Souscription au dépôt selon le jour de l'appel",
        xaxis_title="Jour de l'appel dans le mois",
        yaxis_title="Nombre de clients",
        barmode="group",
        legend_title="Souscription",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )

    st.plotly_chart(fig23)

    st.subheader("Distribution de la variable deposit par contact")
    colors = ["#19D3F3", "#4B4B4B"]

    fig28 = go.Figure()

    for response in ['no', 'yes']:
        fig28.add_trace(go.Histogram(
            x=df[df['deposit'] == response]['contact'],
            name=response,
            marker_color=colors[1] if response == 'yes' else colors[0],
            opacity=0.7
        ))

    fig28.update_layout(
        title="Distribution de la variable Deposit selon le type de Contact",
        xaxis_title="Type de Contact",
        yaxis_title="Nombre de Clients",
        barmode="group",
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(gridcolor="rgba(210,210,210,0.5)"),
        showlegend=True
    )
    st.plotly_chart(fig28)
elif selection == "Analyse de la variable 'solde'":
    st.title("Analyse Variable 'solde'")
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
elif selection == "Analyse de la variable 'Default'":
    st.title("Analyse Variable 'Default'")
    fig26 = go.Figure()

    counts = df['default'].value_counts()

    fig26.add_trace(go.Bar(
    x=counts.index,
    y=counts.values,
    marker_color=['#19D3F3', '#4B4B4B'],
    opacity=0.7
    ))

    fig26.update_layout(
    title="Distribution de default",
    xaxis_title="Default",
    yaxis_title="Nombre de clients",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=False),
    yaxis=dict(gridcolor="rgba(210,210,210,0.5)"),
    showlegend=False
    )
    st.plotly_chart(fig26)
elif selection == "Analyse de la variable 'balance'":
    st.title("Analyse Variable 'balance'")
    fig27 = go.Figure()
    fig27.add_trace(go.Box(
    x=df["balance"],
    name="Balance",
    marker_color="#222A2A",
    opacity=0.7
    ))
    fig27.update_layout(
    title="Distribution de la variable balance",
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=False),
    yaxis=dict(gridcolor="rgba(210,210,210,0.5)")
    )
    st.plotly_chart(fig27)
elif selection == "Crédits":
    st.title("Crédits")
    st.subheader("Participants au projet")
    st.write("""
    - Camille
    - Clément
    - Arnaud
    - Julien
    """)
    st.write("Projet réalisé par l'équipe dans le cadre de notre formation de Data Analyst.")





