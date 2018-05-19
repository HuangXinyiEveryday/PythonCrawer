# Python os操作文件、文件路径
Python获取文件上一级：取文件所在目录的上一级目录
```
#os.path.pardir是父目录,os.path.abspath是绝对路径
os.path.abspath(os.path.join(os.path.dirname('settings.py',os.path.pardir)) 
os.getcwd()#获取当前py文件所在路径
os.path.join（filepath,filename）#os.path.join()在路径处理上很有用，连接文件路径及文件名。应用在爬虫中进行文件下载到制定目录中
urlretrieve()#方法直接将远程数据下载到本地。
```
Python爬虫遇到的问题—目标服务器积极拒绝
安装ssl模块并导入引用
```
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
```

