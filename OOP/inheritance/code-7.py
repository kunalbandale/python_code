class ShowRoom:
    def __init__(self):
        print("Showroom -- 1")
class Room(ShowRoom):
    def __init__(self):
        super().__init__()
        print("Showroom -- 2")
class Show(Room):
    
    def __init__(self):
        print("ShowRoom -- 3")

s = Room()