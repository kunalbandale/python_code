class Flipkart:
    def data(self , name , price):
        print(f"my product name is {name} is total price is {price}")

class Ekart:
    def product_info(self,color,size):
        print(f"my product color is {color} and the size of the product is {size}")
        f = Flipkart()
        f.data("shoes" , 1200)

e = Ekart()
e.product_info("red", 120)
