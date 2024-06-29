def star(func):
    def wrapper():
        print("*"*10)
        func()
        print("*"*10)
    return wrapper

@star

def hello():
    print("hello")

# star (hello)()
hello()
