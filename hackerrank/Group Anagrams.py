strs = ["eat","tea","tan","ate","nat","bat"]


dict((key, []) for key in new_strs)


new_strs = [''.join(sorted(x)) for x in strs]


new_strs
str_dict = {}#dict((key, []) for key in new_strs)

'aes' in str_dict

for i in strs:
    if ''.join(sorted(i)) in str_dict.keys():
        #str_dict[''.join(sorted(i))].append(i)
        str_dict.get(''.join(sorted(i))).append(i)
    else:
        str_dict[''.join(sorted(i))] = [i]

list(str_dict.values())


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """


        #new_strs = [''.join(sorted(x)) for x in strs]

        str_dict = dict((key, []) for key in [''.join(sorted(x)) for x in strs])

        for i in sorted(strs):
            if ''.join(sorted(i)) in str_dict.keys():
                str_dict[''.join(sorted(i))].append(i)

        return(list(str_dict.values()))
