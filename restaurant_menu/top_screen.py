from kivy.app import App
from kivy.uix.screenmanager import  Screen
import main_screen as main
import database as data

class TopScreen(Screen):
    def push_number(self,button):
        text = self.ids.text_box
        text.text = f"{button.text}人"

    def delete_number(self):
        text = self.ids.text_box.text
        text = text[:-2]
        self.ids.text_box.text = text


        """
        ここから下は修正した部分
        """
    def confirm_button(self):
        db = data.Database()
        text = self.ids.text_box.text
        text = text[:-1]
        db.insert_count(int(text))
        c_id = db.import_customer()
        App.get_running_app().customer_id = c_id

        if not self.manager.has_screen('main'):
            self.manager.add_widget(main.MainScreen(name='main'))
        self.manager.current = "main"
