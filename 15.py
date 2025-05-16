class Salem:
    def __init__(self):
        print("salem cor")
    def car(self):
        print("my car")
        
class Chennai(Salem):
    def __init__(self):
        print("chennai cor")
        

    def byke(self):
        print("my byke")

c=Chennai()
c.byke()
c.car()
