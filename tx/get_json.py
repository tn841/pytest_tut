#-*- coding:utf-8 -*-
import json

from pip._vendor import requests

def tx_get_superheroes():
    url = 'https://mdn.github.io/learning-area/javascript/oojs/json/superheroes.json'
    res = requests.get(url)
    print('')
    print("res.content : {}".format(type(res.content)))
    print("json.loads : {}".format(json.loads(res.content)))

    return res
