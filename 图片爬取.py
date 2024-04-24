import requests
url = 'https://img2.baidu.com/it/u=2214388039,2430684729&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=889'

response = requests.get(url = url)
img_data = response.content
with open('1.jpg','wb') as fp:
    fp.write(img_data)