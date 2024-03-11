
from kivy.uix.screenmanager import ScreenManager, Screen

class ComfirmScreen(Screen):
    def current_main(self):
        self.manager.current = "main"