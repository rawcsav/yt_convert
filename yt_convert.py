import pytube
from moviepy.editor import VideoFileClip
from typing import List

def convert_to_mp3(filename: str) -> None:
    clip = VideoFileClip(filename)
    clip.audio.write_audiofile(filename[:-4] + ".mp3")
    clip.close()

def choose_resolution(resolution: str) -> int:
    resolutions = {
        "low": 18,
        "medium": 22,
        "high": 137,
        "very high": 313
    }
    return resolutions.get(resolution, 18)

def download_video(url: str, resolution: str) -> str:
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    print(f"Downloading {url}...")
    stream = video.streams.get_by_itag(itag)
    filename = stream.default_filename
    stream.download()
    print(f"Downloaded {filename} successfully!")
    return filename

def download_videos(urls: List[str], resolution: str) -> None:
    for url in urls:
        download_video(url, resolution)

def main() -> None:
    print('''
    (1) Download YouTube Videos Manually
    (2) Download a YouTube Playlist
    ''')

    choice = input("Choice: ")
    quality = input("Enter quality (low, medium, high, very high): ")

    if choice == "2":
        link = input("Enter the link to the playlist: ")
        print("Downloading playlist...")
        download_playlist(link, quality)
        print("Playlist downloaded successfully!")
    elif choice == "1":
        links_input = input("Enter a single link or comma-separated links: ")
        links = [link.strip() for link in links_input.split(",")]
        print("Downloading videos...")
        download_videos(links, quality)
        print("All videos downloaded successfully!")
    else:
        print("Invalid input! Terminating...")

if __name__ == "__main__":
    main()
