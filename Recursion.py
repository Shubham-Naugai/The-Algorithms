""" Recursion """

# CodeProblem-1
def firstMethod():
    secondMethod()
    print("I am the first Method")

def secondMethod():
    thirdMethod()
    print("I am the second Method")

def thirdMethod():
    fourthMethod()
    print("I am the third Method")

def fourthMethod():
    print("I am the fourth Method")


# CodeProblem-2
## Recursion vs Iterarion ###
def powerOfTwo(n):
    if n == 0:
         return 1
    else:
        power = powerOfTwo(n-1)
        return power * 2


def powerOfTwoIt(n):
    i = 0
    power = 1
    while i < n:
        power = power * 2
        i = i + 1
    return power


# CodeProblem-3
# recursive case => f(num) = num%10 + f(num/10)
def SumOfDigits(n):
    assert n>=0 and int(n) == n, "number should be positive"
    if n == 0:
        return 0
    else:
        return n%10 + SumOfDigits(n//10)


# CodeProblem-4
def gcd(num1, num2):
    assert int(num2) == num2 and int(num1) == num1, "Numbers must be integer"
    if num1 < 0:
        a = -1 * num2
    if num2 < 0:
        num2 = -1 * num2
    if num2 == 0:
        return num1
    return gcd(num2, num1%num2)


# CodeProblem-5
def decimalToBinary(n):
    assert n >= 0 and int(n) == n, "number must be a positive integer only"
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * decimalToBinary(int(n/2))


# CodeProblem-6
def power(base, exp):
    assert exp>=0 and int(exp) == exp, 'Exponent must be positive integer only'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base*power(base, exp-1)

if __name__ == "__main__":
    # 1
    firstMethod()
    print()
    
    # 2
    print(powerOfTwo(3))
    print()
    print(powerOfTwoIt(4))
    print()
    
    # 3
    print(SumOfDigits(1114))
    print()
    
    # 4
    print("Greatest common divisor", gcd(47,-18))
    print()
    
    # 5
    print("converting decimal to binary", decimalToBinary(13))
    print()
    
    # 6
    print(power(2, 4))
    print()


