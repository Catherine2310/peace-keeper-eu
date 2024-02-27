import streamlit as st
import pandas as pd
import numpy as np

st.title('Peace Keeper')

# Spécifiez le chemin vers votre fichier CSV
chemin_fichier = r'C:\Users\cfran\OneDrive\Documents\MBA IA\Python\Airline Dataset Updated - v2.csv'

# Chargez les données dans un DataFrame pandas
donnees = pd.read_csv(chemin_fichier)

# Affichez les premières lignes pour vérifier
print(donnees.head())

   
# Fonction pour la page d'accueil
def page_accueil():
    st.title("Page d'accueil")
    st.write("Bienvenue sur la page d'accueil.")

# Fonction pour la page de contact
def page_contact():
    st.title("Informations par pays")
    st.write("Bienvenue sur Informations par pays.")

# Ajout des options dans la sidebar pour la navigation
page = st.sidebar.selectbox("Choisir une page :", ["Accueil", "Informations par pays"])

# Logique de navigation
if page == "Accueil":
    page_accueil()
elif page == "Informations par pays":
    page_contact()
