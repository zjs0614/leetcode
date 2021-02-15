class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        MIN_LENGTH = 5

        # special cases
        while num1[0] == "0" and len(num1) > 1:
            num1 = num1[1:]
        while num2[0] == "0" and len(num2) > 1:
            num2 = num2[1:]
        if num1 == "0" or num2 == "0":
            return "0"
        if num1 == "1":
            return num2
        if num2 == "1":
            return num1
        
        left, right, left_length = "0", "0", 0
        if len(num1) > MIN_LENGTH:
            mid = int(len(num1) / 2)
            left_length = len(num1) - mid
            left = self.multiply(num2, num1[0:mid])
            right = self.multiply(num2, num1[mid:])
        elif len(num2) > MIN_LENGTH:
            mid = int(len(num2) / 2)
            left_length = len(num2) - mid
            left = self.multiply(num2[0:mid], num1)
            right = self.multiply(num2[mid:], num1)
        else:
            return str(int(num1) * int(num2))
        res, i, j, inc = "", len(left)-1, len(right)-1, 0
        while i >= 0 or j >= 0:
            if left_length > 0:
                if j >= 0:
                    res = right[j] + res
                else:
                    res = "0" + res
                left_length -= 1
            else:
                v_r = 0 if j < 0 else int(right[j])
                v_l = 0 if i < 0 else int(left[i])
                val = v_l + inc + v_r
                inc = 1 if val >= 10 else 0
                res = str(val%10) + res
                i -= 1
            j -= 1
        if inc > 0:
            res = "1" + res
        while res[0] == "0" and len(res) > 1:
            res = res[1:]
        return res
