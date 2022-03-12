def solution(s):
    lst = []
    if len(s)%2 == 1:
        s+="_"
    for i in range(len(s)):
            if i %2 == 0:
                lst.append(s[i:i+2])
    return lst