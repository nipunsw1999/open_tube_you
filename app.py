import streamlit as st
import yt_dlp

st.title("Video Downloader")


if 'video_info' not in st.session_state:
    st.session_state['video_info'] = None
    
video_url = st.text_input("Enter video URL")

if video_url:
    st.write("Fetching video details...")
    with yt_dlp.YoutubeDL() as ydl:
        video_info = ydl.extract_info(video_url, download=False)
        col1, col2, col3 = st.columns([3,1,3])
        with col1:
            st.write("Title")
            st.write("Uploader")
            st.write("Duration")
        with col2:
            st.write(" - ")
            st.write(" - ")
            st.write(" - ")
        with col3:
            st.write(video_info['title'])
            st.write(video_info['uploader'])
            st.write(video_info['duration'])