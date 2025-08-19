class Grandpa:
    def Tvs(self, TVS_price):
        print(f'TVs_total price is {TVS_price}')

class Father(Grandpa):
    def Land(self, total_land):
        print(f'total land is {total_land}')

    def Tvs(self, TVS_model):
        super().Tvs(TVS_price=1000)   # Call Grandpa with price
        print(f'TVe_model is ---> {TVS_model}')

class Child(Father):
    def Phone(self):
        print("Iphone--->17")

    def Land(self, land_loc):
        super().Land(total_land=100)  # Call Father with land
        print(f'land current location is {land_loc}')

c = Child()
c.Tvs(2025)
c.Phone()
c.Land("pune")
