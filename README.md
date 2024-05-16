# 自动登录 cpolar 网站并读取通道 IP

## 1. 功能概述

这个代码的作用是使用 Python 脚本自动登录 cpolar 网站并读取对应通道 IP，并将其复制到剪切板。您可以使用python脚本进行操作，但是这样可能还是不够简洁。您可以按照README中的步骤将其打包成一个可执行文件，这样的功能让操作变得十分简便。

## 2. 打包预处理与打包方法

如果你想将 `cpolar_ssh.py` 打包成可执行文件，你可以按照以下步骤进行：

### 安装 PyInstaller

首先，你需要确保在你的环境中已经安装 PyInstaller。你可以使用 pip 命令来安装 PyInstaller：

```bash
pip install pyinstaller
```
    
### 使用 pyi-makespec 预处理

首先，你需要使用 `pyi-makespec` 工具来为打包做好准备。这个工具可以根据你的 Python 脚本生成一个用于打包的 `.spec` 文件。在生成 `.spec` 文件时，你还可以指定一些选项，比如打包后的可执行文件的图标等。spec文件的data选项保证了你能够正确读取到user.cfg文件中的配置信息。

```bash
pyi-makespec -F -i icon.ico cpolar_ssh.py
```

在这个命令中，-F 选项告诉 PyInstaller 生成单个独立的可执行文件，而 -i 选项指定了图标文件的路径。您可以按照自己的喜好进行替换。

### 使用 PyInstaller 进行打包
一旦你有了 .spec 文件，就可以使用 PyInstaller 进行实际的打包工作了。PyInstaller 将会根据 .spec 文件的配置来将你的 Python 脚本及其依赖项打包成一个独立的可执行文件。

```bash
pyinstaller cpolar_ssh.spec
```
这将在当前目录下生成一个名为 dist 的文件夹，在其中你将会找到生成的可执行文件。
同时，你可以通过在user.cfg中修改mode选项来选择所需的ip地址类型。
【SSH】：获取port 22 端口的转发地址
【HTTPS】：获取port 80 端口的转发地址


## 3. 注意事项
在本项目中，note 文件夹下的 HTML 文件是作者在开发过程中搜索资料的记录。如果其中存在侵权内容，读者可以自行删除并联系我进行删除。