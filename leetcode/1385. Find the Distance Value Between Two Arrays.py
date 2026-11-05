class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        result=0
        flag=False
        seen_true=set()
        seen_false=set()
        for el1 in arr1:
            for el2 in arr2:
                if el1 in seen_true:
                    result+=1   
                    flag=True
                    break
                elif abs(el1-el2)<=d:
                    flag=True
                    seen_false.add(el1)
                    break
            if not(flag):
                result+=1
                flag=False
                seen_true.add(el1)
            else:flag=False
        return result

