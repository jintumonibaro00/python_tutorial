def displayInventory(inventory):
    print("Inventory:")
    item_total = 0

    for item, count in inventory.items():
        print(f"{count} {item}")
        item_total += count

    print("Total number of items:", item_total)


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory



inv = {
    'gold coin': 42,
    'rope': 1
}

displayInventory(inv)
dragonLoot = [
    'gold coin',
    'dagger',
    'gold coin',
    'gold coin',
    'ruby'
]


inv = addToInventory(inv, dragonLoot)

print("After looting and adding items: ")


displayInventory(inv)
