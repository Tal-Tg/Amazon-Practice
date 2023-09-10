
nums = [2,7,6,3]
target = 9

def twoSum(nums, target):
    length = len(nums)
    for index, value in enumerate(nums):
        for index2,value2 in enumerate(nums):
            if nums[index] + nums[index2] == target:
                print(f"nice: { nums[index]}  {nums[index2]} in target: {target}")
                
            
                
twoSum(nums,target)


