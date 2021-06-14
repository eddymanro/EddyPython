def uppercase(func):



@uppercase
def greet(name):
    return "Greetings {}!".format(name)


print(greet("World"))
