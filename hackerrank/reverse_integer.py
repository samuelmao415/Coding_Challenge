

# Slice notation "[a:b:c]" means "count in increments of c starting at a inclusive, up to b exclusive".
x = -123
reverse(x)


#solution one
def reverse(x):
    if x>=0:
        x = str(x)
        output = int(x[::-1])
    else:
        x = str(x)
        output = int('-'+x[:0:-1])
    if (-2**31 < output < 2**31 - 1):
        result = output
    else:
        result = 0
    return(result)
