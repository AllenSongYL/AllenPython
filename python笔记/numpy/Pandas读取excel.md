# Pandas

## 入门介绍

生成对象

```
s = pd.Series([1, 3, 5, np.nan, 6, 8])
```



## 读取excel

### Excel文件

`read_excel()`方法使用Python的`xlrd`模块来读取Excel 2003（`.xls`)版的文件，而Excel 2007+ （`.xlsx`)版本的是用`xlrd`或者`openpyxl`模块来读取的。`to_excel()` 方法则是用来把`DataFrame`数据存储为Excel格式。一般来说，它的语法同使用csv数据是类似的，更多高级的用法可以参考[cookbook (opens new window)](https://www.pypandas.cn/docs/user_guide/cookbook.html#cookbook-excel)。

### 语法

第一个参数，指定文件路径，默认取第一张表，也可以通过指定sheet_name表名或使用数字索引, 

header：

​    表示用第几行作为表头，默认为0，即第一行。

​    hearder=1：选择第二行为表头，第一行数据就不要了。其他以此类推。

​    hearder=[1,2,3]：选择第2,3,4行的数据作为表头，第二行之上的数据不用

```python
pd.read_excel('path_to_file.xls', sheet_name='Sheet1'，header=0)
```

### ExcelFile类

为了更方便地读取同一个文件的多张表格，`ExcelFile`类可用来打包文件并传递给`read_excel`。因为仅需读取一次内存，所以这种方式读取一个文件的多张表格会有性能上的优势。


```python
xlsx = pd.ExcelFile('path_to_file.xls')
df = pd.read_excel(xlsx, 'Sheet1')
```

`ExcelFile`类也能用来作为上下文管理器。

```python
with pd.ExcelFile('path_to_file.xls') as xls:
	ic(xls.sheet_names)                 #sheet_names属性能将文件中的所有表格名字生成一组列表。
    df1 = pd.read_excel(xls, 'Sheet1')
    df2 = pd.read_excel(xls, 'Sheet2')
    df3 = pd.read_excel(xls,sheet_name=None)  #使用None获取所有表格
    df4 = pd.read_excel(xls, 1)               #使用表格索引,默认0第一张表
```

主要的用法就是用来解析多张表格的不同参数