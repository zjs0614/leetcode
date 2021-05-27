class Solution:
    """
        Input: 
            - list of tasks [A,B,A,C,D] [1:10**4]
            - least cooldown units: n (>=0)
        Output:
            minimum units of time

        E.G: A,A,A,A,B,B,B,C,C,D

        Solution: Greedy, Schedule task

        - Form a count map:
            {A:4}, {B:3}, {C:2}, {D:1}
            task_size: 4

        init a board:
            - width: n+1
            - height: max(count_map)
        
        E.G. n = 2, max(count_map) = 4 ({A:4})
        X  X  X
        X  X  X
        X  X  X
        X  X  X

        1) fill in the most frequent task
            A X X
            A X X
            A X X
            A X X

            set:
                avail_size: (width-1)(height-1)
                task_bottom: 1
                extra_size: 0

        2) loop the rest sorted count_map:
            if task_count == height:
                task_bottom += 1
                avail_size -= (task_count - 1)
            else：
                avail_size -= task_count

            if avail_size < 0:
                extra_size += -avail_size
                avail_size = 0
        
        3) return (width)(height-1) + task_bottom + extra_size

        A B C
        A B C
        A B C
        A B D

      0 D E F
      1 D E F
      2 E F G

      3 G H I
      4 G H I

      5 J
      6 J
        
        extra rows for a new letter must less than original height
        so, we can re-order each row, to separate rows with same task too close, such as
        line 0 - 6
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks) <= 0:
            return len(tasks)

        letter_count_map = dict()
        for task in tasks:
            letter_count_map[task] = letter_count_map.get(task, 0) + 1
        sorted_tasks = sorted(letter_count_map.items(), key=lambda x: x[1], reverse=True)
        res = 0

        height = sorted_tasks[0][1]
        width = n + 1
        bottom_count = 1
        empty_space_left = (height - 1)*(width - 1)
        extra_size = 0
        for i in sorted_tasks[1:]:
            if i[1] == height:
                bottom_count += 1
                empty_space_left -= i[1] - 1
            else:
                empty_space_left -= i[1]
            if empty_space_left < 0:
                extra_size += -empty_space_left
                empty_space_left = 0
        return (width * (height - 1)) + bottom_count + extra_size