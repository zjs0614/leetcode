class Solution:
    def getCombination(self, letters, num, careOrder):
        res = []
        for index, letter in enumerate(letters):
            sublist = self.getCombination(letters[index:] if careOrder else letters, num - 1, careOrder) if num > 1 else [""]
            for c in sublist:
                res.append(letter + c)
        return res

    def letterCombinations(self, digits: str) -> List[str]:
        letter_map = {
            "2": ['a','b','c'],
            "3": ['d','e','f'],
            "4": ['g','h','i'],
            "5": ['j','k','l'],
            "6": ['m','n','o'],
            "7": ['p','q','r','s'],
            "8": ['t','u','v'],
            "9": ['w','x','y','z'],
        }
        CARE_ORDER = False
        num_count_map = {}
        for digit in digits:
            if digit in num_count_map:
                num_count_map[digit] = num_count_map[digit] + 1
            else:
                num_count_map[digit] = 1
        res = []
        for digit in num_count_map:
            combination = self.getCombination(letter_map[digit], num_count_map[digit], CARE_ORDER)
            tmp = []           
            if len(res) > 0:
                for c1 in res:
                    for c2 in combination:
                        tmp.append(c1+c2)
            else:
                tmp = combination
            res = tmp
        return res