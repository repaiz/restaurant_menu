from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import NumericProperty

#Python上でボタンにIDを付与することができないのでボタンをカスタム
#delete＿buttonメソッドでカートリスト内の特定のオブジェクトを削除する際にインデックスを指定するために必要
class CustomButton(Button):
    unique_id = NumericProperty()

class ScrollView(ScrollView):
    def __init__(self, **kwargs):
        super(ScrollView, self).__init__(**kwargs)

        #スクロール画面のサイズと位置を指定
        self.size_hint = 0.9, 0.9
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        #スクロールの中に表示するボックスレイアウトを作成
        #サイズヒントYをNoneにしておくことが重要
        layout = BoxLayout(orientation = "vertical", size_hint_y = None)

        #カートに入っているリスト型のオブジェクトを取得
        cart_list = App.get_running_app().cart_list

        #ループでリスト内のオブジェクトの情報を取り出し、ボタンにしてボックスレイアウトに追加
        for item in cart_list:
            item_id = 0
            item_name = item[0]["product_name"]
            item_amount = int(item[0]["amount"])
            item_price = int(item[0]["price"])
            button = CustomButton(unique_id = item_id, text = f"{item_name} : 数量  {item_amount} : 金額  {item_amount*item_price}円  :削除", on_press=self.delete_button, size_hint_y = None, height = 200)
            layout.add_widget(button)

        #スクロールが持つminimum_heightの値にボックスレイアウトの高さを常に合わせるための記述
        layout.bind(minimum_height = layout.setter('height'))

        self.add_widget(layout)

    #カートに入っている商品を削除する記述
    def delete_button(self, instance):
        #childrenはkivyがもつモジュールで、おそらくself(スクロール)のchildren(子widget※今回はボックスレイアウト)を指している
        layout = self.children[0]
        layout.remove_widget(instance)

        cart_list = App.get_running_app().cart_list
        del cart_list[instance.unique_id]

        App.get_running_app().root.get_screen("cart").update_total_price()