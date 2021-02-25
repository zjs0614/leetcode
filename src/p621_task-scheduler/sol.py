class Solution:
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