from kivy.app import App
from kivy.uix.screenmanager import Screen
import scroll_view as scroll
from datetime import datetime

class CartScreen(Screen):
    def on_enter(self, *args):

        self.ids.scroll.clear_widgets()

        scroll_view = scroll.ScrollView()
        self.ids.scroll.add_widget(scroll_view)

        self.update_total_price()

    def update_total_price(self):

        cart_list = App.get_running_app().cart_list
        total_price = 0
        for item in cart_list:
            item_price = int(item[0]["price"])
            item_amount = int(item[0]["amount"])
            total_price += item_price*item_amount
        self.ids.cart_total_price.text = f"{str(total_price)}円"

    def order_comfirm(self):
        cart_list = App.get_running_app().cart_list
        order_list = App.get_running_app().order_list

        now = datetime.now().replace(microsecond=0)

        for item in cart_list:
            item[0]["date"] = now
            order_list.append(item)

        cart_list = []
        App.get_running_app().cart_list = cart_list

        self.manager.current = "comfirm"

