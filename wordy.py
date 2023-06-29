def rotate(text, key):
    list = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    new = ""
    for i in text:
        if i in list:
            index = list.index[i] + key + 1
            if index > 25:
                index = index - 26
            new += list[index]
        else:
            new += i
    return new


hi = rotate("a", 1)
print(hi)
