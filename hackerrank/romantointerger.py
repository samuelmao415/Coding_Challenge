s = "MCMXCIV"
s="LVIII"
s="MCDLXXVI"
romanToInt(s)


def romanToInt(s):
    #dictionary for all the cases and exceptions
    roman_dict ={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
    ,'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
    #store arabic numbers from Roman numberals break-down
    numbers = []
    #divide the roman numerals into pairs and check if a pair is in the roman_dict
    pairs = [s[i:i+2] for i in range(0,len(s),1)]
    for pair in pairs:
        if roman_dict.get(pair) is not None and len(pair)==2:
            numbers.append(roman_dict.get(pair))
            s = s.replace(pair,'') #remove the pair from the original roman numeral string
    #divide the remaining roman numeral into single string
    single_str = [s[i:i+1] for i in range(0,len(s),1)]
    for single in single_str:
        numbers.append(roman_dict.get(single))
    print(numbers)
    #sum all the numbers from the numbers list
    output = sum(numbers)
    return(output)
