# arena-media-agent-template
# Arena Media Agent Template

This repository is designed for Arena AI (Agent Mode) to autonomously download, transcribe, and translate video audio streams.

## Features
- Audio extraction from video URLs using `yt-dlp`
- Native speech-to-text processing using `openai-whisper`

## Instructions for Arena Agent
1. Install the required dependencies: `pip install -r requirements.txt`
2. Create and run a Python script to download the video audio track.
3. Use the Whisper engine to listen to the target language and translate it directly to English text.
