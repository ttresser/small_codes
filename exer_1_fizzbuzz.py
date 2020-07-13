def fizzbuzz(x):
    x = int(x)
    rest1 = x % 3
    rest2 = x % 5
    if rest1 == 0 and rest2 == 0:
        return "FizzBuzz"
    else:
        if rest1 == 0:
            return "Fizz"
        else:
            if rest2 == 0:
                return "Buzz"
            else:
                return x
