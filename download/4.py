#标准差：

import numpy as np
np.std(a, axis=None, dtype=None, ddof=0, keepdims= Fales)
#方差：

np.std()**2

#a : 输入数据，数组或序列；

#axis : 指定计算平均的轴；

#dtype : 指定数据类型，默认为'float64'；

#ddof : 表示自由度。计算中使用的除数是N - ddof，N为元素个数，默认ddfo为0；

#keepdims : 是否保留维度，如果为True，计算后减少的维度将保留1的大小，默认为False。

###example###
import numpy as np
data = np.array([1,3,6,7,5,3])
print(np.std(data,0))