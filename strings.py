name = "William"
age = 30
print("Hello %s, you are %s years today!" % (name, age))

mylist = [1, 2, 3, 4]
print("A list: %s" % mylist)

print("Float %.4f" % float(5))

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)


# STRING OPERATIONS

astring = "ABCDEF GHIJK"
print(len(astring))

print(astring.index("D"))

print(astring.count("G"))

# Sliced syntax [start:stop:step]
print(astring[3:7:2])

# Reverse string
print(astring[::-1])

print(astring.upper())
print(astring.lower())

print(astring.split(" "))
