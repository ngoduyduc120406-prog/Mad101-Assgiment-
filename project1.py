def next_string(s):
    s = list(s)

    for i in range(len(s)-1, -1, -1):
        if s[i] != 'd':
            s[i] = chr(ord(s[i]) + 1)
            return ''.join(s)
        else:
            s[i] = 'a'

    return 'a' * (len(s) + 1)
Amane
def is_wavy(s):
    for i in range(len(s)-1):
        if i % 2 == 0:
            if s[i] >= s[i+1]:
                return False
        else:
            if s[i] <= s[i+1]:
                return False
    return True


def next_wavy(s):
    s = next_string(s)
    while not is_wavy(s):
        s = next_string(s)
    return s
Amane
def count_wavy_before(s):
    cur = 'a' * len(s)
    count = 0

    while cur < s:
        if is_wavy(cur):
            count += 1
        cur = next_string(cur)

    return count
Amane
from itertools import product

def count_contains(n, sub):
    letters = ['a','b','c','d']
    count = 0

    for p in product(letters, repeat=n):
        s = ''.join(p)
        if sub in s:
            count += 1

    return count
