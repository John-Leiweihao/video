import streamlit as st
st.set_page_config(page_title="PE-GPT", page_icon="💎", layout="centered",
                   initial_sidebar_state="auto", menu_items=None)
st.title("PE-GPT🤖-Design Case3")
video_file2 = open('DesignCase3.mp4', 'rb')
video_bytes2 = video_file2.read()

st.video(video_bytes2)
