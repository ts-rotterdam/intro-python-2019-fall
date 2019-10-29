# Fibonacci numbers module
# return Fibonacci series up to n
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


# this will be run when imported
# f = int(input("Input n: "))
# print(fib(f))

# this will only be run when run directly
if __name__ == "__main__":
    f = int(input("Input n: "))
    print(fib(f))
