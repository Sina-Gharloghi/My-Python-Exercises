s=int(input("enter the number : "))
a=s

for x in range(1,s):
	b = s*(a-1)
	a=a-1
	s=b
	
print (b)