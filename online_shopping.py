class Product:
    store_name="TechShop Georgia"
    currency="GEL"
    total_products=0

    def __init__(self, name, price, stock, category, discount=0):
        self.name= name 
        self.price=float(price)
        self.stock=int(stock)
        self.category=category
        self.discount=discount
        Product.total_products  +=1
        pass

    def get_info(self):
        return f"Product Name: {self.name}, Price: {self.price} {self.currency}, Stock: {self.stock}, Category: {self.category}, Discount: {self.discount}%"

    def apply_discount(self, percent):
        self.discount=percent
        discounted_price=self.price*(1-(percent/100))
        return discounted_price
    def update_stock(self, amount):
        self.stock += amount
        if self.stock < 0:
            return "Stock cannot be negative."
        return self.stock
    def calculate_final_price(self):
        final_price=self.price - (self.price * self.discount / 100)
        return final_price
    @classmethod
    def get_total_products(cls):
        return cls.total_products

p1 = Product("Smartphone X", 1200, 15, "Electronics")
p2 = Product("Wireless Headphones", 250, 30, "Electronics", discount=10)
p3 = Product("Running Shoes", 180, 8, "Sportswear")

print(p1.get_info())
p1.apply_discount(15)
print(f"final price  {p1.calculate_final_price()} {Product.currency}")

p3.update_stock(5) 
p3.update_stock(-2)
