# METHOD:The difference between a method and a function lies in their context and how they are used:
# the difference betwen method and function is that method uses
# Method: A method is a function that is associated with an object. It is defined inside a class and operates on the instance of that class. A method always takes at least one parameter, typically named self, which refers to the instance of the class it is called on. For example:
# class Cookie:
#     def get_color(self):  # This is a method
#         return self.color
# Here, get_color is a method because it is defined inside the Cookie class and operates on the instance (self).

# Function: A function is a standalone block of code that performs a specific task. It is not tied to any object or class unless explicitly passed one. For example:
# def greet(name):  # This is a function
#     return f"Hello, {name}!"
# Here, greet is a function because it is not defined inside a class and does not operate on an instance.

# Key Difference:
# A method is called on an object (e.g., cookie_one.get_color()), and it implicitly receives the instance (self) as its first argument.
# A function is called independently (e.g., greet("Alice")) and does not have access to any instance unless explicitly passed.
# In your Cookie class, get_color and set_color are methods because they are defined within the class and operate on the self instance.
       

class Cookie:
    def __init__(self, color):
        self.color = color     #putting color to cookie

    def get_color(self):
        return self.color       #returning its color output

    def set_color(self, color):
        self.color = color      #changing the previously set colour


cookie_one = Cookie('green')
cookie_two = Cookie('blue')

print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color())
print('Cookie two is still', cookie_two.get_color())
