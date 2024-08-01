# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

def removeDuplicates(string):
    if len(string) == 0:
        return ""
    else:
        if string.count(string[0]) == 1:
            return string[0] + str(removeDuplicates(string[1:]))
        else:
            return str(removeDuplicates(string[1:]))


print(removeDuplicates("greeeeetinnnngs"))
