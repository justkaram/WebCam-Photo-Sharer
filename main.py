from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.camera import Camera
from filestack import Client

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
        self.ids.cam.export_to_png('image.png')


class FileShare:

    def __init__(self, file_path, api_key='AqiHXdRzhT0aW9n3FOeVDz'):
        self.file_path = file_path
        self.api_key = api_key

    def get_link(self):
        client = Client(apikey=self.api_key)
        link = client.upload(filepath=self.file_path)
        return link.url


class ImageScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
