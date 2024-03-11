from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.properties import NumericProperty

import database as data

class DetailScreen(Screen):
    source = StringProperty()
    price = StringProperty()
    name = StringProperty()
    amount = NumericProperty(1)

    def on_enter(self, *args):
        item_id = App.get_running_app().button_id

        db = data.Database()
        dict = db.serch_item(int(item_id))
        self.name = dict[0]["product_name"]
        self.price = f"{dict[0]['price']}円"
        self.source = f"{item_id}.jpeg"

    def add_cart(self):
        item_id = App.get_running_app().button_id
        db = data.Database()
        dict = db.serch_item(int(item_id))
        dict[0]["amount"]=self.amount
        App.get_running_app().cart_list.append(dict)
        self.manager.current = "cart"

    def plus_amount(self,button):
        self.amount += button
        self.ids.amount.text = str(self.amount)

