class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda x: (-x[0],x[1]))
        for i in range(1, len(people)):
            person = people[i]
            self.reorder(people, i, person[1])
        return people

    def reorder(self, people, i, j):
        if j < i:
            person = people[i]
            while j < i:
                people[i] = people[i-1]
                i -= 1
            people[i] = person