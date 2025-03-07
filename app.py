import streamlit as st 
from pytube import YouTube

st.title("Video Downloader")

url = st.text_input("Enter the video URL")

if url:
    yt = YouTube(url)
    st.write("Title:", yt.title)
    st.image(yt.thumbnail_url)