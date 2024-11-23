import streamlit as st
import pandas as pd
import numpy as np

# Titre de l'application
st.title("Exemple avec Streamlit")

# Afficher un texte
st.write("Ceci est une application Streamlit simple.")

# Ajouter un curseur interactif
slider_val = st.slider("Choisissez un nombre :", 0, 100)

# Calcul basé sur l'entrée utilisateur
st.write(f"Le carré de {slider_val} est {slider_val ** 2}.")

# Charger des données fictives
data = pd.DataFrame({
    'x': np.arange(1, 101),
    'y': np.random.randint(1, 101, 100)
})

# Afficher un graphique interactif
st.line_chart(data)

#Lien de l'appli
#http://localhost:8501
#http://192.168.47.153:8501
