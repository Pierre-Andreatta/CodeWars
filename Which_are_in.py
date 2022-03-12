def in_array(array1, array2):
    return sorted(list(dict.fromkeys(s1 for s1 in array1 if any(s1 in s2 for s2 in array2))))