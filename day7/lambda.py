def myfunc(n):
    return lambda a : a*n
    lambda a : a*2
doubler = myfunc(2)
triper = myfunc(3)

# print(doubler(3))
print(triper(3))

# lambda function remains always in return type.

