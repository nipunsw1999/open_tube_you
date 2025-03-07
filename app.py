import streamlit as st
import yt_dlp

st.title("Video Downloader")

tab1, tab2 = st.tabs(["Single Video download", "Playlist download"])

with tab1:
    video_url = st.text_input("Enter video URL")
    if video_url:
        select_resolution = st.selectbox("Select resolution", ["1080", "720", "480", "360"])
        download_btn = st.button("Download video")
        if select_resolution:
            # Use f-string for dynamic resolution
            ydl_opts = {
                'format': f'bestvideo[height={select_resolution}]+bestaudio/best[height={select_resolution}]',
                'merge_output_format': 'mp4',
            }
            
        if download_btn:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                video_info = ydl.extract_info(video_url, download=False)
                st.write(f"Video info: {video_info['title']}")
                ydl.download([video_url])
                st.success("Video Download Success")

with tab2:
    st.write("Playlist download")
