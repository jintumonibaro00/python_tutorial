birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print("Enter a name: (Blank for quit)")

    name = input()

    if name == "":
        break 

    elif name in birthdays:
        print(birthdays[name] + f"is the birthday for {name}")

    else:
        print(f"I do not have the birthday details for {name}")

        print(f"Enter date for {name}")

        bday = input()

        birthdays[name] = bday

        print("Database updated")
