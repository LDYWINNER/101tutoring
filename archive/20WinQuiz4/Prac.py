
def replaceLetter(string, letter, replacementLetter):
    if len(string) == 0:
        return ''
    elif string[0] == letter:
        return replacementLetter + replaceLetter(string[1:], letter, replacementLetter)
    elif string[0] != letter:
        return string[0] + replaceLetter(string[1:], letter, replacementLetter)
    
print(replaceLetter("test string", "t", "z"))
print(replaceLetter("mississipi", "i", "Q"))