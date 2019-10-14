#Factorial Calculator
n = input("Enter number: ")
fact = 1

for x in range(int(n),0,-1):
	fact = fact*x

print(fact)