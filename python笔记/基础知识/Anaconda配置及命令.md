# Anaconda



## 配置代理

打开文件

C:\Users\alan\.condarc

添加

~~~
show_channel_urls: true
allow_other_channels: true

proxy_servers:
  http: http://127.0.0.1:7890
  https: http://127.0.0.1:7890

ssl_verify: true
~~~



## 添加源

~~~
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/ conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge  conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
~~~



## 基本命令

查看版本信息 conda --version
创建一个虚拟环境 conda create -n rqsdk python=3.8.2
激活新的虚拟环境 conda activate rqsdk
退出当前环境 conda deactivate
删除虚拟环境conda remove --name rqsdk --all
如果拷贝过来未能自动识别，可手动安装 conda install --offline local_path

**conda list**     									查看安装了哪些包

**conda env list** 、**conda info -e** 	 查看存在哪些虚拟环境

**conda update conda**      				检查更新conda

