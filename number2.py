def translate(text):
    type = ""
    for i in text:
        type += i
        if i in "bcdfghjklmnpqrstvwxz":
            type += 'o' + i
    return type

print(translate('this is fun'))