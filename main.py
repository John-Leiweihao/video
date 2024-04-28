import streamlit as st
st.set_page_config(page_title="PE-GPT", page_icon="💎", layout="centered",
                   initial_sidebar_state="auto", menu_items=None)

st.markdown(
        """
        ## PE-GPT
        """
    )
st.title("PE-GPT🤖")
import streamlit as st
video_file1 = open('DesignCase1.mp4', 'rb')
video_bytes1 = video_file1.read()

st.video(video_bytes1)

video_file2 = open('DesignCase2.mp4', 'rb')
video_bytes2 = video_file2.read()

st.video(video_bytes2)
