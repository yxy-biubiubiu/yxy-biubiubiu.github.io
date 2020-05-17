'''
function ：standardized(x,a)
将数据标准化。 
对x的a轴标准化。
x为序列或数组，
a为int；如1或(0,1)
'''
import numpy as np
def standardized(x,a):
    y = (x - x.mean(axis=(a)))/x.std(axis=(a))
    return y

#x为任意形状数组，函数对x的a轴进行标准化，

#a为int型；如1或(0,1)。