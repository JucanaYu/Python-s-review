def intersect(nums1, nums2):
    point1=0
    point2=0
    sum=[]
    len_nums1=len(nums1)
    sorted_nums1=sorted(nums1)
    len_nums2=len(nums2)
    sorted_nums2=sorted(nums2)
    while point1<len_nums1 and point2 < len_nums2:
        if sorted_nums1[point1]==sorted_nums2[point2]:
            sum.insert(0,sorted_nums1[point1])
            point1+=1
            point2+=1
        else:
            if sorted_nums1[point1] > sorted_nums2[point2]:
                point2+=1
            else:
                point1+=1
    return sum

if __name__ == "__main__":
    nums1=[1,2,2,1]
    nums2=[2,2]
    sum=intersect(nums1,nums2)
    print(sum)