import math

y = float(input("Write the value of y:\n"))
A = float(input("Write the value of a:\n"))
B = float(input("Write the value of b:\n"))
C = float(input("Write the value of c:\n"))

quadratic_formula = (B**2) - (4*A*(C - y))

if quadratic_formula > 0:
    The_first_x = (-B + math.sqrt(quadratic_formula)) / (2*A)
    The_second_x = (-B - math.sqrt(quadratic_formula)) / (2*A)
    print(f"The solutions are {The_first_x} and {The_second_x}")

elif quadratic_formula == 0:
    X = -B / (2*A)
    print(f"The solution for both roots is {X}")

else:
    real_part = -B / (2*A)
    imaginary_part = math.sqrt(abs(quadratic_formula)) / (2*A)
    The_first_x = complex(real_part, imaginary_part)
    The_second_x = complex(real_part, -imaginary_part)
    
    if The_first_x == The_second_x:
        print(f"The solution to both roots is {The_first_x}")
    else:
        print("The roots are imaginary.")
        print(f"The first solution is {The_first_x}")
        print(f"The second solution is {The_second_x}")


















