import streamlit as st
st.set_page_config(page_title="PE-GPT", page_icon="💎", layout="centered",
                   initial_sidebar_state="auto", menu_items=None)


st.write("# PE-GPT🤖 : A New Paradigm for Power Electronics Design,Welcome!👋")
st.sidebar.success("Please select a demo above.")
st.markdown(
    """
    This repository presents demo videos of using "Power Electronics GPT (PE-GPT)" diverse design applications in power electronics. Source codes will be open-sourced progressively.
    """
)
#st.image('PE-GPT.png')
st.markdown( 
  """
  ### Design Case1 (analyzed in the manuscript):
    - 1st user request: minimal current stress  
    - 2nd user request (iterative design): extended soft switching ranges  
    - 3rd user request: fine-tuning of PANN by uploading few time-series samples  

    ### Design Case 2:
    - 1st user request: minimal current stress, full-range zero voltage switching, and relatively easy implementation  
    - 2nd user request (iterative design): enhanced current stress performance
"""
)
