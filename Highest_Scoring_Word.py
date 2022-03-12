def high(x):
    res = {}
    for w in x.split()[::-1]:
        res[sum([ord(s) - 96 for s in w])] = w
    return res[max(res)]