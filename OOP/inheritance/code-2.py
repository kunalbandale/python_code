class parent:
    def __init__(self):
        print("constructor parent")

class child(parent):
    def __init__(self):
        super(self).__init__()
        print("constructor child")

c = child
c.__init__(c)

