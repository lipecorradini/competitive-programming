
# importing library sympy 
from sympy import symbols, Eq, solve 
  
# defining symbols used in equations 
# or unknown variables 
a, b, c = symbols('x,y') 
  
# defining equations 
eq1 = Eq((x+y), 1) 
print("Equation 1:") 
print(eq1) 
eq2 = Eq((x-y), 1) 
print("Equation 2") 
print(eq2) 
  
# solving the equation 
print("Values of 2 unknown variable are as follows:") 
  
print(solve((eq1, eq2), (x, y))) 


def main():
    while(True):

        n = input()
        if not n:
            break
        