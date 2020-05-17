#原函数
from scipy.stats import pearsonr
pearsonr(x,r)
#输入：

#x:输入数据1(1维序列)

#y:输入数据2(1维序列)

#返回：

#r：皮尔逊相关系数

#p-value ：双尾P值

#该函数优点在于可以直接输出P值，省去了再次计算置信区间的步骤，缺点在于仅适用于两个一维序列。

#改进： 将以下内容复制进*.py文件，与使用脚本放在同一文件夹内，通过import * 调用。


'''
function ：escorc(x,y,opt)
计算x与y的相关系数，及其双尾P值。 
x必须为一维数组
y可以为一维数组或三维数组，若y为一维数组，opt为1，计算两序列相关系数；
若y为三维数组，则时间维度必须在最左边，即axis=0，opt =2，计算序列和场的相关关系分布。
返回r,t
'''
import numpy as np
from scipy.stats import pearsonr
from numba import jit
@jit
def escorc(x,y,opt):
    if opt==1:
        r,p = pearsonr(x,y)
    elif opt ==2:
        lat = y.shape[1]
        lon = y.shape[2]
        r,p = np.zeros((lat,lon)),np.zeros((lat,lon))
        for i in range(lat):
            for j in range(lon):
                r[i,j],p[i,j] = pearsonr(x,y[:,i,j])
    return r,p