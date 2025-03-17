# YouTube Video Downloader using yt-dlp 🎬

This Python script allows you to download YouTube videos or audio using `yt-dlp`, an advanced alternative to `pytube` that handles YouTube's restrictions more effectively.

## Features ✨
- Download videos in the best available quality 🎥
- Extract and download audio as MP3 🎵
- No YouTube restrictions (works even when `pytube` fails) ✅

## Installation 🛠️
Ensure you have Python installed (version 3.x recommended).

### 1️⃣ Install Dependencies
Run the following command to install `yt-dlp`:
```bash
pip install yt-dlp
```

## Usage 🚀
Run the script and follow the on-screen instructions.

### 2️⃣ Run the Script
```bash
python youtube_downloader.py
```

### 3️⃣ Enter YouTube Video URL
When prompted, enter the **YouTube video link** you want to download.

### 4️⃣ Choose Format
- **Press Enter** → Download the video in the best quality.
- **Type 'audio'** → Download only the audio in MP3 format.

## Code 📝
Here's the complete script:
```python
import yt_dlp

def download_video(url, audio_only=False):
    options = {
        'format': 'bestaudio' if audio_only else 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

video_url = input("🎬 Enter YouTube Video URL: ")
mode = input("🎵 Type 'audio' for MP3 or press Enter for Video: ").strip().lower()

if mode == "audio":
    download_video(video_url, audio_only=True)
else:
    download_video(video_url)
```

## Troubleshooting 🔧
**1. If you get an error, update `yt-dlp`:**
```bash
pip install --upgrade yt-dlp
```

**2. If downloading is slow, try using proxy settings in `yt-dlp`.**

## Contributing 🤝
Feel free to contribute by suggesting improvements or reporting issues!

## License 📜
This project is open-source and available under the **MIT License**.

---

Enjoy downloading! 🚀