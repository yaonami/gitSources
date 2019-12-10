import json
import requests


# 图灵机器人
def get_response(msg):
    KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
    apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'
    dat = {
        "perception": {
            "inputText": {
                "text": msg
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "信息路"
                }
            }
        },
        "userInfo": {
            "apiKey": KEY,
            "userId": "fool"
        }
    }
    dat = json.dumps(dat)
    r = requests.post(apiUrl, data=dat).json()
    # print(r["results"][0]["values"]["text"])
    res = r["results"][0]["values"]["text"]
    return res


# 青云客机器人
def QINGYUNKERobot(mes):
    engine = "http://api.qingyunke.com/api.php?key=free&appid=0&msg="
    try:
        url = engine + mes
        r = requests.get(url).json()
        res = r["content"]
        return res
    except:
        raise
        # return "出错了"