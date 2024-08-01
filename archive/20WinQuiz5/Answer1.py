
def removeDuplicates(string):
    if len(string) == 0:
        return ""
    elif len(string) == 1:
        return string[0] + string[1:]
    else:
        if string[0] == string[1]:
            return removeDuplicates(string[1:])
        else:
            return string[0] + removeDuplicates(string[1:])


print(removeDuplicates('greeeetinnngs'))