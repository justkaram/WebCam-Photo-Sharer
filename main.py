from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from filestack import Client
import time
import os
import pyperclip

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.cam.play = True
        self.ids.cam_button.text = 'Stop Camera'

    def stop(self):
        self.ids.cam.play = False
        self.ids.cam_button.text = 'Start Camera'
        self.ids.cam.texture = None

    def capture(self):
        current_time = time.strftime('%d%m%Y-%H%M%S')
        path = f'files/{current_time}.png'
        self.ids.cam.export_to_png(path)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img_screen.source = path


class FileShare:

    def __init__(self, file_path, api_key='AqiHXdRzhT0aW9n3FOeVDz'):
        self.file_path = file_path
        self.api_key = api_key

    def get_link(self):
        client = Client(apikey=self.api_key)
        link = client.upload(filepath=self.file_path)
        return link.url


class ImageScreen(Screen):

    def create_link(self):
        os.chdir('files')
        img_path = os.listdir()[-1]
        file = FileShare(file_path=img_path)
        self.img_url = file.get_link()
        self.manager.current_screen.ids.link_label.text = self.img_url

    def copy_link(self):
        try:
            pyperclip.copy(self.img_url)
        except AttributeError:
            self.ids.link_label.text = 'Create a link first'


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
