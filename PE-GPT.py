import streamlit as st
st.set_page_config(page_title="PE-GPT", page_icon="💎", layout="centered",
                   initial_sidebar_state="auto", menu_items=None)


st.markdown(
    """
    <h2 style='font-size: 43px;'>PE-GPT🤖 : A New Paradigm for Power Electronics Design, Welcome!👋</h2>
    """,
    unsafe_allow_html=True
)
st.sidebar.success("Please select a demo above.")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image('PE-GPT logo.png', width=200)  # 设置图片宽度为300像素，可以根据需要调整
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
    ### Design Case 3 (analyzed in the manuscript): Circuit Design for Buck Converters
    - 1st user request: current and voltage ripples within respective boundaries, and high-power density
    - 2nd user request (PE-specific reasoning): rationale behind the designed circuit parameters, analysis of current and voltage harmonics
    - 3rd user request (Interact with simulation model): verify design in PLECS simulation
"""
)
