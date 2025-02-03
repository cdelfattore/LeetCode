# You could use pow(x, n) which is probably optimized to use binary exponentiation but that's not how you learn.

# x = 2.000000
# n = -2

# # Use Binary exponentiation to reduce the number of multiplications needed.
# result = pow(pow(x, 2), (n / 2))
# print(result)


# x = 3.00000
# n = 5
# result = pow(x * ( x * x))

# Using recursion
x = 3.000000
n = 80
t = n
if n < 0:
    t = abs(n)

loops = 0
result = 1
while t:
    if t & 1:
        result = result * x
    x = x * x
    t >>= 1
    loops += 1
print(loops)
if n < 0:
    result = 1 / result
print(result)