class Person:
    name = "John"
    age = 30

    def function(self):
        print("This is inside a class")


john = Person()
alex = Person()

alex.name = "Alex"

print(john.name)
print(alex.name)
