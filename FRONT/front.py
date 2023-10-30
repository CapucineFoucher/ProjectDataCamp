import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define page functions
def homepage():
    st.title("Home Page")
    # Add presentation of the project 
    st.header("Presentation of the project")
    st.write("""
    In this project, our primary aim is to create a user-friendly web platform for early eye cancer detection. 
    We will preprocess a dataset of eye images, including resizing, normalization, and data partitioning. 
    Our cloud-based image classification model will focus on detecting eye cancer. Users can easily upload images for assessment. 
    Our goal is to showcase the power of cloud-based AI in medical image analysis and aid in early eye cancer detection.
    """)
    # Add graphics of the dataset 
    st.header("Graphical representation of the dataset")

    # Charger vos données (remplacez cela par votre propre méthode de chargement)
    df_test = pd.read_csv('../BACK/data/Test_Set/RFMiD_Testing_Labels.csv')

    # Comptez le nombre d'images par classe
    class_counts = df_test['Disease_Risk'].value_counts()

    # Créez le graphique
    fig, ax = plt.subplots(figsize=(10, 6))
    class_counts.plot(kind='bar', ax=ax)
    ax.set_title('Distribution of eye diseases in the test set')
    ax.set_xlabel('Disease Risk')
    ax.set_ylabel('Number of images')

    st.write(""" As we can see a lot of people are affected by eye diseases.
             That means that they might have a risk of eye cancer.
             So our app can be useful for people, to detect eye's diseases early and to be able to treat them. """)
    
    # Affichez le graphique dans Streamlit
    st.pyplot(fig)

    # Add explenation of the data cleaning 
    st.header("Data cleaning")

    st.write(""" For the data cleaning we decided to drop all the columns diseases that nobody had.""")

    st.write(""" Here's the correlation matrix before dropping empty columns:""")

    # Exclure les deux premières colonnes (ID et Disease_Risk) pour la matrice de corrélation
    correlation_df = df_test.iloc[:, 2:].astype(float)

    # Calculer la matrice de corrélation
    correlation_matrix = correlation_df.corr()

    # Créer une figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Tracer la matrice de corrélation sous forme de carte de chaleur
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".1f", ax=ax)

    # Afficher le graphique dans Streamlit
    st.pyplot(fig)

    st.write(""" Here's the correlation matrix after dropping empty columns:""")

    df_test_cleaned = pd.read_csv('../BACK/data/Test_Set/test_cleaned.csv')
    # Exclure les deux premières colonnes (ID et Disease_Risk) pour la matrice de corrélation
    correlation_df = df_test_cleaned.iloc[:, 2:].astype(float)

    # Calculer la matrice de corrélation
    correlation_matrix = correlation_df.corr()

    # Créer une figure
    fig, ax = plt.subplots(figsize=(12, 10))

    # Tracer la matrice de corrélation sous forme de carte de chaleur
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".1f", ax=ax)

    # Afficher le graphique dans Streamlit
    st.pyplot(fig)

    # Add presentation of the model 
    st.header("Presentation of the prediction model")

def detection_page():
    st.title("Upload Your Eye Image")

    # Upload an image
    uploaded_image = st.file_uploader("Upload an eye image", type=["jpg", "png", "jpeg"])

    # Check if an image has been uploaded
    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    ## add the machine learning part here


def about_page():
    st.title("About us")
    # Add prsentation of the team members
    st.header("Presentation of the team members")
    # Création des trois cadres
    col1, col2, col3 = st.columns(3)

    # Cadre pour la première personne
    with col1:
        st.image("pictures/capucine.png", use_column_width=True)  
        st.subheader("Capucine Foucher")
        st.write("Prediction Model + Contribution to Frontend")

    # Cadre pour la deuxième personne
    with col2:
        st.image("pictures/ariane.png", use_column_width=True)  
        st.subheader("Ariane Rousseau")
        st.write("Data Cleaning + Contribution to Frontend")

    # Cadre pour la troisième personne
    with col3:
        st.image("pictures/Anya.JPG", use_column_width=True)  
        st.subheader("Anya Tabti")
        st.write("Streamlit frontend")

    # Add project planing 


# Manage session state
if "page" not in st.session_state:
    st.session_state.page = "Home"  # Default to the home page

# Add navigation
page = st.selectbox("Select a page", ("Home", "Eye Disease", "About us"))

# Conditional page rendering
if page == "Home":
    homepage()
elif page == "Eye Disease":
    detection_page()
elif page == "About us":
    about_page()
