string = "ass"


def returnDictWithCharNo(str):
    charDict = {}
    for value in string:
        if value not in charDict:
            charDict[value] = 1
        else:
            charDict[value] += 1
    print(charDict)

    for key in charDict.keys():
        if charDict[key] == 1:
            return key
            break
        else:
            return "_"


print(returnDictWithCharNo(string))


def find_sum_of_two(A, val):
    found_values = set()
    for a in A:
        if val - a in found_values:
            print(found_values)
            return True

        found_values.add(a)

    return False


A = [2, 5, 6, 7, 2, 8, 9]
val = 8

print(find_sum_of_two(A, val))
