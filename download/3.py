'''
function ：anomaly(x,a)
计算序列，数组距平。 
对x的a轴求距平。
x为序列或数组，
a为int；如1或(0,1)
'''
import numpy as np
def anomaly(x,a):
    y = x - x.mean(axis=(a))
    return y

###example###
import numpy as np
data = np.array([[1,3,6], [7,5,3]])
print(anomaly(data,0))
print(anomaly(data,(0,1)))