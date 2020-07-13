nm = int(input("Um número inteiro: "))
rest1 = nm % 5
rest2 = nm % 3
if rest1 == 0 and rest2 == 0:
    print("FizzBuzz")
else:
    print(nm)
