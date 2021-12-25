""" Factorial """

"""
- It is the product of all positive integers less than or equal to n
- Denoted by n!
- 0! = 1! = 1

Example:
6! = 6*5*4*3*2*1 = 720
6! = 6*5! as 6*5! = 6*5*4*3*2*1 = 720

General exp. : n(n-1)!
"""
def factorial(n):
    assert n >= 0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)


""" Fibonacci """

"""
Fibonacci sequence is sequence of numbers in which each number is the sum of the 
two preceding ones and the sequence starts from 0 and 1

Example:
0,1,1,2,3,5,8,13,21,34,55,89,...
5 = 3 + 2

General exp. : f(n) = f(n-1) + f(n-2)  (let n=6(index), f(n)=8, f(n-1)=5, f(n-2)=3)
"""
def fibonacci(n):
    assert n >=0 and int(n) == n , 'Fibonacci number cannot be negative number or non integer.'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == "__main__":
    num = 5
    print("The factorial of", num, "is", factorial(num))
    
    n = 6
    print(f"{n}th fibonacci number", fibonacci(n))


