import requests
url = 'https://www.qmjianli.com/cvs/24423THOLRKLQGR'

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

response = requests.get(url=url,headers=header)

page_text = response.text

with open('wodejianli.html','w',encoding='utf-8')as fp:
    fp.write(page_text)