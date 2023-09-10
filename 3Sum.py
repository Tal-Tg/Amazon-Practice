nums = [-1,0,1,2,-1,-4]
# nums = [0,0,0]

def threeSum(nums):
    # better code review
    
    output= []
    nums.sort();
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:continue
        l =i+1
        r= len(nums)-1
        while (l < r):
            if nums[i]+ nums[l]+nums[r] == 0:
                output.append([nums[i], nums[l],nums[r]])
                while (l < r and nums[l] == nums[l+1]):
                    l+=1
                while (l < r and nums[r] == nums[r-1]):
                    r-=1
                l+=1
                r-=1
            elif nums[i]+ nums[l]+nums[r] > 0:
                r-=1
            else:
                l+=1
    return output;

print(threeSum(nums));



# your code working

    # for i in range(0, len(nums)):
    #     for j in range(0, len(nums)):
    #         for k in range(0, len(nums)): 
    #             if nums[i]+nums[j]+nums[k] == 0:
    #                 print(nums[i],nums[j],nums[k])
    #                 break;
    # return