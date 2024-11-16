#字典里面的键必须是唯一的，但是值可以是重合的
tinydict2 = { 'abc': 123, 98.6: 37 }
print(tinydict2)

#对字典的增加
dict={'name':'lihua','age':18}
print("原字典：",dict)
dict['gender']='M'
print("添加之后的新字典:",dict)

#对字典内容的删除
del dict['gender']
print("删除之后的新字典",dict)

#对字典内容的修改方法一
dict['age']=24
print("修改之后的新字典：",dict)

#对字典内容的修改方法二
dict.update({"age":18})
print("修改之后的新字典：",dict)

#对字典的键遍历
print("-----------------------")
print("对键遍历：\n")
for i in dict:
    print(i)

#对字典的值遍历
print("---------------------")
print("对值遍历：\n")
for i in dict.values():
    print(i)
