from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase, DEFAULT_FONT
from kivy.resources import resource_add_path
from kivy.properties import ListProperty
from kivy.properties import StringProperty
from kivy.properties import NumericProperty

#必要なスクリーンをインポート
import top_screen as top
import main_screen as main
import detail_screen as detail
import cart_screen as cart
import comfirm_screen as comfirm
import order_log_screen as order
import call_waiter_screen as call_waiter
import checkout_screen as checkout

#kvファイル内でMyButtonクラスを利用するためインポートが必要
import my_button
import footer_layout

#言語設定
resource_add_path("/System/Library/Fonts")
LabelBase.register(DEFAULT_FONT, "Hiragino Sans GB.ttc")

#画像のパスを設定
resource_add_path("image")

class MenuApp(App):

    #カートの中身を保存するリスト
    cart_list = ListProperty()

    #注文履歴を保存するリスト
    order_list = ListProperty()

    #顧客IDを保存するプロパティ
    customer_id = NumericProperty()

    #build関数で起動時の初期設定を実施
    def build(self):
        self.sm = ScreenManager()
        self.sm.add_widget(top.TopScreen(name = "top"))
        self.sm.add_widget(main.MainScreen(name = "main"))
        self.sm.add_widget(detail.DetailScreen(name = "detail"))
        self.sm.add_widget(cart.CartScreen(name = "cart"))
        self.sm.add_widget(comfirm.ComfirmScreen(name = "comfirm"))
        self.sm.add_widget(order.OrderLogScreen(name = "order_log"))
        self.sm.add_widget(call_waiter.CallWaiterScreen(name = "call_waiter"))
        self.sm.add_widget(checkout.CheckoutScreen(name = "checkout"))
        return self.sm

#runメソッドでアプリを起動
MenuApp().run()