kruh1="-"
kruh2="--"
kruh3="---"
a=[kruh3]  #věž 1
b=[kruh1]  #věž 2
c=[kruh2]  #věž 3

def obrázek():
    print(f"    |        |       |")
    print(f"    |        |       |")
    print(f" {kruh3}|{kruh3}    {kruh1}|{kruh1}    {kruh2}|{kruh2}")

command=str(input())
print(command)
if command == "a-b" or "a b" or "ab":
    