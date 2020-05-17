import numpy as np

np.mean(a, axis=None, dtype=None)

np.nanmean(a, axis=None, dtype=None) 
#np.nanmean() 默认略过缺测值进行计算

#a : 输入数据，数组或序列；

#axis : 指定计算平均的轴，默认为全部数据的平均。如 axis=0;axis=(0,1)等；

#dtype : 指定数据类型，默认为'float64'。

###example###
import numpy as np
data = np.array([[1,2,3],[4,5,6]])
print(np.mean(data))
print(np.mean(data,axis = 0))
print(np.mean(data,axis = (0,1)))

data2 = np.array([1,np.nan,3,4,5,6])
print(np.mean(data2))
print(np.nanmean(data2))