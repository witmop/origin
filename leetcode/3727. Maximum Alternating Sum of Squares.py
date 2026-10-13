class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        stack=[]
        some_stacks=[]

        for ind,el in enumerate(arr):
            stack.append(el)
            if sum(stack)>target:
                stack=[]
            elif sum(stack)==target:
                some_stacks.append(stack)
                stack=[]
        if len(some_stacks)>=2:
            some_stacks=sorted(some_stacks,key=lambda x: len(x))
            return len(some_stacks[0])+len(some_stacks[1])
        else: return -1
