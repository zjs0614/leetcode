class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def getKey(v1):
            v1_vals = v1.split(' ', 1)
            if v1_vals[1][0].isdigit():
                return 'b'
            else:
                return 'a' + v1_vals[1] + " " + str(len(v1_vals[1])) + " " + v1_vals[0]
        return sorted(logs, key=lambda x: getKey(x))