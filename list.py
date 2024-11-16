list = ['red', 'green', 'blue', 'yellow', 'white', 'black','red']   #列表是允许重复元素的出现
print(list)
print( list[0] )
print( list[1] )
print( list[2] )

#使用append对列表内容进行添加
list.append('green')
print(list)

#使用del对列表内容进行删除
del(list[-1])
print(list)

