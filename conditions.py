x = 2
print(x == 2)
print(x < 3)

name = "John"
age = 23

if name == "John" and age == 23:
    print("John has been identified!")

if name == "John" or name == "Rick":
    print("John OR Rick is found")

if name in ["John", "Rick"]:
    print("Name found")
elif name == "Sandra":
    print("Sandra found")
else:
    print("Nothing found")

# IS
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)

# NOT
print(not True)