import requests
url = 'http://www.cpta.com.cn/'

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

response = requests.get(url=url,headers=header)

page_text = response.text

with open('kaoshi.html','w',encoding='utf-8')as fp:
    fp.write(page_text)