def flatten(iterable):
    output = []
    result(iterable, output)
    return output


def result(item, output):
    for i in item:
        if type(i) is list:
            result(i, output)
        else:
            if i != None:
                output.append(i)
    return output
