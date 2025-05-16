class Mango:
    def balaji(self,a,b):
        print("even" if a%2==0 else "odd")
        print(a+b)
    def ssvi(self,c):
        for i in range(c):
            print(i,"* 5 = ",i*5)
    def hema(self):
        print("hybd city")
    def nithish(self,d):
        fact=1
        for i in range(1,d+1):
            fact=fact*i
        print(fact)
        
m=Mango()    
m.balaji(101,51)
m.ssvi(11)
m.hema()
m.nithish(5)
o=Mango()
o.hema()

