# hexadecimals = [1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f"]
string = {
    "a": "01100001",   # 1.key   2.value
    "b": "01100010",
    "c": "01100011",
    "d": "01100100",
    "e": "01100101",
    "f": "01100110"
}
numbers = {
    "0": "00110000",   # 1.key   2.value
    "1": "00110001",
    "2": "00110010",
    "3": "00110011",
    "4": "00110100",
    "5": "00110101",
    "6": "00110110",
    "7": "00110111",
    "8": "00111000",
    "9": "00111001"
}
binary1 = []
binary2 = []
input1 = input("enter a hex: ")
print("")
byte = ""
start = 0
counter = 0
str1 = ""

for hex in input1:
    if hex != "#":
        for num1 in numbers.keys():
            if hex == num1:
                binary1.append(numbers.get(num1))
        for str1 in string.keys():
            if hex == str1:
                binary1.append(string.get(str1))

binary1 = list(binary1)


print(binary1)

for count1, num in enumerate(binary1):
    if num == " ":
        start = count1
    elif num != " " or "[" or "]" or "," or "'":
        if counter == 8:   # 1 byte (8 bits)
            for num in numbers.keys():
                if num == byte:
                    byte == numbers.get(byte)
            binary2.append(byte)
            print(f"binary1: {binary1}")
            byte = ""
            counter = 0
        counter += 1
        byte += num
    
            

print("")
print(f"done binary: {binary1}")
print(f"done string: {str1}")















# Ctrl+K Ctrl+C
# Ctrl+K Ctrl+U