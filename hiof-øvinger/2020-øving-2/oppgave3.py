my_list = ["H", "I", "O", "F"]
my_string1 = "H:I:O:F"
my_string2 = "HIOF"

# a)
print("".join(my_list))

# b)
string_as_list = my_string1.split(":")
print(string_as_list)

# c)

list = []
for letter in my_string2:
    list.append(letter)
print(list)

string2_as_list = [x for x in my_string2]
print(string2_as_list)