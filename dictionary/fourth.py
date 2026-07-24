allGuests = {'Alice': {'apples': 5, 'pretzels': 12},'Bob': {'ham sandwiches': 3, 'apples': 2},'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guest , item):
    numBrought = 0 

    for k , v in guest.items():
        numBrought = numBrought + v.get(item , 0)
    return numBrought

print("Enter item to search: ")

item = input()
print(f"number of {item} brought is " + str(totalBrought(allGuests , item)) )

        
