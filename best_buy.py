import json
class BestBuy:
    def __init__(self):
        self.fileName = "best_buy.json"
        self.jsonObject=None
        #INSERT INTO product (sku, name, description, image_url, active, units_in_stock, unit_price, category_id,date_created) VALUES ('BOOK-TECH-1000', 'Crash Course in Python', 'Learn Python at your own pace. The author explains how the technology works in easy-to-understand language. This book includes working examples that you can apply to your own projects. Purchase the book and get started today!', 'assets/images/products/books/book-luv2code-1000.png', 1, 100, 14.99, 1, NOW());
    def save_str(self,strContent):
        fp = None
        pstr=strContent.encode('utf-8')
        try:
           filename="data.sql"
           fp = open(filename, "w")
           if fp:
                fp.write(pstr)
                print("Successfully created " + filename)
        finally:
            if fp:
                fp.close()

    def generate(self):
        products=self.jsonObject["catalog"][1];
        sql=""
        for prod in products["products"]:
            sku = prod["sku"]
            name = prod["name"]
            if prod["category_id"] == "1000":
               category_id="1"
            else:
               category_id="2"
            description=prod["description"]
            description="Will be updated later"
            image_url=prod["images"][0]["url"]
            active = "1"
            units_in_stock ="100"
            unit_price=prod["price"]
            date_created="NOW()"
            sql += "INSERT INTO product_best_buy (sku, name, description, image_url, active, units_in_stock, unit_price, category_id,date_created) VALUES("
            sql += "'" + sku + "',"
            sql += "'" + name + "',"
            sql += "'" + description + "',"
            sql += "'" + image_url + "',"
            sql += active + ","
            sql += units_in_stock + ","
            sql += unit_price + ","
            sql += category_id + ","
            sql += date_created + ")"
            sql += ";\n"
        realsql= sql
        self.save_str(realsql)



    def loadJson(self):
        try:
            with open(self.fileName) as f:
                try:
                    self.jsonObject = json.load(f)
                    return self.jsonObject
                except Exception as e:
                    raise e
        except Exception as e:
            print ("{0}:{1}".format(e.args[1], file))



