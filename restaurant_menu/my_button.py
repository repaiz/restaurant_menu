
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

class MyButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(MyButton, self).__init__(**kwargs)
        self.source = ""
