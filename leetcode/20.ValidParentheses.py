#20 Задание LeetCode
class Solution:
    def isValid(self, s: str) -> bool:
        data={")":"(","]":"[","}":"{"}
        opening="([{"
        stack=[]
        for el in s:
            if len(stack)==0:
                stack.append(el)
            elif el in opening:
                stack.append(el)
            elif stack[-1]!=data[el]:
                return False
                break
            else:stack.pop()
        if len(stack)!=0:return False
        else:return True