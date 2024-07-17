import random

print("How long should the password be?")
amount = int(input())

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["-", "+", ":", ";", ",", ".", "!", "?", "_", "/", "*", "@", "#"]

code = []

# random letter
def randomLetter():
    l = random.randint(0, 25)
    x = alphabet[l]
    # uppercase
    r = random.randint(0, 1)
    if r == 1:
        x = x.upper()
    code.append(x)

# random number
def randomNumber():
    l = random.randint(0, 9)
    x = str(numbers[l])  # Convert the number to a string before appending
    code.append(x)

# random symbol
def randomSymbol():
    l = random.randint(0, 12)
    x = symbols[l]
    code.append(x)

while len(code) < amount:
    r = random.randint(0, 5)
    if r == 0 or r == 1 or r == 2:
        randomLetter()
    elif r == 3 or r == 4:
        randomNumber()
    elif r == 5:
        randomSymbol()

code = ''.join(code[:amount])
print(code)
