import requests
game_tile = input('enter a game name:')
params = {
    'q' : game_tile
}
url = 'https://game.51.com/search/action/game/'

response = requests.get(url=url,params=params)

page_text = response.text

filename = game_tile+'.html'
with open(filename,'w',encoding='utf-8')as fp:
    fp.write(page_text)