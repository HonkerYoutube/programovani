import re

numbers = {
    "00110000": "0",
    "00110001": "1",
    "00110010": "2",
    "00110011": "3",
    "00110100": "4",
    "00110101": "5",
    "00110110": "6",
    "00110111": "7",
    "00111000": "8",
    "00111001": "9",
    "01100001": "10",
    "01100010": "11",
    "01100011": "12",
    "01100100": "13",
    "01100101": "14",
    "01100110": "15"
}

input1 = input("Enter a binary string: ").replace(" ", "")  # Removing spaces for simplicity
input1 = input1.replace("'", "")
input1 = input1.replace(",", "")
input1 = input1.replace("[", "")
input1 = input1.replace("]", "")

str1 = input1
print(f"str1: {str1}")
print(f"len(str1): {len(str1)}")
list1 = []
byte = ""
counter = 0

# Loop through the input string and extract bytes
for i in range(0, len(input1), 8):
    byte = input1[i:i+8]
    if byte in numbers:
        list1.append(numbers[byte])
    else:
        list1.append("Invalid")

print(f"List1: {list1}")





str1 = re.sub("[^01]", "", str1)
print(f"Cleaned Input: {str1}")

list2 = []

if len(str1) % 24 != 0:
    print("Error: Binary string length must be a multiple of 24")


r = int(str1[0:8], 2)
g = int(str1[8:16], 2)
b = int(str1[16:24], 2)
list2.append((r, g, b))


list2 = str(list2)
list2 = list2.replace("[", "")
list2 = list2.replace("]", "")
list2 = list2.replace("(", "")
list2 = list2.replace(")", "")
list2 = list2.replace(",", "")
print(f"List2: {list2}")
                                                                            # udělat z toho list


        
