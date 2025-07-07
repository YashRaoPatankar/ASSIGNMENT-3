# for factorial calculation
def factorial(n):
        if n < 0:
            return "Factorial not defined for negative numbers"
        elif n < 2:
            return 1
        else:
            return n * factorial(n - 1)
        
nn = int(input("Enter a number to find its factorial: "))
result = factorial(nn)
print(f"The factorial of {nn} is", result)