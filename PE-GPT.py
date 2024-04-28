import streamlit as st
st.set_page_config(page_title="PE-GPT", page_icon="💎", layout="centered",
                   initial_sidebar_state="auto", menu_items=None)


st.write("# Power Electronics GPT (PE-GPT)🤖,Welcome!👋")
st.sidebar.success("Please select a demo above.")
st.markdown(
    """
    This repository presents demo videos of using "Power Electronics GPT (PEGPT)" for the modulation design of dual-active-bridge converters. Source codes will be open-sourced progressively.

    ### Design Case1 (analyzed in the manuscript)
    - 1st user request: minimal current stress  
    - 2nd user request (iterative design): extended soft switching ranges  
    - 3rd user request: fine-tuning of PANN by uploading few time-series samples  

    ### Design Case 2:
    - 1st user request: minimal current stress, full-range zero voltage switching, and relatively easy implementation  
    - 2nd user request (iterative design): enhanced current stress performance
"""
)
