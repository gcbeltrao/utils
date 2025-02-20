from pytubefix import YouTube
from pytubefix.cli import on_progress
import os

OUTPUT_FOLDER = "downloaded_videos"
VIDEO_LIST_FILE = "video_links.txt"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

with open(VIDEO_LIST_FILE) as file:
    video_links = file.readlines()

    for url in video_links:
        url = url.strip()
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=OUTPUT_FOLDER)
