import pymysql

class Database:

    def __init__(self):#コンストラクタ

        #下記のpymysql.connectでデータベースと接続
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="restaurant_db",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )

    def serch_item(self,product_code):
        sql = "SELECT * FROM menu WHERE product_code = %s"

        with self.connection.cursor()as cursor:
            cursor.execute(sql,(product_code))
            return cursor.fetchall()


        """
        ここから先が足した部分
        """


    def insert_count(self, count):
        sql = "INSERT INTO customer (count) VALUES (%s)"

        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql, (count))
                self.connection.commit()  # コミットを追加
                print("インサート成功")
        except Exception as e:
            print(f"失敗: {e}")


    def import_customer(self):
        sql = "SELECT customer_id FROM customer ORDER BY customer_id DESC LIMIT 1"

        with self.connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                last_customer_id = result["customer_id"]
                return last_customer_id
            else:
                return None

    def insert_order(self,order_list):
        insert_list = order_list

        sql = "INSERT INTO restaurant_db.order (customer_id, date, product_code, product_name, amount, price) VALUES (%s,%s,%s,%s,%s,%s)"

        for item in insert_list:
            customer_id = item[0]["customer_id"]
            date = item[0]["date"]
            product_code = item[0]["product_code"]
            product_name = item[0]["product_name"]
            amount = item[0]["amount"]
            price = item[0]["price"]

            try:
                with self.connection.cursor() as cursor:
                    cursor.execute(sql, (customer_id,date,product_code,product_name,amount,price))
                    self.connection.commit()  # コミットを追加
                    print("インサート成功")
            except Exception as e:
                print(f"失敗: {e}")


