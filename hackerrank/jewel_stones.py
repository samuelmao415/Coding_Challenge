J = "aA"
S = "aAAbbbb"

jewels = [j for j in J]
stones = [s for s in S]

jewel_dict = dict.fromkeys(jewels , 0)
for stone in stones:
    if jewel_dict.get(stone) != None:
        jewel_dict[stone] += 1

sum(jewel_dict.values())


class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        jewels = [j for j in J]

        stones = [s for s in S]


        jewel_dict = dict.fromkeys(jewels , 0)
        for stone in stones:
            if jewel_dict.get(stone) != None:
                jewel_dict[stone] += 1

        output = sum(jewel_dict.values())
        return(output)
