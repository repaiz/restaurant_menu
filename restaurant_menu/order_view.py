from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView


class OrderView(ScrollView):
    def __init__(self, **kwargs):
        super(OrderView, self).__init__(**kwargs)


        self.size_hint = 0.9, 0.9
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        layout = BoxLayout(orientation="vertical", size_hint_y=None)

        order_list = App.get_running_app().order_list

        for item in order_list:
            item_name = item[0]["product_name"]
            item_amount = int(item[0]["amount"])
            item_price = int(item[0]["price"])
            label = Label(text=f"{item_name} : 数量  {item_amount} : 金額  {item_amount*item_price}円 ",size_hint_y=None,height=200)
            layout.add_widget(label)

        layout.bind(minimum_height=layout.setter('height'))

        self.add_widget(layout)
