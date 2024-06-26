import requests

#1.指定url
main_url = 'https://www.eastmoney.com/'

#2.发起请求:
#get函数可以根据指定的url发起网络请求
#get函数会返回一个响应对象:
response = requests.get(url=main_url)
response.encoding = encodings = 'utf-8'

#3.获取响应数据
page_text = response.text #text是可以返回字符串形式的响应数据/爬取到的数据

#4.持久化存储
with open('dongfang.html','w', encoding='utf-8') as fp:
    fp.write(page_text)