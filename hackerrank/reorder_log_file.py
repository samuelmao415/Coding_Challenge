logs =  ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
logs =["t kvr", "r 3 1", "i 403", "7 so", "t 54"]
logs =["j je", "b fjt", "7 zbr", "m le", "o 33"]
class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        #number_str = [str(x) for x in range(0,11)]

        letter_list,digit_list = [],[]
        for i,log in enumerate(logs):
            if log.split()[1].isdigit():
                digit_list.append(log)
            else:
                letter_list.append(log)

        letter_list.sort(key = lambda x: (x.split()[1:],x.split()[0] ))


        return(letter_list + digit_list)
