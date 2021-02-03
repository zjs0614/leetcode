class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        skypoints, up, max_height = [], True, height[0]
        for i, h in enumerate(height):
            max_height = max_height if max_height > h else h
            if h == 0:
                continue
            if len(skypoints) == 0:
                skypoints.append(i)
            else:
                lastPoint = skypoints[-1]
                if height[lastPoint] < h and up:
                    skypoints.append(i)
                elif height[lastPoint] < h and not up:
                    while len(skypoints) >= 2 and height[skypoints[-1]] <= height[skypoints[-2]] and h > height[skypoints[-1]]:
                        skypoints.pop()
                    skypoints.append(i)
                    up = h >= max_height 
                elif height[lastPoint] > h and up:
                    skypoints.append(i)
                    up = False
                elif height[lastPoint] > h and not up:
                    skypoints.append(i)
                elif height[lastPoint] == h:
                    skypoints.append(i)
        res, skypoint_count = 0, 0
        for i, h in enumerate(height):
            if skypoint_count >= len(skypoints):
                break;
            if i == skypoints[skypoint_count]:
                skypoint_count += 1
                continue
            if skypoint_count < len(skypoints) and skypoint_count > 0:
                if height[skypoints[skypoint_count]] > height[skypoints[skypoint_count-1]]:
                    res += (height[skypoints[skypoint_count-1]] - h)
                elif height[skypoints[skypoint_count]] <= height[skypoints[skypoint_count-1]]:
                    res += (height[skypoints[skypoint_count]] - h)
        return res