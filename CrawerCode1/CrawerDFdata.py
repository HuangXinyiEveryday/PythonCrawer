# coding=utf-8
# 导入需要使用到的模块
import re
import csv
import codecs
import urllib
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options



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

#爬虫具体数据
def getAjaxdata(code):
    htmlurl="http://data.eastmoney.com/zjlx/"+code+".html"#具体页面url
    #webtest=webdriver.PhantomJS()
    chrome_options = Options()
    chrome_options.add_argument('--headless')#selenium+headless爬虫技术，爬虫动态ajax数据
    chrome_options.add_argument('--disable-gpu')
    webtest = webdriver.Chrome(chrome_options=chrome_options)#设置谷歌浏览器chrome_options
    webtest.get(htmlurl)
    stocktext=webtest.find_element_by_id('dt_1').text#根据表的id爬虫数据
    stockname=webtest.find_element_by_class_name('tit').text#爬虫股票名称
    stockarray=stocktext.split()#以空格分隔
    columnname1=[]#行1，表示主力、超大单等
    columnname2=[]#行2，真实的数据净占比、净额
    columndata=[]#每一行具体数据
    #print(columnname1)
    #如果有历史资金流向数据才记录
    if (len(stockarray)) > 20:
        #设置表头格式
        for i in range(0, 3):
            columnname2.append(stockarray[i])
        columnname1.append(stockname)
        for i in range(3, 8):
            columnname1.append(stockarray[i])
        for i in range(8, 18):
            columnname2.append(stockarray[i])
        #保存到csv文件中
        text=os.getcwd()+'/Data/'+code+".csv"
        j=18
        with open(text,"w",encoding='utf-8-sig') as csvfile:
            writer=csv.writer(csvfile)
            writer.writerow(columnname1)
            writer.writerow(columnname2)
            #具体每一行数据处理并存储，直至结束
            while j+13 <= (len(stockarray)):
                for i in range(j, j+13):
                    columndata.append(stockarray[i])
                j = j+13
                writer.writerow(columndata)
                columndata=[]
        csvfile.close()
        print(stockname, '处理完成')
#getAjaxdata("600085")


Url = 'http://quote.eastmoney.com/stocklist.html'  # 东方财富网股票数据连接地址
filepath=os.getcwd()+'/Data/'#定义数据文件保存路径，获取当前目录继续加路径
# 实施抓取
code = getStackCode(getHtml(Url))
# 获取所有股票代码（以6开头的，应该是沪市数据）集合
CodeList = []
for item in code:
    if item[0]=='3':
        CodeList.append(item)
        print(item,"is processing")
        #每一个代码爬取具体数据
        getAjaxdata(item)

