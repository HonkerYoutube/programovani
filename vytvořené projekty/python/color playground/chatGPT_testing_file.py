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
print(f"Input: {input1}")

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
