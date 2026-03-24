def is_wavy(s):
    if len(s) < 2:
        return True
    for i in range(len(s)-1):
        if i % 2 == 0:
            if s[i] >= s[i+1]:
                return False
        else:
            if s[i] <= s[i+1]:
                return False
    return True

def count_wavy_before(s):
    k = len(s)
    if k == 0:
        return 0
    def rec(pos, prev, tight):
        if pos == k:
            return 1
        res = 0
        upper = s[pos] if tight == 1 else 'd'
        for ch in 'abcd':
            if ch > upper:
                continue
            if pos > 0:
                if (pos - 1) % 2 == 0:
                    if prev >= ch:
                        continue
                else:
                    if prev <= ch:
                        continue
            new_tight = 1 if tight == 1 and ch == s[pos] else 0
            res += rec(pos + 1, ch, new_tight)
        return res
    total = rec(0, '', 1)
    if is_wavy(s):
        total -= 1
    return total

if __name__ == "__main__":
    s = input().strip()
    print(count_wavy_before(s))
