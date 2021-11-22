car = []
price = []

i = int(input("enter the quantity of cars : "))

for x in range(i) :
    n = str(input("car name : "))
    m = float(input("price : "))

    car.append(n)
    price.append(m)

name = str(input("enter the car name : "))

if name in car:
    c = car.index(name)

    print ("price = ", price[c] , "$")
else:
    print("the car doesn't exist")

input()