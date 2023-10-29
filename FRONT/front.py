import streamlit as st

# Define page functions
def homepage():
    st.title("Home Page")
    # Add presentation of the project 
    # Add graphics of the dataset 
    # Add explenation of the data cleaning 
    # Add presentation of the model 


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
    # Say who did what 
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
