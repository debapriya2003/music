---

# 🎵 YouTube Music Streamer (Streamlit App)

## Overview

**YouTube Music Streamer** is a lightweight Python web application built with **Streamlit** that allows users to search for songs on YouTube and instantly stream their audio without downloading the video. The app uses the **YouTube Data API v3** to fetch music-related videos and **yt-dlp** to extract and stream high-quality audio in real time.

This project demonstrates how to combine third-party APIs, media extraction tools, and rapid UI development to create a functional music streaming experience directly in the browser.

---

## Key Features

* 🔍 **YouTube Music Search**

  * Search for songs, artists, or tracks using natural text queries
  * Fetches the top relevant music videos from YouTube

* 🎧 **Real-Time Audio Streaming**

  * Streams audio directly from YouTube without downloading files
  * Uses `yt-dlp` to extract the best available audio format

* 🖼️ **Thumbnail Preview**

  * Displays high-quality video thumbnails for visual context

* ⚡ **Fast & Lightweight UI**

  * Built with Streamlit for instant rendering and responsiveness
  * No complex frontend frameworks required

* 🔐 **Secure API Key Handling**

  * Uses environment variables (`.env`) to protect the YouTube API key

---

## How It Works

1. The user enters a song or artist name in the search box.
2. The app queries the **YouTube Data API v3** to retrieve matching video results.
3. For each result:

   * The video title and thumbnail are displayed
   * `yt-dlp` extracts the direct audio stream URL
4. Streamlit’s audio player streams the music instantly in the browser.

This approach avoids video downloads and focuses purely on audio playback.

---

## Tech Stack

* **Frontend / UI:** Streamlit
* **Backend Logic:** Python
* **APIs:** YouTube Data API v3
* **Media Extraction:** yt-dlp
* **Environment Management:** python-dotenv

---

## Project Structure

```
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## Environment Setup

Create a `.env` file in the project root:

```
YOUTUBE_API_KEY=your_youtube_api_key_here
```

Make sure the YouTube Data API v3 is enabled in your Google Cloud Console.

---

## Installation & Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Use Cases

* Quick music streaming without opening YouTube
* Learning project for API integration and media streaming
* Demonstration of `yt-dlp` usage in real-time applications
* Prototype for music-based web apps

---

## Limitations

* Dependent on YouTube API quotas
* Streaming availability depends on YouTube video restrictions
* Not intended for commercial music distribution

---

## Educational Purpose

This project is built for **learning and experimentation**, showcasing:

* API consumption
* Audio extraction pipelines
* Rapid app development with Streamlit

It is **not affiliated with or endorsed by YouTube**.

---

## Future Improvements

* Playlist support
* Search filters (artist, duration, popularity)
* Playback queue
* UI enhancements and dark mode
* Lyrics integration

---

## Conclusion

**YouTube Music Streamer** is a simple yet powerful example of how Python, Streamlit, and modern media tools can be combined to build an interactive music streaming experience. It emphasizes clarity, speed, and educational value while remaining easy to extend and customize.

---
