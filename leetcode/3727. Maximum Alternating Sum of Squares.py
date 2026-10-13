nums = [1,-1,2,-2,3,-3]
result=0
nums=sorted(map(lambda x: abs(x),nums))
min_nums=[]
max_nums=[]
min_nums=nums[:len(nums)//2]
max_nums=nums[len(nums)//2:]
max_length=max(len(min_nums),len(max_nums))
for el in range(max_length):
    if el <len(max_nums):
        result+=max_nums[el]**2
    if el< len(min_nums):
        result -=min_nums[el]**2
print(result)