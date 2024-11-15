def reverseString(user_input):
    inputwords=user_input.split(" ")    #将user_input里面的字符串以空格进行分隔
    inputwords=inputwords[-1::-1]   #这里有三个参数，第一个参数代表最后一个元素，第二个参数表示一直移动到末尾，第三个参数表示逆向且步长为1

    output=' '.join(inputwords) #将inputword里面的每个成员用空格分隔，然后再拼接成一个字符串

    return output

if __name__=="__main__":
    user_input=input("输入一个字符串：")
    rw=reverseString(user_input)
    print('逆转的字符为:',rw)