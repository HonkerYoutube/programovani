print("")
print("")
print("how many times do you want to repeat this?")
repeat = int(input())
print("")

previous_number = 0
number = 1
next_number = 0 

for i in range(repeat):
    
      #neví se
    next_number = number + previous_number
    previous_number = number
    number = next_number
    
    print(f"number: {number}   loop num: {i + 1}")