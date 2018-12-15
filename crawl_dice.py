import requests
from pymongo import MongoClient
# 连接数据库
client = MongoClient()
url = 'https://a.dragonex.im/game/dice/bet/latest/?coin_id=104&page_size=9'
# 获取数据库
db = client.dragonex
# 获取集合
collection = db.dice



def crwal(url):
    global  num




    try:
        req = requests.get(url)
        content = req.json()
    except:
        print("failed to get content")
    collection.insert_many(content['data'])








crwal(url)


# for key in data:
#     count[key] = count.get(key,0)+1
#
# print(sorted(count.items(),key=lambda item:item[0]))
# print(num)

