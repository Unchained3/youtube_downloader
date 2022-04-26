from pytube import YouTube
from moviepy.editor import *

class Downloader:
    def __init__(self, link) -> None:
        self.link = link

    def download_mp4(self, mp4_folder) -> str:
        youtube = YouTube(self.link)
        file_name = youtube.streams[0].title.replace(" ", "_").replace("/", "-") + ".mp4"
        file_path = youtube.streams.filter(progressive=True, file_extension='mp4').order_by("resolution").desc().first().download(output_path=mp4_folder, filename=file_name)
        return file_path

    def convert_mp3(self, mp4_file_path, mp3_file_path) -> str :
        video = VideoFileClip(mp4_file_path)
        video.audio.write_audiofile(mp3_file_path)
