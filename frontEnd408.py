# to run: go to project folder where Pipenv is and run: pipenv shell
# then run: streamlit run myfile.py
# to quit streamlit server: ctrl-c
# to exit environment enter "exit"
# to be able to interact with dataframe: pip install streamlit-aggrid


import streamlit as st
import pandas as pd
import numpy as np
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


st.set_page_config(page_title="Disney Dashboard",
                    layout="wide")



# ------------ SIDEBAR -------------

st.sidebar.header("Editing Menu")
addStuff = st.sidebar.button("Add to database")
delStuff = st.sidebar.button("Delete from database")
modStuff = st.sidebar.button("Update database")
rollBack = st.sidebar.button("Undo")

# ----- MAIN PAGE -----
st.title("Disney Dashboard")
st.markdown("##")

with st.expander("Filter data"):
    col1, col2, col3 = st.columns(3)
    with col1:
        park = st.multiselect(
            "Park:",
            options="M",
            default = "M"
        )
        section = st.multiselect(
            "Section:",
            options="M",
            default = "M"
        )
        location = st.multiselect(
            "Location:",
            options="M",
            default = "M"
        )
    with col2:
        restaurant = st.multiselect(
            "Restaurant:",
            options="M",
            default = "M"
        )
        ride = st.multiselect(
            "Ride:",
            options="M",
            default = "M"
        )
        utilities = st.multiselect(
            "Utilities:",
            options="M",
            default = "M"
        )
    with col3:
        shops = st.multiselect(
            "Shop:",
            options="M",
            default = "M"
        )
        shops = st.multiselect(
            "Filter:",
            options="M",
            default = "M"
        )
        shops = st.multiselect(
            "Filter2:",
            options="M",
            default = "M"
        )


st.write("Table here at some point smh")
# ------------- DATAFRAME ---------
data = pd.read_csv("main_Sections.csv", index_col=0)
AgGrid(data)
# ---------------------------------

if addStuff:
    st.write("Enter info below to add to table")
    col1, col2, col3 = st.columns(3)
    with col1:
        s1 = st.text_input("Enter park")
    with col2:
        s2 = st.text_input("Enter section")
    with col3:
        s3 = st.text_input("Enter location")


