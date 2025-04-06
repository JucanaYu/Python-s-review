def plusOne(digits):
    sum=0
    for i in range(0,len(digits)):
        sum=sum*10+digits[i]
    sum+=1
    sum=[int(x) for x in str(sum)]
    # print(sum)
    return sum

if __name__ == "__main__":
    print(plusOne([1,2,3]))