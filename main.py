from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import webbrowser

import time

from filesharer import FileSharer

Builder.load_file('frontend.kv')

# as our design has two screens, we need to create two classes for each screen
# this is a requirement for KiVy

# can use the class to capture webcam type (start,stop, capture)
# extending the CameraScreen class which inherits from Screen
class CameraScreen(Screen):
    def start(self):
        '''Start the camera and change the text of the button to "Stop Camera"'''
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        # set texture back to default as the stop method sets it to None
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        '''Stop the camera and change the text of the button to "Start Camera"'''
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        '''Capture the current image of the camera and save it in the images folder'''
        current_time = time.strftime('%Y%m%d-%H%M%S', time.localtime())
        self.filepath = f"files/image_{current_time}.png"
        self.ids.camera.export_to_png(self.filepath)

        self.manager.current = "image_screen"
        # set current screen image source to latest dynamic image
        self.manager.current_screen.ids.image.source = self.filepath

class ImageScreen(Screen):
    # set class variable for link message that is available in the class methods
    link_message = "CREATE A LINK FIRST"
    def create_link(self):
        '''Create a sharable link of the image and display it on the screen'''
        file_path = App.get_running_app().root.ids.camera_screen.filepath
        fileshare = FileSharer(file_path)
        self.url = fileshare.share()
        self.ids.link.text = self.url

    def copy_link(self):
        '''Copy the link to the clipboard'''
        # class method to copy to clipboard, dont need object instance
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        '''Open the link in the browser'''
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()
