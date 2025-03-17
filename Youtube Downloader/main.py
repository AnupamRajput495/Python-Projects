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