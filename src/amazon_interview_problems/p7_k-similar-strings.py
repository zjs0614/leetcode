class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        if len(A) != len(B):
            return -1
        if len(A) == 0:
            return 0
        count = [0] * 6
        a = []
        b = []
        for letter in A:
            count[ord(letter)-ord('a')] += 1
            a.append(letter)
        for letter in B:
            count[ord(letter)-ord('a')] -= 1
            b.append(letter)
        for c in count:
            if c > 0 or c < 0:
                return -1
        return self.findKSimilarity(a, b)
    
    def findKSimilarity(self, A, B):
        if A == B:
            return 0
        if len(A) == 2:
            return 1
        if A[0] == B[0]:
            return self.findKSimilarity(A[1:], B[1:])
        p = 0
        find = []
        for i, letter in enumerate(A[1:]):
            if letter == B[0]:
                if A[0] == B[i+1]:
                   p = i+1
                   break 
                find.append(i+1)
        p = find[0] if len(find) > 0 and p == 0 else p
        A[0], A[p] = A[p], A[0]
        return 1 + self.findKSimilarity(A[1:], B[1:])
sol = Solution()

print(sol.kSimilarity("aabccb", "bbcaca"))