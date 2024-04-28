import streamlit as st
video_file = open('DesignCase2.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
