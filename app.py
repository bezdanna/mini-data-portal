import streamlit as st
import pandas as pd

# This MUST be the first Streamlit command right after your imports
st.set_page_config(layout="wide")

# The updated, foolproof way to hide all Streamlit branding
hide_styles = """
<style>
/* Hides the entire top decoration bar and menus */
[data-testid="stHeader"] {
    display: none !important;
}
/* Hides the default Streamlit footer at the bottom */
footer {
    visibility: hidden !important;
}
</style>
"""
st.markdown(hide_styles, unsafe_allow_html=True)

# 1. The Core Data Skeleton
raw_data = {
    "title": ["Inception", "Interstellar", "The Notebook", "Gladiator", "Superbad"],
    "genre": ["Sci-Fi", "Sci-Fi", "Romance", "Action", "Comedy"],
    "rating": [8.8, 8.6, 7.8, 8.5, 7.6],
    "year": [2010, 2014, 2004, 2000, 2007]
}
df = pd.DataFrame(raw_data)

# 2. The Website Title & Visual Elements
st.title("🎬 My Mini Data Portal")
st.write("This is a skeleton website connecting a Python filter to a web interface.")

# 3. Create the Interactive Dropdown Menu on the page
all_genres = ["All Open"] + list(df["genre"].unique())
selected_genre = st.selectbox("Filter by Genre:", all_genres)

# 4. The Filtering Connection
if selected_genre == "All Open":
    filtered_df = df
else:
    filtered_df = df[df["genre"] == selected_genre]

# 5. Display the final results dynamically on the screen
st.dataframe(filtered_df)