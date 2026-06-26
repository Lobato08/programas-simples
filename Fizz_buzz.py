numero_1 =101

for numero_1 in range(1, 101):
    if numero_1 % 5 == 0 and 3 == 0:
      print("fizzbuzz")
    elif numero_1 % 5 == 0:
        print("Buzz")

    elif numero_1 % 3 == 0:
        print("Fizzz")

    else:
        print(numero_1)