def solution(roman):
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    rom_sym = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    rom_int = ''
    i = 0
    while  roman > 0:
        for _ in range(roman // val[i]):
            rom_int += rom_sym[i]
            roman -= val[i]
        i += 1

    return rom_int