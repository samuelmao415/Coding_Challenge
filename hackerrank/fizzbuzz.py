10 %2
n = 15

for i in range(1, n+1):

    if i % 15 ==0:
        print('FizzBuzz')
    elif i %3 == 0:
        print('Fizz')
    elif i % 5 ==0:
        print('Buzz')

    else:
        print(i)


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list_output = []
        for i in range(1, n+1):

            if i % 15 ==0:
                list_output.append('FizzBuzz')
            elif i %3 == 0:
                list_output.append('Fizz')
            elif i % 5 ==0:
                list_output.append('Buzz')
            else:
                list_output.append(str(i))
        return(list_output)
