def square_digits(num):
    s = ''
    for i in str(num):
        s += str(int(i)**2)
    return int(s)