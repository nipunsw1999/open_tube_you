import streamlit as st
from pytubefix import YouTube
from functions import duration_show
from urllib.error import HTTPError

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
        try:
            yt = YouTube(video_url)

            # Display video details
            st.image(yt.thumbnail_url)
            st.write(f"**Title:** {yt.title}")
            st.write(f"**Duration:** {duration_show(yt.length)}")

            # Fetch available resolutions (adaptive)
            resolutions = [stream.resolution for stream in yt.streams.filter(adaptive=True) if stream.resolution]

            # Remove duplicates and sort
            unique_resolutions = sorted(set(resolutions), key=lambda x: int(x.replace('p', '')) if x else 0)

            if unique_resolutions:
                select_resolution = st.selectbox("Select Video Quality", unique_resolutions)
                download_btn = st.button("Download")

                if download_btn:
                    try:
                        stream = yt.streams.filter(adaptive=True, resolution=select_resolution).first()

                        if stream:
                            stream.download(output_path="downloads")
                            st.success("Downloaded successfully!")
                        else:
                            st.error("Selected resolution is not available.")
                    
                    except HTTPError as e:
                        st.error(f"HTTP Error: {e.code} - {e.reason}")
                    
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
            else:
                st.error("No adaptive resolutions available.")
                
        except Exception as e:
            st.error("Invalid video URL or YouTube blocked the request.")
            st.session_state.stat = False

with tab2:
    st.write("Playlist Download (Coming Soon)")
