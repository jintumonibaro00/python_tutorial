Cat_Name = []

while True:
    print("Enter Cat name" +  str(len(Cat_Name) + 1) + "(enter nothing to exit)")

    name = input()

    if name == "":
        break
    Cat_Name = Cat_Name + [name]

print("The Cat Names are: ")
for name in Cat_Name:
    print(" " + name)
