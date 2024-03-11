from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class FooterLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(FooterLayout,self).__init__(**kwargs)

        cart_button = Button(text = "カートを確認", on_press = self.current_cart)
        order_log_button = Button (text = "注文履歴", on_press = self.current_order_log)
        call_waiter_button = Button(text = "店員を呼ぶ", on_press = self.current_call_waiter)
        checkout_button = Button(text = "お会計", on_press = self.current_checkout)
        back_main_menu_button = Button(text = "メニューへ戻る", on_press = self.current_back_main_menu)

        self.add_widget(cart_button)
        self.add_widget(order_log_button)
        self.add_widget(call_waiter_button)
        self.add_widget(checkout_button)
        self.add_widget(back_main_menu_button)

    def current_cart(self,instance):
        App.get_running_app().sm.current = "cart"

    def current_order_log(self,instance):
        App.get_running_app().sm.current = "order_log"

    def current_call_waiter(self,instance):
        App.get_running_app().sm.current = "call_waiter"

    def current_checkout(self,instance):
        App.get_running_app().sm.current = "checkout"

    def current_back_main_menu(self,instance):
        App.get_running_app().sm.current = "main"
        

