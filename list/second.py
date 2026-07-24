def coma_code(item):
    if len(item) == 0:
        return ""
    elif len(item) == 1:
        return item[0]
    else:
        return ", ".join(item[:-1]) + " and " + item[-1]

spam = ['apples', 'bananas', 'tofu', 'cats']
print(coma_code(spam))
