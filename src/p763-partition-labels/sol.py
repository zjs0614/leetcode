class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        group_index = [0] * 26
        group_count = 1
        for index, letter in enumerate(S):
            letter_index = ord(letter) - ord('a')
            if group_index[letter_index] == 0:
                group_index[letter_index] = group_count
                group_count += 1
            else:
                j = index - 1
                while j >= 0:
                    prev_letter = S[j]
                    if prev_letter == letter:
                        break
                    else:
                        group_index[ord(prev_letter) - ord('a')] = group_index[letter_index]
                    j -= 1

                group_count = group_index[letter_index] + 1
        
        res = [0] * (group_count-1)
        for i, l in enumerate(S):
            letter_index = ord(l) - ord('a')
            res[group_index[letter_index]-1] += 1
        return res