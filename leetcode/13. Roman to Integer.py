class Solution:
    def romanToInt(self, s: str) -> int:
        data={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        stack=[]
        result=0
        for el in s:
            if len(stack)==0:
                stack.append(el)
            elif data[stack[-1]]<data[el]:
                result+=data[el]-data[stack[-1]]
                stack.pop()
            else:
                result+=data[stack[-1]]
                stack.pop()
                stack.append(el)
        if len(stack)!=0:
            result+=data[stack[-1]]
        return result