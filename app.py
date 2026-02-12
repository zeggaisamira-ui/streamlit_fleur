import streamlit as st
import pandas as pd

df = pd.read_csv("comptes.csv")


import streamlit as st
import pandas as pd
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Album Fleurs", layout="wide")

# ===============================
# LECTURE DU CSV
# ===============================
df_users = pd.read_csv("comptes.csv")

credentials = {"usernames": {}}

for _, row in df_users.iterrows():
    credentials["usernames"][row["name"]] = {
        "name": row["name"],
        "password": row["password"],
        "email": row["email"],
        "failed_login_attemps": row["failed_login_attemps"],
        "logged_in": row["logged_in"],
        "role": row["role"],
    }

# ===============================
# AUTHENTIFICATION
# ===============================
authenticator = Authenticate(
    credentials,
    "cookie_fleur",
    "cle_secrete_fleur",
    30
)

authenticator.login(key="login_form_fleur")

# ===============================
# SI CONNECTÉ
# ===============================
if st.session_state["authentication_status"]:

    # SIDEBAR
    with st.sidebar:
        st.write(f"Bienvenue {st.session_state['name']}")

        selection = option_menu(
            menu_title="Menu",
            options=["Accueil", "Album des fleurs"],
            icons=["house", "image"],
            default_index=0
        )

        authenticator.logout("Déconnexion")

    # PAGE ACCUEIL
    if selection == "Accueil":
        st.title("Bienvenue sur ma page 🌸")
        st.write("Application sécurisée avec authentification.")

    # PAGE ALBUM
    if selection == "Album des fleurs":
        st.title("Mon album de fleurs 🌺")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("images.1.jpg")

        with col2:
            st.image("images.2.jpg")

        with col3:
            st.image("images.3.jpg")

# ===============================
# ERREURS LOGIN
# ===============================
elif st.session_state["authentication_status"] is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect")

elif st.session_state["authentication_status"] is None:
    st.warning("Veuillez entrer vos identifiants")

