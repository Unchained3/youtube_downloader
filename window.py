from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.config import Config
import os

from downloader import Downloader

class FileChoosePopup(Popup):
    load = ObjectProperty()

class ClosablePopup(Popup):
    
    message = StringProperty("Default message")

    def set_message(self, message):
        self.message = message 

    def set_color(self, color):
        self.separator_color = color

class MainWidget(Widget):
    video_file_path = StringProperty("/")
    music_file_path = StringProperty("/")
    youtube_url = StringProperty("")
    file_chooser_popup = ObjectProperty(None)

    def open_popup_video(self):
        self.file_chooser_popup = FileChoosePopup(load=self.load_video)
        self.file_chooser_popup.open()

    def open_popup_music(self):
        self.file_chooser_popup = FileChoosePopup(load=self.load_music)
        self.file_chooser_popup.open()

    def load_video(self, selection):
        self.file_chooser_popup.dismiss()
        self.video_file_path = selection

    def load_music(self, selection):
        self.file_chooser_popup.dismiss()
        self.music_file_path = selection

    def update_url(self):
        self.youtube_url = self.ids.youtube_url_input.text

    def download(self):
        if self.youtube_url == "":
            popup = ClosablePopup()
            popup.set_message("A Youtube URL have to be selected")
            popup.set_color([1, 0, 0, 1])
            popup.open()
            return
        downloader = Downloader(self.youtube_url)
        mp4_file_path = downloader.download_mp4(self.video_file_path)
        mp3_file_name = mp4_file_path.split("/")[-1][:-1] + "3"
        downloader.convert_mp3(mp4_file_path, os.path.join(self.music_file_path, mp3_file_name))
        popup.dismiss()
        popup = ClosablePopup()
        popup.set_message("Video have been converted")
        popup.set_color([0, 1, 0, 1])
        popup.open()

class MainApp(App):
    def build(self):
        Config.set('kivy', 'exit_on_escape', '0')
        return MainWidget()
    
if __name__ == "__main__":
    MainApp().run()

