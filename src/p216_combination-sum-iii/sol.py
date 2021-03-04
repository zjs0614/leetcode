class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''
        k: 2-9
        n: 1-60
        {i}: 1-9

        cases:
            (1) n < k(1+k)/2 return []
            (2) n == k(1+k)/2 return [[1,2,..,k]]
            (3) n > (19-k)k/2 return []
            (4) n == (19-k)k/2 return [[9,8,..,9-k+1]]
        '''
        return self.find(k, n, 1)

    
    def find(self, k, n, start):
        if k > 9 - start + 1:
            return []
        if n < k*(start+start+k-1)/2 or n >(19-k)*k/2:
            return []
        if n == k*(start+start+k-1)/2:
            return [list(range(start,start+k))]
        if n == (19-k)*k/2:
            return [list(range(9-k+1, 10))]
        if k == 1:
            if n >= start and n <= 9:
                return [[n]]
            else:
                return []
        res = []
        while start <= 9 - k + 1:
            local_res = self.find(k-1, n-start, start + 1)
            for combination in local_res:
                combination.append(start)
            res.extend(local_res)
            start += 1
        return res

