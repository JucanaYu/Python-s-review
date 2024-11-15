site={'Google','Baidu','Aliyun','Bytedance','Google'}   #用{}来表示一个集合，set()表示一个空集合，{ }表示一个空字典
print(site)

if 'Google' in site:
    print('在集合中')
else:
    print('不在集合中')

#集合还可以用作交集、并集等操作
a = set('abracadabra')
b = set('alacazam')

print(a)    #去重之后的字符串a
print(b)    #去重之后的字符串b
print("--------------------------------------")
print(a)
print(a - b)     # a 和 b 的差集
print(a | b)     # a 和 b 的并集
print(a & b)     # a 和 b 的交集
print(a ^ b)     # a 和 b 中不同时存在的元素
print(type(a))