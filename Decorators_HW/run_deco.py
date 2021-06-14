print_registry = []


# Exercise 1
def uppercase(function):
    def wrapper(text):
        fct = function(text)
        make_uppercase = fct.upper()
        return make_uppercase

    return wrapper


# Exercise 2
def safe_divide(function):
    def wrapper(first_number, second_number):
        try:
            fct = function(first_number, second_number)
            return fct
        except ZeroDivisionError:
            return 'Unable to perform division'

    return wrapper


@safe_divide
def divide(first_number, second_number):
    return first_number / second_number


def register(func):
    global print_registry
    print_registry.append(func.__name__)

    def inside_func(*args, **kwargs):
        return func

    return inside_func


# I have a question here, if I use 2 decorators on the same function "greet" than i get the name function wrapper
# not sure how to bypass that and get the function
@uppercase
def greet(name):
    return "Greetings {}!".format(name)


@register
def say_hello(name):
    return "Hello {}!".format(name)


@register
def say_goodbye(name):
    return "Goodbye {}!".format(name)


print(greet("World"))
print(divide(10, 4))
print(divide(22, 60))
print(divide(2, 0))

print(print_registry)
