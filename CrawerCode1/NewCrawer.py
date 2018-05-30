# 导入需要使用到的模块
import urllib.request
import re
import os
import ssl
import socket

# 爬虫抓取网页函数
def getHtml(url):
    html = urllib.request.urlopen(url).read()
    html = html.decode('gbk')
    return html


# 抓取网页股票代码函数
def getStackCode(html):
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
    pat = re.compile(s)
    code = pat.findall(html)
    #print(code);
    return code


#########################开始干活############################
Url = 'http://quote.eastmoney.com/stocklist.html'  # 东方财富网股票数据连接地址
filepath=os.getcwd()+'/Data1/cyb'# 定义数据文件保存路径，获取当前目录继续加路径
# 实施抓取
code = getStackCode(getHtml(Url))
# 获取所有股票代码（以6开头的，应该是沪市数据）集合
CodeList = []
for item in code:
    if item[0] == '3':
        CodeList.append(item)
        print(item)
# 抓取数据并保存到本地csv文件
ssl._create_default_https_context = ssl._create_unverified_context#防止网站检测爬虫拒绝请求
socket.setdefaulttimeout(120)#设置超时时间60s
for code in CodeList:
    print('正在获取股票%s数据' % code)
    url = 'http://quotes.money.163.com/service/chddata.html?code=1' + code + \
         '&end=20180518&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
    filename = os.path.join(filepath, code + '.csv')#将获取的当前目录与文件名链接
    #解决网页响应缓慢，爬虫超时报错结束
    try:
        urllib.request.urlretrieve(url, filename)
    except socket.timeout:
        count=1
        while count <= 5:
            try:
                urllib.request.urlretrieve(url, filename)
                break
            except socket.timeout:
                err_info = 'Reloading for %d time' % count if count == 1 else 'Reloading for %d times' % count
                print(err_info)
                count += 1
        if count>5:
            print("downloading failed!")

