#### 肯德基（POST请求、动态加载数据、UA检测）

#- http://www.kfc.com.cn/kfccda/storelist/index.aspx

#  - 将餐厅的位置信息进行数据爬取

import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

header = {
    'User -Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)',
    'Referer' : 'http://www.kfc.com.cn/kfccda/storelist/index.aspx',
}

response = requests.post(url=url,headers=header)

page = response.json()
print(page)