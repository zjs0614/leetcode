class Solution:
    def decodeString(self, s: str) -> str:
        '''
        Sol1:
            step0: set res = ""
            step1:  loop letter l in s
                        if l is digit:
                            get string s in bracket (string index)
                            recursively call the same decode method, to get decoded string of s
                            res append l times of string s
            return res
        '''
        s, index = self.decodeStringRec(s)
        return s

    def decodeStringRec(self, s):
        res, index = "", 0
        while index < len(s):
            letter = s[index]
            if letter in ["1","2","3","4","5","6","7","8","9"]:
                try:
                    count_str = self.toCount(s, index)
                    open_index = index + len(count_str)
                    inner_str, close_index = self.decodeStringRec(s[open_index+1:])
                    res = res + (inner_str * int(count_str))
                    index = open_index + 1 + close_index + 1
                except:
                    print("string invalid")
            elif letter == "]":
                return res, index
            else:
                res = res + letter
                index += 1
        return res, index
        
    def toCount(self, s, index):
        count = ""
        while index < len(s) and s[index] in ["1","2","3","4","5","6","7","8","9","0"]:
            count += s[index]
            index += 1
        return count
        