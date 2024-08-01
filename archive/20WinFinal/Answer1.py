
# 1.1
# 20 / 8
print(20 / 8)
# 1.2
#

# 1.3
#

# 1.4
# b
#a = {}
#a[[1,2,3]] = 4
#print(a)

# 1.5
# b

# 1.6
#

# 1.7
#

# 1.8
# 26, 49, 38

# 1.9
string = 'Hello Byung'
other = 'I am Alice'
result = string[:5] + other[-6:]
print(result)

# 1.10
for i in range(200, 96, -4):
    print(i)

# 1.11
import re
answer = r'\w+[\.\w+]?[@]\w*\.(edu|com)$'
guess = []
guess.append('test123@stonybrook.edu')
guess.append('some.name@gmail.com')
guess.append('a@b.com')
guess.append('shouldfail@home.org')
guess.append('no spaces allowed @gmail.com')
for i in guess:
    if re.search(answer, i):
        print('True')
    else:
        print('False')
