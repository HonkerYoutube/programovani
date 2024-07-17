import re

# to remove everything except 0, 1 use:
str1 = ""
str1 = re.sub("[^01]", "", str1)
#

# to slice string use:
str1 = "abcdef"
str1 = str1[3:5]   # 3.index až 5.index
#

# to know if there is remaider(zbytek) use:
num = 3
if num % 2 == 1:   # Vyjde 1, protože je to zbytek. To procento znamená operaci modulo
    print(f"zbytek: {num}")
#

# to replace number, letter or symbol use:
str1 = "abcdef"
str1 = str1.replace("d", "")   # udělá to nový string, takže to je funkce, která udělá nový string
#

