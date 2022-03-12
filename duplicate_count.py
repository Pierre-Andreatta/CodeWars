def duplicate_count(text):
    text = text.lower()
    lst = ''
    for i in text:
        if text.count(i) >1:
            if i not in lst:
                lst += i
    return len(lst)