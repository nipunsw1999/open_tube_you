import streamlit as st
import yt_dlp

st.title("Video Downloader")


if 'video_info' not in st.session_state:
    st.session_state['video_info'] = None
    



tab1,tab2 = st.tabs(["Single Video download", "Playlist download"])
with tab1:
    video_url = st.text_input("Enter video URL")
    if video_url:
        select_resolution = st.selectbox(["1080","720","480","360"])
        if select_resolution:
            ydl_opts = {
                'format':'(bestvideo[height-{select_resolution}]+bestaudio)/',
                'merge_output_format': 'mp4',
            }
        with yt_dlp.YoutubeDL() as ydl:
            video_info = ydl.extract_info(video_url, download=False)
            ydl.download(video_url)
with tab2:
    st.write("Playlist download")