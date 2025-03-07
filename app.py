import streamlit as st
from pytubefix import YouTube
from functions import duration_show
import time

st.title("Video Downloader")

if "stat" not in st.session_state:
    st.session_state.stat = False

tab1, tab2 = st.tabs(["Single Video Download", "Playlist Download"])

with tab1:
    video_url = st.text_input("Enter video URL")
    search_btn = st.button("Search Video")

    if search_btn:
        st.session_state.stat = True
    if video_url == "":
        st.session_state.stat = False

    if st.session_state.stat:
        yt = YouTube(video_url)
        st.image(yt.thumbnail_url)
        st.write(f"**Title:** {yt.title}")
        st.write(f"**Duration:** {duration_show(yt.length)}")
        # Fetch available resolutions (adaptive)
        streams = yt.streams.filter(adaptive=True)
        resolutions = [stream.resolution for stream in streams if stream.resolution]
        # Remove duplicates and sort
        unique_resolutions = sorted(set(resolutions), key=lambda x: int(x.replace('p', '')))
        
        # Select resolution
        select_resolution = st.selectbox("Select Video Quality", unique_resolutions)
        
        # Get file size of the selected resolution
        selected_stream = yt.streams.filter(adaptive=True, resolution=select_resolution).first()
        if selected_stream:
            file_size = selected_stream.filesize / (1024 * 1024)  # Convert bytes to MB
            st.write(f"**File Size:** {file_size:.2f} MB")
        # Download button
        download_btn = st.button("Download")
        if download_btn and selected_stream:
            with st.spinner("Downloading..."):
                st.write(time.time())
                selected_stream.download(output_path="downloads")
            st.success("Downloaded successfully!")

with tab2:
    st.write("Playlist Download (Coming Soon)")
