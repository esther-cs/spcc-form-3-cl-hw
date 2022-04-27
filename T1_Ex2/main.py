#Part 1 - Calculation of discount
total_price=int(input("Enter the total purchase price: $ "))
if total_price>=150:
    discount_price=total_price*0.8
elif total_price>=100:
    discount_price=total_price*0.9
elif total_price>=50:
    discount_price=total_price*0.95
discount_price=str(discount_price)
print("Discounted price: $"+discount_price)

#Part 2- a better quadratic equation solver
import math
from math import sqrt
a=int(input())
b=int(input())
c=int(input())
if a==0:
    print("Not a quadratic equation!")
elif ((b**2) < (4*a*c)):
    print("No real roots")
else:
    x_1=(-1*b+math.sqrt(b**2-(4*a*c)))/(2*a)
    x_2=(-1*b-math.sqrt(b**2-(4*a*c)))/(2*a)
    x_1=str(x_1)
    x_2=str(x_2)
    print("The roots are "+x_1+" and "+x_2)
