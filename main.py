from window import Window

# MP4FOLDER = "/home/mathieu/Videos"
# MP3FOLDER = "/home/mathieu/Music"

# downloader = Downloader("https://www.youtube.com/watch?v=L2HsVzdA8dk")
# mp4_file_path = downloader.download_mp4(MP4FOLDER)
# mp3_file_name = mp4_file_path.split("/")[-1][:-1] + "3" 
# mp3_file_path = downloader.convert_mp3(mp4_file_path, os.path.join(MP3FOLDER, mp3_file_name))


window = Window("/home/mathieu/Videos", "/home/mathieu/Music")
window.run()