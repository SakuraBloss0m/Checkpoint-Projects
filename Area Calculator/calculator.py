# Area Calculator
# printing header
print("==========")
print("Area Calculator 📐")
print("==========")

# selectable options
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")

answer = int(input("Which shape: "))

# value inputs
# --------- Triangle ---------
if answer == 1:
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = 0.5 * base * height
    print(f"Area of triangle: {area}")

# --------- Rectangle ---------
elif answer == 2:
    length = float(input('Enter the Length: '))
    width = float(input("Enter the width: "))
    area = length * width
    print(f"Area of rectangle: {area}")

# --------- Square ------------
elif answer == 3:
    side = float(input("Enter the side: "))
    area = side * side
    print(f"Area of square: {area}")

# --------- Circle -------------
elif answer == 4:
    radius = float(input("Enter the radius: "))
    area = 3.14 * radius * radius
    print(f"Area of circle: {area}")

# -------- Quit Option -----------
elif answer == 5:
    print("Goodbye!")

else:
    print("Invalid Option")
