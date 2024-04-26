from lxml import etree
import requests
import os
#新建一个文件夹
dirName = 'girls'
if not os.path.exists(dirName):#如果文件夹不存在，则新建，否则不新建
    os.mkdir(dirName)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

url = 'https://pic.netbian.com/4kmeinv/index.html'
response = requests.get(url=url,headers=headers)
response.encoding = 'gbk'
page_text = response.text

#数据解析：图片地址+图片名称
tree = etree.HTML(page_text)#HTML()专门用来解析网络请求到的页面源码数据
#该列表中存储的是每一个li标签
li_list = tree.xpath('//div[@class="slist"]/ul/li')
for li in li_list:
    #局部解析：将li标签中指定的内容解析出来
    img_title = li.xpath('./a/b/text()')[0]+'.jpg'# 左侧./表示xpath的调用者对应的标签
    img_src = 'https://pic.netbian.com'+li.xpath('./a/img/@src')[0]

    #对图片发起请求，存储图片数据
    img_data = requests.get(url=img_src,headers=headers).content
    # girls/123.jpg
    img_path = dirName + '/' + img_title
    with open(img_path,'wb') as fp:
        fp.write(img_data)
    print(img_title,'下载保存成功！')