
#
import re
phone = '123-456-7890'
pattern = r'^\d{3}-\d{3}-\d{4}$'
if re.search(pattern, phone):
    print("The string matches the pattern.")
else:
    print("The string does not match")

#
line = 'the dog and cat'
result = re.sub(r'(.*)(dog)(.*)', r'\1fox\3', line)
print(result)

#
date = '12/25/05'
result = re.sub(r'(\d\d)/(\d\d)/(\d\d)', r'20\3-\1-\2', date)
print(result)

#
# \w+\.(png|gif|jpg)
# (4\d{15}|(5[1-5]\d{14})|3[4-7]\d{13})
# ISBN [01][\s-]\d{5}[\s-]\d{3}[\s-][0-9X]
# -?\d+(,\d{3})*(\.\d+)?(e-?\d+)?
# 1[\s-\?\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}
