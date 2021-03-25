class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        DIRRECTION_COUNT = 4
        step_count = [0] * DIRRECTION_COUNT
        current_direction = 0

        for _ in range(4):
            for i in instructions:
                if i == "G":
                    step_count[current_direction] += 1
                elif i == "L":
                    current_direction -= 1
                elif i == "R":
                    current_direction += 1
                if current_direction >= len(step_count):
                    current_direction = current_direction % DIRRECTION_COUNT
                elif current_direction < 0:
                    current_direction += DIRRECTION_COUNT
        
        return step_count[0] == step_count[2] and step_count[1] == step_count[3]