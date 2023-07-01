def is_valid(isbn):
    formula = []
    for i in isbn:
        if i.isnumeric():
            formula.append(int(i))
        elif i == "-":
            isbn.replace("i", "")
        elif i == "X" and isbn.index(i) == len(isbn) - 1:
            formula.append(10)
        else:
            return False
    if len(formula) != 10:
        return False
    else:
        check = 0
        for b in range(1, 11):
            check += formula[b - 1] * b
        resault = check % 11 == 0
        return resault
