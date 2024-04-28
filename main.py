import streamlit as st
video_file1 = open('DesignCase1.mp4', 'rb')
video_bytes1 = video_file1.read()

st.video(video_bytes1)

video_file2 = open('DesignCase2.mp4', 'rb')
video_bytes2 = video_file2.read()

st.video(video_bytes2)
