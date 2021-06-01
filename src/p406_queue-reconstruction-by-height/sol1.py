class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        Input:
            - people: list[list[hi, ki]]: length[1:2000], hi:[0,10**6], ki
        Output:
            - List[List[int]]: reconstruct

        Analysis:
            - sorting, inserting problem
            - linked list
            - O(n*n), sort first, insert sort linked list
        """
        people_new = sorted(people, key=lambda x: (-x[0], x[1]))
        for i, p in enumerate(people_new):
            h, k = p[0], p[1]
            if i > k:
                for j in range(k, i):
                    people_new[j], people_new[i] = people_new[i], people_new[j]
        return people_new
