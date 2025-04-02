#把一个类作为一个迭代器，需要在类里面实现两个方法，__iter__()和__next__()
class NumberSequenceIterator:
    #初始化迭代器，设置初值
    def __init__(self,start,end):
        self.start=start
        self.end=end

    #__iter__()返回一个迭代器对象
    def __iter__(self):
        return self
    
    #__next__()方法返回迭代器的下一个值
    def __next__(self):
        if self.start>self.end:
            raise StopIteration
        result=self.start
        self.start+=2
        return result

    
numbersequence=NumberSequenceIterator(1,5)

for i in numbersequence:
    print(i)