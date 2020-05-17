#原函数：
from scipy import stats
stats.linregress(x, y)
#输入：

#x:输入数据1(1维序列)

#y:输入数据2(1维序列)

#返回：

#slope：回归斜率

#intercept：回归截距

#r-value ：相关系数

#p-value ：假设检验的双侧p值，其零假设是斜率为零

#stderr ：标准误差估计

#同相关系数一致，该函数优点在于可以直接输出P值，省去了再次计算置信区间的步骤，缺点在于仅适用于两个一维序列。

#改进：将以下内容复制进*.py文件，与使用脚本放在同一文件夹内，通过import * 调用。

'''
function ：linearregress(x,y,opt)
计算x与y的相关系数，及其双尾P值。 
x必须为一维数组
y可以为一维数组或三维数组，若y为一维数组，opt为1，计算两序列线性回归；
若y为三维数组，则时间维度必须在最左边，即axis=0，opt =2，计算序列和场的线性回归。
返回slope, intercept, r_value, p_value, std_err
'''
import numpy as np
from scipy import stats
from numba import jit
@jit
def linearregress(x,y,opt):
    if opt==1:
        slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    elif opt ==2:
        lat = y.shape[1]
        lon = y.shape[2]
        slope, intercept, r_value, p_value, std_err = np.zeros((lat,lon)),np.zeros((lat,lon)),np.zeros((lat,lon)),np.zeros((lat,lon))
        for i in range(lat):
            for j in range(lon):
                slope[i,j], intercept[i,j], r_value[i,j], p_value[i,j], std_err[i,j] = stats.linregress(x,y[:,i,j])
    return slope, intercept, r_value, p_value, std_err