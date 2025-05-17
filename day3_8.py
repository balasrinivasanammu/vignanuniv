class Gowri:
    def __init__(self):
        print("parent constructor")
    def infosys(self,a):
        print("chennai=",a)
class Abrod(Gowri):
    def __init__(self):
        super().__init__()
        print("child constructor")
    def infosys(self,x):
        super().infosys(x)
        print("banglore=",x)
g=Abrod()
g.infosys(1100)
