class Solution:
    def topKFrequent(self, words, k: int):
        count_map = {}
        for word in words:
            if word in count_map:
                count_map[word] += 1
            else:
                count_map[word] = 1

        return sorted(count_map, key=lambda x: (len(words)-count_map[x], x), reverse=False)[:k]

