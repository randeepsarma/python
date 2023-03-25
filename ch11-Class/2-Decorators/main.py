# python decorators are a way to extend the functionality of functions and methods, by modifying its behavior without modifying the source code. They are used for a variety of purposes, such as logging, memoization, access control, and more. They are a powerful tool that can be used to make your code more readable, maintainable, and extendable.
def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        print(*args)
        print(**kwargs)
        fx(*args, **kwargs)
        print("Thanks for using this function")

    return mfx


@greet
def add(a, b):
    print(a + b)


add(1, 2)
