class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations=["+","-","*","/"]
        nums=[]
        for el in tokens:
            if el not in operations:
                nums.append(int(el))
            else:
                temp2=nums.pop()
                temp1=nums.pop()
                if el=="+":
                    nums.append(temp1+temp2)
                elif el=="-":
                    nums.append(temp1-temp2)
                elif el=="*":
                    nums.append(temp1*temp2)
                elif el=="/":
                    nums.append(int(temp1/temp2))
        return nums[0]
