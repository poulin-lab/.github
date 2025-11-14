2 * * 5
# syntax serror

3 +
# syntax error

4 / 0
# crashes, python identifies error before code is run

4 + 3 * 2
(4 + 3) * 2
# logic error -> forgot brackets

x = 7
# x doesn't equal to 7, you're assigning the variable to seven

age_mcgill_students = 23
# give all variables a proper name

y = x * 6
x = 8
y

# id tells you memory address of where a value is stored
id(x)
# if x = 7 or x = 8, the memory address will be different (every value has a different memory address)
# if a = 1000 or b = 1000, memory addresses will be different still
a = 1000
b = 1000
a = b
# assigning a to b, now a will refer to the same memory address as b (variables store memory addresses that refers to data)
a = 10
b = 10
id(a)
id(b)
# id the same... why? python knows that first few numbers are more used than bigger numbers, python needs to access it faster (breaks rule of different memory addresses for each person)
# depends on ram and python version... how to identify how much numbers break this rule? david's number is 256 (power of two, remember computers are in base 2)

def double(num: float) -> float:
    """ Return twice the value of num.
    >>> double(7.0)
    14.0
    >>> double(5.7)
    11.4
    """
    
    return num * 2
    
# sign a contract that num needs to be a float and then return a float (python DOES NOT CARE about the contract though)
# must use name of variables you get as a parameter
# >>> simulates the prompt of the python shell, examples of what you expect to get back
# help(double) will return how to use the function