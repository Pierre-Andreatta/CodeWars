def get_middle(s):
    nb = len(s)
    re = nb/2
    if nb % 2 == 1:
        text = s[int(re-0.5):int(re+0.5)]
    else:
        text = s[int(re-1):int(re+1)]
    return text