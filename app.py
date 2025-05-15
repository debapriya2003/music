
import streamlit as st
import requests
import yt_dlp
import os
from dotenv import load_dotenv

load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
def search_youtube_music(query):
    api_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': 5,
        'key': YOUTUBE_API_KEY
    }
    response = requests.get(api_url, params=params)
    return response.json().get('items', [])

def get_audio_url(video_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'extract_flat': False,
        'forceurl': True,
        'noplaylist': True,
        'skip_download': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        return info['url'], info.get('thumbnail')

st.set_page_config(page_title="YouTube Music Player", layout="centered")
st.title("🎵 YouTube Music Streamer")

query = st.text_input("Search for a song...", placeholder="e.g. Calm Down Rema")

if query:
    results = search_youtube_music(query)
    for video in results:
        title = video['snippet']['title']
        video_id = video['id']['videoId']
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        thumbnail = video['snippet']['thumbnails']['high']['url']

        st.markdown(f"### {title}")
        st.image(thumbnail, width=300)

        try:
            with st.spinner("Fetching audio..."):
                audio_url, _ = get_audio_url(video_url)
                st.audio(audio_url, format="audio/mp4")
        except Exception as e:
            st.error(f"❌ Could not stream audio.")
