import streamlit as st 
from pytube import YouTube

st.title("Video Downloader")

url = st.text_input("Enter the video URL")
check = st.button("Check")


if check and url !="":
    try:
        with st.spinner("Wait for it...", show_time=True):
            yt = YouTube(url)
        st.success("Done!")
        st.write("Title:", yt.title)
        st.image(yt.thumbnail_url)
    except Exception as e:
        st.write(e)