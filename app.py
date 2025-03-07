import streamlit as st
from pytubefix import YouTube

st.title("Video Downloader")

tab1, tab2 = st.tabs(["Single Video download", "Playlist download"])

with tab1:
    video_url = st.text_input("Enter video URL")
    if video_url:
        select_resolution = st.selectbox("Select resolution", ["1080", "720", "480", "360"])
        download_btn = st.button("Download video")
        if select_resolution:
            pass
            
        if download_btn:
                st.success("Video Download Success")

with tab2:
    st.write("Playlist download")
