import numpy as np
np.percentile(a, q, axis=None, overwrite_input=False, interpolation='linear', keepdims=False)
#a : 输入数据，数组或序列；

#q : [0-100]之间的浮点数，所需计算的分位；

#axis : 指定计算平均的轴；

#overwrite_input : 是否重写覆盖原本数据，默认为False；

#interpolation : 所需分位数位于两个数据点之间时要使用的插值方法。可选：{'linear', 'lower', 'higher', 'midpoint', 'nearest'}，默认'linear'；

#keepdims : 是否保留维度，如果为True，计算后减少的维度将保留1的大小，默认为False。

###example###
import numpy as np
data = np.array([[1,3,6], [7,5,3]])
print(np.percentile(data, 50))
print(np.percentile(data, 50, axis=0, interpolation='lower'))
print(np.percentile(data, 50, axis=1))
print(np.percentile(data, 50, axis=1, keepdims=True))