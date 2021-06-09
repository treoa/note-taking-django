from enum import Enum

class Shake(Enum):
    VANILLA = 123
    EXPERT = 1234

print(Shake.EXPERT)
print(Shake.EXPERT.name)
print(Shake.EXPERT.value)
print(type(Shake.EXPERT))

# creating a simple add function
def add(a, b):
    return a+b
  
# creating a simple odd_even function
# to check if the number is odd or even
def odd_even(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")