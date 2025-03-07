import streamlit as st
from pytubefix import YouTube
from functions import duration_show

st.title("Video Downloader")

if "stat" not in st.session_state:
    st.session_state.stat = False


tab1, tab2 = st.tabs(["Single Video download", "Playlist download"])

with tab1:
    video_url = st.text_input("Enter video URL")
    search_btn = st.button("Search video")
    if search_btn:
        st.session_state.stat = True
    if video_url == "": st.session_state.stat = False
    if st.session_state.stat:
            yt = YouTube(video_url)
            st.image(yt.thumbnail_url)
            st.write(yt.title)
            st.write(duration_show(yt.length))
            
            # Build Resolutions
            resolutions = [stream.resolution for stream in yt.streams.filter(adaptive=True)]
            
            # Filter and arrange
            cleaned_resolutions = []
            seen_none = False
            for res in resolutions:
                if res == "None":
                    if not seen_none:
                        cleaned_resolutions.append(res)
                        seen_none = True
                else:
                    if res not in cleaned_resolutions:
                        cleaned_resolutions.append(res)
            sorted_resolutions = sorted(cleaned_resolutions[1:], key=lambda x: int(x.replace('p', '')) if x else 0)
            if "None" in resolutions:
                sorted_resolutions.insert(0, "None")
            select_resolution = st.selectbox("Select Video Quality", sorted_resolutions)
            download_btn = st.button("Download")
            if download_btn and select_resolution != "None":
                yt.streams.filter(adaptive=True, resolution=select_resolution).first().download(output_path="downloads")
                st.success("Downloaded successfully")
            elif download_btn and select_resolution == "None":
                st.error("Select a resolution")
            
        # except Exception as e:
        #     st.error("Invalid video URL")
        #     st.session_state.stat = False
    
with tab2:
    st.write("Playlist download")
