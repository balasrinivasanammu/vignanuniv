class Testmatch:
    def city(self, name=None,salary=None):
        if name or salary:
            print(f"Best of luck, {name} {salary}!")
        elif name:
            print("Oreo",name)
        else:
            print("Good day!")
 
d = Testmatch()
d.city()         
d.city("Balaji")
d.city("Balaji",10000)  
