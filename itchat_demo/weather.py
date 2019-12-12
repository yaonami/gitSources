import requests


# 和风天气V5版本API
# def getWeather(city):
#     url = 'https://free-api.heweather.com/v5/forecast?city='+city+'&key=7d0daf2a85f64736a42261161cd3060b'
#     html = requests.get(url)
#     html.encoding = 'utf8'
#     data = html.json()
#     print(data)
#     # data = data.json()
#     print(type(data))
#     weather = data['HeWeather5'][0]['daily_forecast']
#     print(weather)
#     daily_weather = weather[0]
#     print(daily_weather)


# 获取未来7天的天气预报
def getWeatherForecast(city):
    url = 'https://free-api.heweather.net/s6/weather/forecast?location='+city+'&key=cc33b9a52d6e48de852477798980b76e'
    html = requests.get(url)
    html.encoding = 'utf8'
    data = html.json()
    status = data['HeWeather6'][0]['status']
    recent7_weather = []
    if status=='ok':
        daily_forecast = data['HeWeather6'][0]['daily_forecast']
        for tmp in daily_forecast:
            day_weather = {'日期':tmp['date'], '最高温度':tmp['tmp_max'], '最低温度':tmp['tmp_min'],
                         '白天天气':tmp['cond_txt_d'], '夜间天气':tmp['cond_txt_n'], '风向':tmp['wind_dir'],
                         '风力':tmp['wind_sc'], '能见度':tmp['vis'], '地区':city}
            recent7_weather.append(day_weather)
    return recent7_weather


# 获取当前时间的天气
def getWeatherNow(city):
    url = 'https://free-api.heweather.net/s6/weather/now?location='+city+'&key=cc33b9a52d6e48de852477798980b76e'
    html = requests.get(url)
    html.encoding = 'utf8'
    data = html.json()
    status = data['HeWeather6'][0]['status']
    weather = []
    if status=='ok':
        now = data['HeWeather6'][0]['now']
        update = data['HeWeather6'][0]['update']['loc']
        now_weather = {'地区':city, '更新时间':update, '当前温度':now['tmp'], '体感温度':now['fl'],
                       '当前天气':now['cond_txt'], '当前风向':now['wind_dir'], '当前风力':now['wind_sc'],
                       '能见度':now['vis']}
        weather.append(now_weather)
    return weather


# 获取未来24小时的天气
def getWeatherHourly(city):
    url = 'https://free-api.heweather.net/s6/weather/hourly?location='+city+'&key=cc33b9a52d6e48de852477798980b76e'
    html = requests.get(url)
    html.encoding = 'utf8'
    data = html.json()
    status = data['HeWeather6'][0]['status']
    recent24_weather = []
    if status=='ok':
        hourlies = data['HeWeather6'][0]['hourly']
        for tmp in hourlies:
            hourly_weather = {'时间':tmp['time'], '温度':tmp['tmp'], '天气':tmp['cond_txt'], '风向':tmp['wind_dir'],
                              '风力':tmp['wind_sc'], '地区':city}
            recent24_weather.append(hourly_weather)
    return recent24_weather


# 获取生活指数
def getWeatherLifestyle(city):
    url = 'https://free-api.heweather.net/s6/weather/lifestyle?location='+city+'&key=cc33b9a52d6e48de852477798980b76e'
    html = requests.get(url)
    html.encoding = 'utf8'
    data = html.json()
    status = data['HeWeather6'][0]['status']
    all_lifestyle = []
    if status=='ok':
        lifestyle = data['HeWeather6'][0]['lifestyle']
        typeDict = {'comf':'舒适度指数', 'cw':'洗车指数', 'drsg':'穿衣指数', 'flu':'感冒指数', 'sport':'运动指数',
                    'trav':'旅游指数', 'uv':'紫外线指数', 'air':'空气指数', 'ac':'空调开启指数', 'ag':'过敏指数',
                    'gl':'太阳镜指数', 'mu':'化妆指数', 'airc':'晾晒指数', 'ptfc':'交通指数', 'fsh':'钓鱼指数',
                    'spi':'防晒指数'}
        for tmp in lifestyle:
            lifestyle_con = {typeDict[tmp['type']]:tmp['txt']}
            all_lifestyle.append(lifestyle_con)
    return all_lifestyle


# 模糊获取中国城市/景区信息
def MatchCityAndScenic(text):
    url = 'https://search.heweather.net/find?location='+text+'&key=cc33b9a52d6e48de852477798980b76e&group=cn&mode=match'
    html = requests.get(url)
    html.encoding = 'utf8'
    data = html.json()
    status = data['HeWeather6'][0]['status']
    cities = []
    scenic = []
    if status=='ok':
        res = data['HeWeather6'][0]['basic']
        for tmp in res:
            if tmp['type']=='city':
                # city_info = '城市名称:'+tmp['location']+',所属国家:'+tmp['cnty']+',所属城市:'+tmp['parent_city']+\
                #             ',所属行政区:'+tmp['admin_area']
                cities.append(tmp)
            elif tmp['type']=='scenic':
                # scenic_info = '景点名称:' + tmp['location'] + ',所属国家:' + tmp['cnty'] + ',所属城市:' + \
                #               tmp['parent_city'] + ',所属行政区:' + tmp['admin_area']
                scenic.append(tmp)
    return cities,scenic


# 精确获取中国城市/景区信息
def EqualCityAndScenic(text):
    url = 'https://search.heweather.net/find?location='+text+'&key=cc33b9a52d6e48de852477798980b76e&group=cn&mode=equal'
    html = requests.get(url)
    html.encoding = 'utf8'
    data = html.json()
    status = data['HeWeather6'][0]['status']
    cities = []
    scenic = []
    if status=='ok':
        res = data['HeWeather6'][0]['basic']
        for tmp in res:
            if tmp['type']=='city':
                # city_info = '城市名称:'+tmp['location']+',所属国家:'+tmp['cnty']+',所属城市:'+tmp['parent_city']+\
                #             ',所属行政区:'+tmp['admin_area']
                cities.append(tmp)
            elif tmp['type']=='scenic':
                # scenic_info = '景点名称:' + tmp['location'] + ',所属国家:' + tmp['cnty'] + ',所属城市:' + \
                #               tmp['parent_city'] + ',所属行政区:' + tmp['admin_area']
                scenic.append(tmp)
    return cities,scenic


# 获取某一地区的实时天气
def getWeatherNowByLocation(text):
    cities,scenic = EqualCityAndScenic(text)
    content = []
    if not len(cities)==0:
        for city in cities:
            location = city['location']
            weather = getWeatherNow(location)
            content.append(weather)
    if not len(scenic)==0:
        for scene in scenic:
            location = scene['location']
            weather = getWeatherNow(location)
            content.append(weather)
    return content


# 获取某一地区7天天气
def getWeatherRecentByLocation(text):
    cities, scenic = EqualCityAndScenic(text)
    content = []
    if not len(cities) == 0:
        for city in cities:
            location = city['location']
            weather = getWeatherForecast(location)
            content.append(weather)
    if not len(scenic) == 0:
        for scene in scenic:
            location = scene['location']
            weather = getWeatherForecast(location)
            content.append(weather)
    return content


# 获取某一地区24小时天气
def getWeatherDayByLocation(text):
    cities, scenic = EqualCityAndScenic(text)
    content = []
    if not len(cities) == 0:
        for city in cities:
            location = city['location']
            weather = getWeatherHourly(location)
            content.append(weather)
    if not len(scenic) == 0:
        for scene in scenic:
            location = scene['location']
            weather = getWeatherHourly(location)
            content.append(weather)
    return content


# if __name__ == '__main__':
#     text = ''
#     result1,result2 = MatchCityAndScenic(text)
#     print(result1)
#     if len(result1)==0:
#         print('没有找到您所要查询的地区')
#     else:
#         for result in result1:
#             weather = getWeatherNow(result['location'])
#             print(weather)
    # print(result1)
    # print(result2)
    # city = ''
    # result = getWeatherNow(city)