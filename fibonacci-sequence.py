a = 1
b = 1

i = int(input("Enter the sequence length : "))

print(a)
print(b)

for x in range(i):
    c = a + b

    print(c)

    b = a
    a = c

e = input("press ant key to exit ...")