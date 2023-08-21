# YouTube Video Downloader

This is a simple Python script that allows you to download YouTube videos in various resolutions and optionally convert them to MP3 audio files.

## Requirements

To run this script, you need to have the following Python libraries installed:

- pytube
- pydub
- Make sure you have the `ffmpeg` binary available in your system's PATH, as pydub relies on it for audio conversion

## Usage

1. Download the Python script and save it to a directory.
2. Open a terminal (or command prompt) and navigate to the directory where the script is located.
3. Run the following command:

   ```bash
   python youtube_downloader.py
   ```

4. Follow the on-screen prompts to download YouTube videos or MP3 files.

## Features

- Download YouTube videos in various resolutions (low, medium, high, very high).
- Download multiple videos at once by providing comma-separated links.
- Option to convert downloaded videos to MP3 audio files.
