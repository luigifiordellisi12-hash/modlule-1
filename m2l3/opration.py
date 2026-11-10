class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
apple = fruit("apple", "red")
print(apple.name)




class student:
    grade = 10
    name = "peguin"
    def introduction(self):
        print("hi i am student")
    def details(self):
            print("my name is", self.name)
            print("i study in grade", self.grade)
ob = student()
ob.introduction()
ob.details()



class parrot:
     species = "bird"
     def __init__(self, name, age):
          self.name = name
          self.age = age
blu = parrot("blu", 10)
woo = parrot("woo", 15)
print("blu is a {}". format(blu.species))
print("woo is also {}".format(woo.species))
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))

        