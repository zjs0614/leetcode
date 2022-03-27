class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        """
        1: 0-9
        2: 11 - 99


        3: 90
        101, 111, 121, .. 191
        202, 212, 222, .. 292
        909, 919, 929, .. 999

        4: 90
        1001, 1111, 1221, 1331, .. 1991
        2002, 2112, 2222, 2332, .. 2992
        9009, 9119, 9229, 9339, .. 9999

        5: 10 * 10 * 9 = 900 
        10001, 10101, 10201, 10301, .. 10901
        11011,                      .. 11911


        special case:
        intLength = 1
        """
        max_num = 10 ** intLength - 1
        min_num = 10 ** (intLength - 1)

        if intLength == 1:
            return [n if min_num <= n <= max_num else -1 for n in queries]

        counting_digis = int((intLength+1) / 2)
        starting_num = 10 ** (counting_digis - 1)

        res = []
        for query in queries:
            value = starting_num + query - 1
            value *= (10 ** (intLength - counting_digis))
            for i in range(intLength - counting_digis):
                num = int(value / (10 ** (intLength - i - 1))) % 10
                value += (num * (10 ** (i)))
            if min_num <= value <= max_num:
                res.append(value)
            else:
                res.append(-1)
        return res
