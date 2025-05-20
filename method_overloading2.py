class Formula:
    def area(self, *args):
        if len(args) == 1:
           
            return args[0] ** 2
        elif len(args) == 2:
            
            return args[0] * args[1]
        else:
            return "Invalid number of arguments"

calc = Formula()
print(calc.area(5))        
print(calc.area(4, 6))     
print(calc.area())         
