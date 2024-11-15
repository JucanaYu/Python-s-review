str='0123456789'

print(str[0:-1])    #输出从第一个字符到倒数第二个字符
print(str[0])   #输出第一个字符
print(str[2:6]) #输出第三个字符到第六个字符
print(str[2:])  #输出从第三个字符之后的所有字符
print(str[1:5:2])   #输出从第二个到第五个且步长为2
print(str*2)    #输出字符串两次
print(str+' '+'hello')  #

print('----------------------------------------------')

#对转义字符的消除
print('hello\nworld')
print(r'hello\nworld')
