import itchat
import requests


def sendMsg():
    itchat.send('hello,nice to meet you!', '@cd6ec55721dbed471f992ad8de4b5877c06bb7243814b62fff0bb26a656a5d10')


def sendMsgByNickName(nickName,msg):
    info = itchat.search_friends(nickName)
    itchat.send(msg, info['UserName'])


def getWeather(city):
    url = 'https://free-api.heweather.com/v5/forecast?city='+city+'&key=7d0daf2a85f64736a42261161cd3060b'
    html = requests.get(url)
    html.encoding = 'utf8'
    data = html.json()
    print(data)
    # data = data.json()
    print(type(data))
    weather = data['HeWeather5'][0]['daily_forecast']
    print(weather)
    daily_weather = weather[0]
    print(daily_weather)


