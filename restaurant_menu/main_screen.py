from kivy.app import App
from kivy.uix.screenmanager import Screen,ScreenManager

import detail_screen as detail

class MainScreen(Screen):

    def current_change(self,button_id):
        App.get_running_app().button_id = button_id
        if not self.manager.has_screen('detail'):
            self.manager.add_widget(detail.DetailScreen(name='detail'))
        self.manager.current = 'detail'
