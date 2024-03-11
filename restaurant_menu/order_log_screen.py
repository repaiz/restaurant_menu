from kivy.app import App
from kivy.uix.screenmanager import Screen
import order_view as ov

class OrderLogScreen(Screen):
    def on_enter(self, *args):

        self.ids.order.clear_widgets()
        order_view = ov.OrderView()
        self.ids.order.add_widget(order_view)

        self.update_total_price()

    def update_total_price(self):

        order_list = App.get_running_app().order_list
        total_price = 0
        for item in order_list:
            item_price = int(item[0]["price"])
            item_amount = int(item[0]["amount"])
            total_price += item_price*item_amount
        self.ids.order_total_price.text = f"合計金額：{str(total_price)}円"
