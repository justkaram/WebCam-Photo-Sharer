from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from file_share import FileShare
import time
import os
import pyperclip
import webbrowser

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.cam.opacity = 1
        self.ids.cam.play = True
        self.ids.cam_button.text = 'Stop Camera'

    def stop(self):
        self.ids.cam.opacity = 0
        self.ids.cam.play = False
        self.ids.cam_button.text = 'Start Camera'
        self.ids.cam.texture = None

    def capture(self):
        current_time = time.strftime('%d%m%Y-%H%M%S')
        self.path = f'files/{current_time}.png'
        self.ids.cam.export_to_png(self.path)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img_screen.source = self.path


class ImageScreen(Screen):
    link_message = 'Create a link first !!'

    def create_link(self):
        img_path = App.get_running_app().root.ids.camera_screen.path
        file = FileShare(file_path=img_path)
        self.img_url = file.get_link()
        self.manager.current_screen.ids.link_label.text = self.img_url

    def copy_link(self):
        try:
            pyperclip.copy(self.img_url)
        except AttributeError:
            self.ids.link_label.text = self.link_message

    def open_link(self):
        try:
            webbrowser.open(self.img_url)
        except AttributeError:
            self.ids.link_label.text = self.link_message

    def back_to_cam(self):
        self.manager.current = 'camera_screen'


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
