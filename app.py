import streamlit as st
import yt_dlp

st.title("Video Downloader")

video_url = st.text_input("Enter video URL")

if video_url:
    st.write("Fetching video details...")
    with yt_dlp.YoutubeDL() as ydl:
        video_info = ydl.extract_info(video_url, download=False)
        st.write(video_info)