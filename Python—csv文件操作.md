# Python—csv文件存储

``` python
import csv
 #保存到csv文件中
     text=os.getcwd()+'/Data/'+code+".csv"
     j=18
     with open(text,"w",encoding='utf-8-sig') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(columnname1)
        writer.writerow(columnname2)
        #具体每一行数据处理并存储，直至结束
        while （j+13） <= (len(stockarray)):
           for i in range(j, j+13):
               columndata.append(stockarray[i])#数组追加元素
               j = j+13
               writer.writerow(columndata)
               columndata=[]
        csvfile.close()
```

with open打开csv文件，如果没有则新建该文件，打开文件最后一定要.close()把文件关闭
encoding编码方式则可以解决数据有中文乱码问题
writerow可以写一行数据
::writerows::则可以一次写多行数据
数组加入数据可以使用::.append::方式
python循环的两种格式
	* while  表达式:
				* for 变量 in  range(x,y)-变量取值范围,x≤变量＜y

