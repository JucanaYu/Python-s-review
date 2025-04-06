def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    len_nums=len(nums)
    for i in range(k):
        nums.insert(0,nums[len_nums-1])
        del nums[len_nums]
    print(nums)
        

if __name__ == "__main__":
    nums=[1,2,3,4,5,6,7]
    k=3
    rotate(nums,k)