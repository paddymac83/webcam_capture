from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time

from filesharer import FileSharer

Builder.load_file('frontend.kv')

# as our design has two screens, we need to create two classes for each screen
# this is a requirement for KiVy

# can use the class to capture webcam type (start,stop, capture)
# extending the CameraScreen class which inherits from Screen
class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        # set texture back to default as the stop method sets it to None
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S', time.localtime())
        filepath = f"files/image_{current_time}.png"
        self.ids.camera.export_to_png(filepath)

class ImageScreen(Screen):
    pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()
