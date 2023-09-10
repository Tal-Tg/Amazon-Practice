nums1 = [2,3,5,10]
nums2 = [1,6,8,9]



def whoIsTheKingAndMedian(nums1,nums2):
    newArr = []
    for item in nums1:
        newArr.append(item)
    for item in nums2:
        newArr.append(item)
    sortedArr = sorted(newArr);
    print(sortedArr)
    if len(sortedArr) % 2 == 0:
        print(sortedArr[int(len(sortedArr)/2-1)]+sortedArr[int(len(sortedArr)/2)])
    else: 
        print(sortedArr[int(len(sortedArr)/2)])
    return;

whoIsTheKingAndMedian(nums1,nums2);