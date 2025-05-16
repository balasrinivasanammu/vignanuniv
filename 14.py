class Hema:
    def jewels(self):
        value=250000
        print(value)
class Son1(Hema):
    def car(self):
        value=300000
        print(value)
class Son2(Hema):
    def byke(self):
        value=15000
        print(value)
class daughter(Hema):
    def job(self):
        value=60000
        print(value)
s1=Son1()
s2=Son2()
d1=daughter()
s1.car()
s1.jewels()
s2.byke()
s2.jewels()
d1.job()
d1.jewels()