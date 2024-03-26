def from_number_to_flower(x):
    if x == 0:
        return "setosa"
    elif x == 1:
        return "versicolor"
    else:
        return "indica"


def floatingg(listt):
    abc = []
    for itemm in listt:
        abc.append(float(itemm))
    return abc
