import stringutils

print("Give me 2 version and I return whether one is greater than, equal, or less than the other. As an example: '1.2' is greater than '1.1'")
str1 = input("First string:") 
str2 = input("Second string:")

res = stringutils.compare(str1, str2)
print(f"'{str1}' is equal to '{str2}'.") if res == 0 else (print(f"'{str1}' is greater to '{str2}'.") if res == 1 else print(f"'{str1}' is less than '{str2}'."))
