# Flask



## 创建虚拟环境

创建一个项目文件夹，然后创建一个虚拟环境。创建完成后项目文件夹中会有一个 `ven` 文件夹

mkdir  project_test

cd  project_test

python  -m venv ven

激活虚拟环境

ven\Scripts\activate

激活后显示：

(ven) PS D:\1.宇信智臻\flaskProject\project_test\ven\Scripts>

## 安装Flask

pip install flask

创建一个hello.py文件

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
```

配置环境变量

cmd:               set FLASK_APP=hello

powershell:    FLASK_APP = "hello"

bash:             export FLASK_APP=hello

## 运行Flask：

flask run

