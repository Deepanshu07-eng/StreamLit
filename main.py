import streamlit as st

st.title("Hello App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("Choose your option")

Play = st.selectbox("Your Fav Game:", ["Cricket","Volley Ball","Hockey","Football","UNO"])