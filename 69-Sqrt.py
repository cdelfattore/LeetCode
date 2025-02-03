# Find square roots without using operators

x = 0
print(x ** 0.5)

# Babylonian squares isn't the most optimal
guess = x / 2
# guess = (guess + (x / guess)) / 2
# guess = (guess + (x / guess)) / 2
# print((guess + (x / guess)) / 2)
while True:
    cg = (guess + (x / guess)) / 2
    if cg == guess:
        break
    else:
        guess = cg
        print(guess) 