class Chennai:
    def __init__(self):
        print("Chennai constructor called")

class Merina(Chennai):
    def __init__(self):
        super().__init__()
        print("Merina constructor called")

d = Merina()
