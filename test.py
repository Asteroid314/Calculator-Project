def factorial(n):
    try:
        if type(n)==str:
            raise TypeError
        if n<0:
            raise ValueError
        elif n==0 or n==1:
            return 1
        else:
            return n*factorial(n-1)
    except ValueError:
        return "Must be 0 or greater to perform a factorial"
    except TypeError:
        return f"Must be an integer, as {n} is not an integer"

print(factorial("joshua vandervelde"))
print(factorial(7))
print(factorial(0))
print(factorial(-4))
