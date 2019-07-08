strs = ["flower","flow","flight",'flooring']
strs = ["dog","racecar","car"]
strs=[]
longestCommonPrefix(strs)


def longestCommonPrefix(x):
    if len(x) ==0:
        return('') #if empty input
    #sort by the shortest string and extract the length of that string
    shortest_str = len(sorted(strs, key= lambda x: len(x))[0])
    #a reverse while loop from the longest prefix to the shortest prefix
    counter=shortest_str
    output_array=[]
    while counter>0:
        prefix = [str[:counter] for str in strs]
        if [prefix[0]] * len(prefix) == prefix: #if the first element equals the whole element
            return(prefix[0])
            output.append(prefix)
        counter = counter -1
    #output array to check if there is no solution
    if len(output_array) ==0:
        return('')
