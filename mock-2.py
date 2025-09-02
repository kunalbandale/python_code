class Camera:
    def take_photo(self):
        print("Taking a photo")

class Phone:
    def make_call(self, number):
        print(f" Calling {number}")

class SmartPhone(Camera, Phone):
    def browse_internet(self):
        print("Browsing the Internet")

sp = SmartPhone()

sp.take_photo()
sp.make_call("7499515487")
sp.browse_internet()
