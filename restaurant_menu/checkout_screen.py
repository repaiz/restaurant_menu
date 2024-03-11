from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
import database as data

class CheckoutScreen(Screen):
    def on_enter(self, *args):
        customer_id = App.get_running_app().customer_id
        order_list = App.get_running_app().order_list

        #合計金額の取得
        total_price = 0
        for item in order_list:
            item_price = int(item[0]["price"])
            item_amount = int(item[0]["amount"])
            total_price += item_price*item_amount

        self.ids.comfirm_total_price.text = f"合計金額：{str(total_price)}円です。"

        #各オーダー情報に顧客IDを付与
        for item in order_list:
            item[0]["customer_id"] = customer_id

        db = data.Database()
        db.insert_order(order_list)




    def reset(self):
        cart_list = []
        App.get_running_app().cart_list = cart_list
        order_list = []
        App.get_running_app().cart_list = order_list

        App.get_running_app().customer_id = 0

        top_screen = self.manager.get_screen('top')
        top_screen.ids.text_box.text = ""
        self.manager.current = "top"
