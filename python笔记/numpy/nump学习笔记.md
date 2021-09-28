# Numpy

[Numpy](http://www.numpy.org/)是Python中科学计算的核心库。它提供了一个高性能的多维数组对象，以及用于处理这些数组的工具。如果你已经熟悉MATLAB，你可能会发现[这篇教程](https://www.numpy.org.cn/user_guide/numpy_for_matlab_users.html)对于你从MATLAB切换到学习Numpy很有帮助。

## 文档地址

API地址：https://www.numpy.org.cn/reference/routines/

入门教程：https://www.numpy.org.cn/article/basics/an_introduction_to_scientific_python_numpy.html



导入包

import numpy as np 

查看numpy版本

```
ic(np.__version__)
ic| np.__version__: '1.20.3'
```

## 数组

numpy数组是一个值网格，所有类型都相同，并由非负整数元组索引。 维数是数组的排名; 数组的形状是一个整数元组，给出了每个维度的数组大小。

```
a = np.array([1,2,3])
创建一个一维数组

ic(type(a))
返回：ic| type(a): <class 'numpy.ndarray'>

ic(a.shape)
返回：ic| a.shape: (3,)
返回数组的维度数据，a是一个包含三个元素的数组

a[0] = 5
通过坐标修改数组

# Numpy还提供了许多创建数组的函数
    a = np.zeros((2,2))
    返回：ic| a: array([[0., 0.],
                  [0., 0.]])
    创建指定维度且全是0的数组

    b = np.ones((1,2))
    返回：ic| b: array([[1., 1.]])
    创建指定维度且全是1的数组
    
    c = np.full((2,2), 7)
    返回：ic| c: array([[7, 7],
              [7, 7]])
    创建指定维度且全是指定数字的数组
    
    d = np.eye(2)
    返回：ic| d: array([[1., 0.],
              [0., 1.]])
    创建一个2x2的矩阵
    
    e = np.random.random((2,2))
    返回：ic| e: array([[0.16105894, 0.05129068],
              [0.03014131, 0.26926341]])
    创建一个填充随机值的数组
```



## 数据索引

Numpy提供了几种索引数组的方法。

### 切片

    a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
    b = a[:2, 1:3]
    返回：ic| b: array([[2, 3],
                  [6, 7]])
    # :2取前两个0，1子数组
    # 1:3取子数组中索引为1和2的列
    
    ic(a[0, 1])
    返回：ic| a[0, 1]: 2
    通过索引取数
    
    b[0, 0] = 77
    返回：ic| b: array([[77,  3],
                  [ 6,  7]])
    # 修改原始数据


​    
​                       
​    

### 整数数组索引

使用切片索引到numpy数组时，生成的数组视图将始终是原始数组的子数组。 相反，整数数组索引允许你使用另一个数组中的数据构造任意数组。

```
a = np.array([[1,2], [3, 4], [5, 6]])
ic(a[[0, 1, 2], [0, 1, 0]])
返回：ic| a[[0, 1, 2], [0, 1, 0]]: array([1, 4, 5])
```



### 整数索引与切片索引混合使用

```
row_a1 = a[1, :]
返回：ic| row_a1: array([5, 6, 7, 8])
row_r2 = a[1:2, :]
返回：ic| row_r2: array([[5, 6, 7, 8]])

col_r1 = a[:, 1]
返回：ic| col_r1: array([ 2,  6, 10])
col_r2 = a[:, 1:2]
返回：ic| col_r2: array([[ 2],
                   [ 6],
                   [10]])
```

### 布尔数组索引

```
a = np.array([[1,2], [3, 4], [5, 6]])
bool_index = (a > 3)
返回:ic| bool_index: array([[False, False],
                       [False,  True],
                       [ True,  True]])
ic(a[bool_index])
返回：ic| a[bool_index]: array([4, 5, 6])
ic(a[a > 2])    
返回：ic| a[a > 2]: array([3, 4, 5, 6])
```

## 数据类型

每个numpy数组都是相同类型元素的网格。Numpy提供了一组可用于构造数组的大量数值数据类型。Numpy在创建数组时尝试猜测数据类型，但构造数组的函数通常还包含一个可选参数来显式指定数据类型。这是一个例子

```
x = np.array([1, 2]) 
ic| x.dtype: dtype('int32')

x = np.array([1.0, 2.0])
ic| x.dtype: dtype('float64')

x = np.array([1, 2], dtype=np.int64) 
ic| x.dtype: dtype('int64')

```



## 数组中的数学

基本数学函数在数组上以元素方式运行，既可以作为运算符重载，也可以作为numpy模块中的函数

### 计算加

```
元素相加：
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)


ic(x + y)
ic| x + y: array([[ 6.,  8.],
                  [10., 12.]])
ic(np.add(x, y))
ic| np.add(x, y): array([[ 6.,  8.],
                         [10., 12.]])

```



### 计算减

```
元素相减：
ic(x - y)
ic| x - y: array([[-4., -4.],
                  [-4., -4.]])
ic(np.subtract(x, y))
ic| np.subtract(x, y): array([[-4., -4.],
                              [-4., -4.]])
```

### 计算乘

```
元素相乘：
ic(x * y)
ic| x * y: array([[ 5., 12.],
                  [21., 32.]])
ic(np.multiply(x, y))
ic| np.multiply(x, y): array([[ 5., 12.],
                              [21., 32.]])xxxxxxxxxx7 1元素相乘：2ic(x * y)3ic| x * y: array([[ 5., 12.],4                  [21., 32.]])5ic(np.multiply(x, y))6ic| np.multiply(x, y): array([[ 5., 12.],7                              [21., 32.]])ic(np.dot(x, y))
```

### 计算除

```
元素相除：
ic(x / y)
ic| x / y: array([[0.2       , 0.33333333],
                  [0.42857143, 0.5       ]])
ic(np.divide(x, y))
ic| np.divide(x, y): array([[0.2       , 0.33333333],
                            [0.42857143, 0.5       ]])
```



### 计算平方根

```
元素平方根：
ic(np.sqrt(x))
ic| np.sqrt(x): array([[1.        , 1.41421356],
                       [1.73205081, 2.        ]])
```



### 计算内积

\*  是元素乘法，而不是矩阵乘法

dot函数来计算向量的内积，将向量乘以矩阵，并乘以矩阵

```
v = np.array([9,10])
w = np.array([11, 12])

ic(v.dot(w))
解析：9 * 11 + 10* 12
ic| v.dot(w): 219
ic(np.dot(v, w))
ic| np.dot(v, w): 219


x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
ic(np.dot(x, y))
解析：
[1,2] [5,6] [1,2] [3,4]
[3,4] [7,8] [5,6] [7,8]
[1 * 5 + 2 * 7 = 19, 1 * 6 + 2 * 8 = 22]
[3 * 5 + 4 * 7 = 43，3 * 6 + 4 * 8 = 50]
ic| np.dot(x, y): array([[19., 22.],
                         [43., 50.]])
```

### sum函数

```
x = np.array([[1,2],[3,4]])
ic(np.sum(x))       #计算所有元素的总和
ic| np.sum(x): 10  
ic(np.sum(x, axis=0)) #计算每列的总和
ic| np.sum(x, axis=0): array([4, 6])
ic(np.sum(x, axis=1)) #计算每行的总和
ic| np.sum(x, axis=1): array([3, 7])
```





## 数学函数

### 三角函数

| method                                                       | description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [sin](https://numpy.org/devdocs/reference/generated/numpy.sin.html#numpy.sin)(x, /[, out, where, casting, order, …]) | 正弦函数, element-wise.                                      |
| [cos](https://numpy.org/devdocs/reference/generated/numpy.cos.html#numpy.cos)(x, /[, out, where, casting, order, …]) | 余弦函数 element-wise.                                       |
| [tan](https://numpy.org/devdocs/reference/generated/numpy.tan.html#numpy.tan)(x, /[, out, where, casting, order, …]) | 正切函数, element-wise.                                      |
| [arcsin](https://numpy.org/devdocs/reference/generated/numpy.arcsin.html#numpy.arcsin)(x, /[, out, where, casting, order, …]) | 反正弦函数, element-wise.                                    |
| [arccos](https://numpy.org/devdocs/reference/generated/numpy.arccos.html#numpy.arccos)(x, /[, out, where, casting, order, …]) | 反余弦函数, element-wise.                                    |
| [arctan](https://numpy.org/devdocs/reference/generated/numpy.arctan.html#numpy.arctan)(x, /[, out, where, casting, order, …]) | 反正切函数, element-wise.                                    |
| [hypot](https://numpy.org/devdocs/reference/generated/numpy.hypot.html#numpy.hypot)(x1, x2, /[, out, where, casting, …]) | 传入直角三角形的“直角边”，返回其斜边。                       |
| [arctan2](https://numpy.org/devdocs/reference/generated/numpy.arctan2.html#numpy.arctan2)(x1, x2, /[, out, where, casting, …]) | x1 / x2的 Element-wise 反正切线正确选择象限。                |
| [degrees](https://numpy.org/devdocs/reference/generated/numpy.degrees.html#numpy.degrees)(x, /[, out, where, casting, order, …]) | 将角度从[弧度](https://numpy.org/devdocs/reference/generated/numpy.radians.html#numpy.radians)转换为度。 |
| radians(x, /[, out, where, casting, order, …])               | 将角度从度转换为弧度。                                       |
| [unwrap](https://numpy.org/devdocs/reference/generated/numpy.unwrap.html#numpy.unwrap)(p[, discont, axis]) | 通过将值之间的增量更改为2 * pi来展开。                       |
| [deg2rad](https://numpy.org/devdocs/reference/generated/numpy.deg2rad.html#numpy.deg2rad)(x, /[, out, where, casting, order, …]) | 将角度从度转换为弧度。                                       |
| [rad2deg](https://numpy.org/devdocs/reference/generated/numpy.rad2deg.html#numpy.rad2deg)(x, /[, out, where, casting, order, …]) | 将角度从弧度转换为度。                                       |

### 双曲函数

| method                                                       | description                |
| ------------------------------------------------------------ | -------------------------- |
| [sinh](https://numpy.org/devdocs/reference/generated/numpy.sinh.html#numpy.sinh)(x, /[, out, where, casting, order, …]) | 双曲正弦, element-wise.    |
| [cosh](https://numpy.org/devdocs/reference/generated/numpy.cosh.html#numpy.cosh)(x, /[, out, where, casting, order, …]) | 双曲余弦, element-wise.    |
| [tanh](https://numpy.org/devdocs/reference/generated/numpy.tanh.html#numpy.tanh)(x, /[, out, where, casting, order, …]) | 计算双曲正切 element-wise. |
| [arcsinh](https://numpy.org/devdocs/reference/generated/numpy.arcsinh.html#numpy.arcsinh)(x, /[, out, where, casting, order, …]) | 反双曲正弦 element-wise.   |
| [arccosh](https://numpy.org/devdocs/reference/generated/numpy.arccosh.html#numpy.arccosh)(x, /[, out, where, casting, order, …]) | 反双曲余弦, element-wise.  |
| [arctanh](https://numpy.org/devdocs/reference/generated/numpy.arctanh.html#numpy.arctanh)(x, /[, out, where, casting, order, …]) | 反双曲正切 element-wise.   |

### 四舍五入

| method                                                       | description                          |
| ------------------------------------------------------------ | ------------------------------------ |
| [around](https://numpy.org/devdocs/reference/generated/numpy.around.html#numpy.around)(a[, decimals, out]) | 平均舍入到给定的小数位数。           |
| [round_](https://numpy.org/devdocs/reference/generated/numpy.round_.html#numpy.round_)(a[, decimals, out]) | 将数组舍入到给定的小数位数。         |
| [rint](https://numpy.org/devdocs/reference/generated/numpy.rint.html#numpy.rint)(x, /[, out, where, casting, order, …]) | 将数组的元素四舍五入到最接近的整数。 |
| [fix](https://numpy.org/devdocs/reference/generated/numpy.fix.html#numpy.fix)(x[, out]) | 四舍五入为零。                       |
| [floor](https://numpy.org/devdocs/reference/generated/numpy.floor.html#numpy.floor)(x, /[, out, where, casting, order, …]) | 返回输入的底限, element-wise.        |
| [ceil](https://numpy.org/devdocs/reference/generated/numpy.ceil.html#numpy.ceil)(x, /[, out, where, casting, order, …]) | 返回输入的上限, element-wise.        |
| [trunc](https://numpy.org/devdocs/reference/generated/numpy.trunc.html#numpy.trunc)(x, /[, out, where, casting, order, …]) | 返回输入的截断值, element-wise.      |

### 加法函数, 乘法函数, 减法函数

| method                                                       | description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [prod](https://numpy.org/devdocs/reference/generated/numpy.prod.html#numpy.prod)(a[, axis, dtype, out, keepdims, …]) | 返回给定轴上数组元素的乘积。                                 |
| [sum](https://numpy.org/devdocs/reference/generated/numpy.sum.html#numpy.sum)(a[, axis, dtype, out, keepdims, …]) | 给定轴上的数组元素的总和。                                   |
| [nanprod](https://numpy.org/devdocs/reference/generated/numpy.nanprod.html#numpy.nanprod)(a[, axis, dtype, out, keepdims]) | 返回数组元素在给定轴上的乘积，将非数字（NaNs）视为一个。     |
| [nansum](https://numpy.org/devdocs/reference/generated/numpy.nansum.html#numpy.nansum)(a[, axis, dtype, out, keepdims]) | 返回给定轴上的数组元素的总和，将非数字（NaNs）视为零。       |
| [cumprod](https://numpy.org/devdocs/reference/generated/numpy.cumprod.html#numpy.cumprod)(a[, axis, dtype, out]) | 返回沿给定轴的元素的累加乘积。                               |
| [cumsum](https://numpy.org/devdocs/reference/generated/numpy.cumsum.html#numpy.cumsum)(a[, axis, dtype, out]) | 返回沿给定轴的元素的累加和。                                 |
| [nancumprod](https://numpy.org/devdocs/reference/generated/numpy.nancumprod.html#numpy.nancumprod)(a[, axis, dtype, out]) | 返回数组元素在给定轴上的累积乘积，将非数字（NaNs）视为一个。 |
| [nancumsum](https://numpy.org/devdocs/reference/generated/numpy.nancumsum.html#numpy.nancumsum)(a[, axis, dtype, out]) | 返回在给定轴上将非数字（NaNs）视为零的数组元素的累积总和。   |
| [diff](https://numpy.org/devdocs/reference/generated/numpy.diff.html#numpy.diff)(a[, n, axis, prepend, append]) | 计算沿给定轴的第n个离散差。                                  |
| [ediff1d](https://numpy.org/devdocs/reference/generated/numpy.ediff1d.html#numpy.ediff1d)(ary[, to_end, to_begin]) | 数组的连续元素之间的差值。                                   |
| [gradient](https://numpy.org/devdocs/reference/generated/numpy.gradient.html#numpy.gradient)(f, *varargs, **kwargs) | 返回N维数组的梯度。                                          |
| [cross](https://numpy.org/devdocs/reference/generated/numpy.cross.html#numpy.cross)(a, b[, axisa, axisb, axisc, axis]) | 返回两个（数组）向量的叉积。                                 |
| [trapz](https://numpy.org/devdocs/reference/generated/numpy.trapz.html#numpy.trapz)(y[, x, dx, axis]) | 使用复合梯形规则沿给定轴积分。                               |

### 指数和对数

| method                                                       | description                                 |
| ------------------------------------------------------------ | ------------------------------------------- |
| [exp](https://numpy.org/devdocs/reference/generated/numpy.exp.html#numpy.exp)(x, /[, out, where, casting, order, …]) | 计算输入数组中所有元素的指数。              |
| [expm1](https://numpy.org/devdocs/reference/generated/numpy.expm1.html#numpy.expm1)(x, /[, out, where, casting, order, …]) | 为数组中的所有元素计算exp（x）-1。          |
| [exp2](https://numpy.org/devdocs/reference/generated/numpy.exp2.html#numpy.exp2)(x, /[, out, where, casting, order, …]) | 为输入数组中的所有p计算2 ** p。             |
| [log](https://numpy.org/devdocs/reference/generated/numpy.log.html#numpy.log)(x, /[, out, where, casting, order, …]) | 自然对数, element-wise.                     |
| [log10](https://numpy.org/devdocs/reference/generated/numpy.log10.html#numpy.log10)(x, /[, out, where, casting, order, …]) | 返回输入数组的以10为底的对数, element-wise. |
| [log2](https://numpy.org/devdocs/reference/generated/numpy.log2.html#numpy.log2)(x, /[, out, where, casting, order, …]) | x的以2为底的对数。                          |
| [log1p](https://numpy.org/devdocs/reference/generated/numpy.log1p.html#numpy.log1p)(x, /[, out, where, casting, order, …]) | 返回元素加一个输入数组的自然对数。          |
| [logaddexp](https://numpy.org/devdocs/reference/generated/numpy.logaddexp.html#numpy.logaddexp)(x1, x2, /[, out, where, casting, …]) | 输入取幂之和的对数。                        |
| [logaddexp2](https://numpy.org/devdocs/reference/generated/numpy.logaddexp2.html#numpy.logaddexp2)(x1, x2, /[, out, where, casting, …]) | 以2为底的输入的幂和的对数。                 |

### 其他特殊函数

| method                                                       | description                       |
| ------------------------------------------------------------ | --------------------------------- |
| [i0](https://numpy.org/devdocs/reference/generated/numpy.i0.html#numpy.i0)(x) | 第一种修改的Bessel函数，阶数为0。 |
| [sinc](https://numpy.org/devdocs/reference/generated/numpy.sinc.html#numpy.sinc)(x) | 返回sinc函数。                    |

### 浮点例程

| method                                                       | description                                              |
| ------------------------------------------------------------ | -------------------------------------------------------- |
| [signbit](https://numpy.org/devdocs/reference/generated/numpy.signbit.html#numpy.signbit)(x, /[, out, where, casting, order, …]) | 在设置了符号位（小于零）的情况下返回 element-wise True。 |
| [copysign](https://numpy.org/devdocs/reference/generated/numpy.copysign.html#numpy.copysign)(x1, x2, /[, out, where, casting, …]) | 将x1的符号更改为x2的符号, element-wise.                  |
| [frexp](https://numpy.org/devdocs/reference/generated/numpy.frexp.html#numpy.frexp)(x[, out1, out2], / [[, out, where, …]) | 将x的元素分解为尾数和二进制指数。                        |
| [ldexp](https://numpy.org/devdocs/reference/generated/numpy.ldexp.html#numpy.ldexp)(x1, x2, /[, out, where, casting, …]) | 返回x1 * 2 ** x2, element-wise.                          |
| [nextafter](https://numpy.org/devdocs/reference/generated/numpy.nextafter.html#numpy.nextafter)(x1, x2, /[, out, where, casting, …]) | 向x2返回x1之后的下一个浮点值, element-wise.              |
| [spacing](https://numpy.org/devdocs/reference/generated/numpy.spacing.html#numpy.spacing)(x, /[, out, where, casting, order, …]) | 返回x与最近的相邻数字之间的距离。                        |

### 理性例程

| method                                                       | description            |
| ------------------------------------------------------------ | ---------------------- |
| [lcm](https://numpy.org/devdocs/reference/generated/numpy.lcm.html#numpy.lcm)(x1, x2, /[, out, where, casting, order, …]) | 返回1和x2的最小公倍数  |
| [gcd](https://numpy.org/devdocs/reference/generated/numpy.gcd.html#numpy.gcd)(x1, x2, /[, out, where, casting, order, …]) | 返回x1和x2的最大公约数 |

### 算术运算

| method                                                       | description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [add](https://numpy.org/devdocs/reference/generated/numpy.add.html#numpy.add)(x1, x2, /[, out, where, casting, order, …]) | 按元素添加参数。                                             |
| [reciprocal](https://numpy.org/devdocs/reference/generated/numpy.reciprocal.html#numpy.reciprocal)(x, /[, out, where, casting, …]) | 以元素为单位返回参数的倒数。                                 |
| [positive](https://numpy.org/devdocs/reference/generated/numpy.positive.html#numpy.positive)(x, /[, out, where, casting, order, …]) | 数值正, element-wise.                                        |
| [negative](https://numpy.org/devdocs/reference/generated/numpy.negative.html#numpy.negative)(x, /[, out, where, casting, order, …]) | 数值负数, element-wise.                                      |
| [multiply](https://numpy.org/devdocs/reference/generated/numpy.multiply.html#numpy.multiply)(x1, x2, /[, out, where, casting, …]) | 逐个乘以参数。                                               |
| [divide](https://numpy.org/devdocs/reference/generated/numpy.divide.html#numpy.divide)(x1, x2, /[, out, where, casting, …]) | 返回输入的真实除法, element-wise.                            |
| [power](https://numpy.org/devdocs/reference/generated/numpy.power.html#numpy.power)(x1, x2, /[, out, where, casting, …]) | 第一阵列元素从第二阵列提升为幂, element-wise.                |
| [subtract](https://numpy.org/devdocs/reference/generated/numpy.subtract.html#numpy.subtract)(x1, x2, /[, out, where, casting, …]) | 逐个元素地减去参数。                                         |
| [true_divide](https://numpy.org/devdocs/reference/generated/numpy.true_divide.html#numpy.true_divide)(x1, x2, /[, out, where, …]) | 返回输入的真实除法, element-wise.                            |
| [floor_divide](https://numpy.org/devdocs/reference/generated/numpy.floor_divide.html#numpy.floor_divide)(x1, x2, /[, out, where, …]) | 返回小于或等于输入的除法的最大整数。                         |
| [float_power](https://numpy.org/devdocs/reference/generated/numpy.float_power.html#numpy.float_power)(x1, x2, /[, out, where, …]) | 第一阵列元素从第二阵列提升为幂, element-wise.                |
| [fmod](https://numpy.org/devdocs/reference/generated/numpy.fmod.html#numpy.fmod)(x1, x2, /[, out, where, casting, …]) | 返回元素的除法 [remainder](https://numpy.org/devdocs/reference/generated/numpy.remainder.html#numpy.remainder)。 |
| [mod](https://numpy.org/devdocs/reference/generated/numpy.mod.html#numpy.mod)(x1, x2, /[, out, where, casting, order, …]) | 返回元素的除法余数。                                         |
| [modf](https://numpy.org/devdocs/reference/generated/numpy.modf.html#numpy.modf)(x[, out1, out2], / [[, out, where, …]) | 返回数组的分数和整数部分, element-wise.                      |
| remainder(x1, x2, /[, out, where, casting, …])               | 返回元素的除法余数。                                         |
| [divmod](https://numpy.org/devdocs/reference/generated/numpy.divmod.html#numpy.divmod)(x1, x2[, out1, out2], / [[, out, …]) | 同时返回按元素商和余数。                                     |

### 处理复数

| method                                                       | description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [angle](https://numpy.org/devdocs/reference/generated/numpy.angle.html#numpy.angle)(z[, deg]) | 返回复杂参数的角度。                                         |
| [real](https://numpy.org/devdocs/reference/generated/numpy.real.html#numpy.real)(val) | 返回复杂参数的实部。                                         |
| [imag](https://numpy.org/devdocs/reference/generated/numpy.imag.html#numpy.imag)(val) | 返回复杂参数的虚部。                                         |
| [conj](https://numpy.org/devdocs/reference/generated/numpy.conj.html#numpy.conj)(x, /[, out, where, casting, order, …]) | 返回 complex [conjugate](https://numpy.org/devdocs/reference/generated/numpy.conjugate.html#numpy.conjugate), element-wise. |
| [conjugate](https://numpy.org/devdocs/reference/generated/numpy.conjugate.html#numpy.conjugate)(x, /[, out, where, casting, …]) | 返回复共轭, element-wise.                                    |

### 杂项

| method                                                       | description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [convolve](https://numpy.org/devdocs/reference/generated/numpy.convolve.html#numpy.convolve)(a, v[, mode]) | 返回两个一维序列的离散线性卷积。                             |
| [clip](https://numpy.org/devdocs/reference/generated/numpy.clip.html#numpy.clip)(a, a_min, a_max[, out]) | 裁剪（限制）数组中的值。                                     |
| [sqrt](https://numpy.org/devdocs/reference/generated/numpy.sqrt.html#numpy.sqrt)(x, /[, out, where, casting, order, …]) | 返回数组的非负 [平方](https://numpy.org/devdocs/reference/generated/numpy.square.html#numpy.square)根, element-wise. |
| [cbrt](https://numpy.org/devdocs/reference/generated/numpy.cbrt.html#numpy.cbrt)(x, /[, out, where, casting, order, …]) | 返回数组的立方根, element-wise.                              |
| [square](https://numpy.org/devdocs/reference/generated/numpy.square.html#numpy.square)(x, /[, out, where, casting, order, …]) | 返回输入的元素方平方。                                       |
| [absolute](https://numpy.org/devdocs/reference/generated/numpy.absolute.html#numpy.absolute)(x, /[, out, where, casting, order, …]) | 计算绝对值 element-wise.                                     |
| [fabs](https://numpy.org/devdocs/reference/generated/numpy.fabs.html#numpy.fabs)(x, /[, out, where, casting, order, …]) | 计算绝对值 element-wise.                                     |
| [sign](https://numpy.org/devdocs/reference/generated/numpy.sign.html#numpy.sign)(x, /[, out, where, casting, order, …]) | 返回数字符号的逐元素指示。                                   |
| [heaviside](https://numpy.org/devdocs/reference/generated/numpy.heaviside.html#numpy.heaviside)(x1, x2, /[, out, where, casting, …]) | 计算Heaviside阶跃函数。                                      |
| [maximum](https://numpy.org/devdocs/reference/generated/numpy.maximum.html#numpy.maximum)(x1, x2, /[, out, where, casting, …]) | 数组元素的逐元素最大值。                                     |
| [minimum](https://numpy.org/devdocs/reference/generated/numpy.minimum.html#numpy.minimum)(x1, x2, /[, out, where, casting, …]) | 数组元素的按元素最小值。                                     |
| [fmax](https://numpy.org/devdocs/reference/generated/numpy.fmax.html#numpy.fmax)(x1, x2, /[, out, where, casting, …]) | 数组元素的逐元素最大值。                                     |
| [fmin](https://numpy.org/devdocs/reference/generated/numpy.fmin.html#numpy.fmin)(x1, x2, /[, out, where, casting, …]) | 数组元素的按元素最小值。                                     |
| [nan_to_num](https://numpy.org/devdocs/reference/generated/numpy.nan_to_num.html#numpy.nan_to_num)(x[, copy, nan, posinf, neginf]) | 用较大的有限数字（默认行为）或使用用户定义的nan，posinf和/或neginf关键字定义的数字将NaN替换为零和无穷大。 |
| [real_if_close](https://numpy.org/devdocs/reference/generated/numpy.real_if_close.html#numpy.real_if_close)(a[, tol]) | 如果复杂输入接近实数，则返回复杂数组。                       |
| [interp](https://numpy.org/devdocs/reference/generated/numpy.interp.html#numpy.interp)(x, xp, fp[, left, right, period]) | 一维线性插值。                                               |

## 例子

### 数组叠加

```
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
c = np.concatenate([a, b], axis=0)
ic| a: array([[0, 1, 2, 3, 4],
              [5, 6, 7, 8, 9]])
ic| b: array([[1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1]])
ic| c: array([[0, 1, 2, 3, 4],
              [5, 6, 7, 8, 9],
              [1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1]])
```