# CSE 101 DongYoon Lee
# Email: dongyoon.lee.1@stonybrook.edu

def scrabble_sort(strings):
    for i in range(1, len(strings)):
        move_left1(strings, i)

    for k in range(1, len(strings)):
        if len(strings[k - 1]) == len(strings[k]):
            move_left2(strings, k)


def move_left1(a, j):
    x = a.pop(j)
    while j > 0 and len(a[j-1]) > len(x):
        j -= 1
    a.insert(j, x)

def move_left2(a, j):
    x = a.pop(j)
    while j > 0 and len(a[j-1]) == len(x) and a[j-1] > x:
         j -= 1
    a.insert(j, x)

a = ['contraceptive', 'strumpet', 'grownup', 'copybook', 'transcend', 'gasser', 'perishing', 'duopsony', 'boottopping', 'arpeggios', 'encephalograph',
     'rower', 'calyciform', 'thrombose', 'scanned', 'eider', 'upturn', 'hypnology', 'antisubmarine', 'droplike']
b = ['standoffishness', 'noggin', 'fridge', 'bactericide', 'impregnator', 'reapportion', 'tryingly', 'watchdog', 'wangling', 'multiplex',
     'inspirit', 'tuberosities', 'rarefier', 'sellout', 'alfa', 'prize', 'viral', 'foxberry', 'torridly', 'beadily']
#Test case 1
scrabble_sort(a)
print(a)

#Test case 2
scrabble_sort(b)
print(b)