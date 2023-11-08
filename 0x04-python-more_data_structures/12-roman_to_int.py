#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convert roman number to decimal

    Args:
        roman_string: roman number representation

    Return:
        Converted decimal if successful
        else 0
    """
    if (not roman_string) or not isinstance(roman_string, type("str")):
        return 0
    roman_dict = dict({("I", 1), ("V", 5), ("X", 10), ("L", 50),
                      ("C", 100), ("D", 500), ("M", 1000)})
    rm_cp = list(map(lambda x: x, roman_string))
    # check for roman string
    for str in roman_string:
        if str not in list(roman_dict.keys()):
            return 0
    # check consequetive roman literals rule
    for cr in rm_cp:
        occ = rm_cp.count(cr)
        idx_1 = rm_cp.index(cr)
        con = 0
        for i in range(occ):
            try:
                idx_2 = rm_cp.index(cr)
            except ValueError:
                continue
            if idx_1 == idx_2:
                con += 1
                rm_cp.pop(idx_2)
                if con > 3:
                    raise TypeError
                ("no consequative roman letters more than 3")

            elif idx_1 != idx_2:
                idx_1 = idx_2
                con = 1
    rm_int = list(map(lambda x: roman_dict.get(x), roman_string))
    rm_int.append(0)
    sum = 0
    for elm in range(len(rm_int)-1):
        if rm_int[elm] < rm_int[elm + 1]:
            sum -= rm_int[elm]
        else:
            sum += rm_int[elm]
    return sum
