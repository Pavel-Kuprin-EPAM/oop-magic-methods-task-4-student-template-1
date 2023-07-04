import sys
sys.tracebacklimit = 0
class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """
    def __set_name__(self, owner, name):
        self.name = name
    
    def __set__(self, instance, value):
        # try:
            if not 0 <= value <= 100:
                raise ValueError(f"Price must be between 0 and 100.")
            instance.__dict__[self.name] = value
        # except ValueError as ve:
        #     print(ve)

class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """
    def __set_name__(self, owner, name):
        self.name = name
        self.count_exp_date = 0
    def __set__(self, instance, value):
        # try:
            if hasattr(instance, self.name) and self.count_exp_date>=1:
                raise ValueError(f"{self.name.capitalize()} can not be changed.")
            if hasattr(instance, self.name): 
                self.count_exp_date+=1 
                instance.__dict__[self.name] = value
        # except ValueError as ve:
        #     print(ve)

class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()
    def __init__(self, author, name, price) -> None:
        self.author = author
        self.name = name
        self.price = price

b = Book("William Faulkner", "The Sound and the Fury", 12)
print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")


b.price = -12
print(b.price)
b.price = 55
print(b.price)
b.author = "new author"
b.name = "new name"