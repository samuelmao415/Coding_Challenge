
x=10
x=121
isPalindrome(x)


def isPalindrome(x):
    str_x = str(x)
    rev_str_x = str_x[::-1]
    if str_x == rev_str_x:
        return(True)
    else:
        return(False)
