import os
import subprocess
import sys

def check_dependencies():
    """Ensure yt-dlp is available in the environment."""
    try:
        import yt_dlp
    except ImportError:
        print("Installing yt-dlp dependency...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
    
    try:
        import whisper
    except ImportError:
        print("Installing openai-whisper dependency...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "openai-whisper"])

def process_video(video_url):
    check_dependencies()
    import yt_dlp
    import whisper

    audio_filename = "downloaded_audio"
    output_audio = f"{audio_filename}.wav"
    
    # 1. Download audio track from YouTube link
    print(f"Downloading audio stream from: {video_url}")
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': audio_filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
            'preferredquality': '192',
        }],
        'quiet': False
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    
    # 2. Native speech-to-text handling using Whisper
    print("Initializing Whisper model to listen and translate...")
    # Using 'base' model for faster operational performance inside the agent container
    model = whisper.load_model("base")
    
    print("Processing audio tracks...")
    # Force language detection to Hungarian and leverage the 'translate' task flag to output English text
    options = {"language": "hu", "task": "translate"}
    result = model.transcribe(output_audio, **options)
    
    print("\n=== Translated English Lyrics Output ===")
    print(result["text"])
    print("=========================================\n")

if __name__ == "__main__":
    target_url = "https://youtube.com"
    process_video(target_url)
