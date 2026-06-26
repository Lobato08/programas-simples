import math 


N = int(input("informe o numero para calcular o fatorial"))

print (math.factorial(N))

print(50*'-')

n = 4
for i in range(2,n +1):
    n *= i
    print (n)