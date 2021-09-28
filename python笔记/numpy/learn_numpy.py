import numpy as np

a = np.array([1, 3, 5])
#numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
#object：数组或嵌套的数列     dtype：数组元素的数据类型，可选   copy：对象是否需要复制，可选
#order： 创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）  subok：默认返回与基类型一致的数组
#ndmin：指定生成数组的最小维度

print(type(a))
#<class 'numpy.ndarray'>
print("a为：{}".format(a))
print("---end---")
b = np.array([[1, 2], [3, 4], [6, 5]])
#多维
print("b为：{}".format(b))
print("---end---")

c1 = np.array([1, 2, 3, 4, 5])
c2 = np.array([1, 2, 3, 4, 5], ndmin=3)
print(c1)
print("---end---")
print(c2)
print("---end---")

