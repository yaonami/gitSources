import itchat
from itchat.content import *
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import time

import sendMS
import weather
import robot
import friend


def login():
    itchat.auto_login(hotReload=True)


def print_time():
    print(time.time())


@itchat.msg_register(TEXT)
def sendWeather(msg):
    type_info = msg['Text'].split('-')[0]
    area = msg['Text'].split('-')[1]
    res = ''
    if type_info=='实况天气':
        weather_info = weather.getWeatherNow(area)
        print(weather_info)
        info = '当前所在地区：'+weather_info['地区']+'\n'+'天气更新时间：'+weather_info['更新时间']+'\n'+'当前天气：'\
               +weather_info['当前天气']+'\n'+'当前风向：'+weather_info['当前风向']+'\n'+'当前风力：'\
               +weather_info['当前风力']+'级'+'\n'+'能见度：'+weather_info['能见度']+' KM'+'\n'+'当前温度：'\
               +weather_info['当前温度']+'℃'+'\n'+'体感温度：'+weather_info['体感温度']+'℃'
        res = info
    elif type_info=='未来7天天气预报':
        weather_info = weather.getWeatherForecast(area)
        print(weather_info)
        infos = ''
        for w in weather_info:
            info = '日期：'+w['日期']+'\n'+'白天天气：'+w['白天天气']+'\n'+'夜间天气：'+w['夜间天气']+'\n'+'风向：'\
                   +w['风向']+'\n'+'风力：'+w['风力']+'级'+'\n'+'最低温度：'+w['最低温度']+'℃'+'\n'+'最高温度：'\
                   +w['最高温度']+'℃'+'\n'+'能见度：'+w['能见度']+' KM'+'\n'+'--------'+'\n'
            infos = infos + info
        res = infos
    elif type_info=='未来24小时天气预报':
        weather_info = weather.getWeatherHourly(area)
        print(weather_info)
        infos = ''
        for w in weather_info:
            info = '时间：'+w['时间']+'\n'+'天气：'+w['天气']+'\n'+'风向：'+w['风向']+'\n'+'风力：'\
                   +w['风力']+'级'+'\n'+'温度：'+w['温度']+'℃'+'\n'+'--------'+'\n'
            infos = infos + info
        res = infos
    elif type_info == '生活指数':
        weather_info = weather.getWeatherLifestyle(area)
        infos = ''
        for w in weather_info:
            f,b = str(w)[1:len(str(w))-1].split(':')
            info = f[1:len(f)-1] + '：'+b[2:len(b)-1]+'\n'+'========'+'\n'
            infos = infos + info
        res = infos
    return res


# @itchat.msg_register(TEXT)
# def sendMsgByRobot(msg):
#     global user_status
#     if user_status[msg['FromUserName']]:
#         if msg['Text']=='小叮咚再见':
#             itchat.send('再见!', msg['FromUserName'])
#             user_status[msg['FromUserName']] = False
#         else:
#             info = robot.get_response(msg['Text'])
#             itchat.send(info, msg['FromUserName'])
#     else:
#         if msg['Text']=='小叮咚':
#             itchat.send('在的呢!', msg['FromUserName'])
#             user_status[msg['FromUserName']] = True

@itchat.msg_register(TEXT)
def sendMsgByRobot(msg):
    global user_status
    if user_status[msg['FromUserName']]:
        if msg['Text']=='小叮咚再见':
            itchat.send('再见!', msg['FromUserName'])
            user_status[msg['FromUserName']] = False
        else:
            info = robot.QINGYUNKERobot(msg['Text'])
            itchat.send(info, msg['FromUserName'])
    else:
        if msg['Text'] == '小叮咚':
            itchat.send('在的呢!', msg['FromUserName'])
            user_status[msg['FromUserName']] = True


if __name__ == "__main__":
    global user_status
    login()
    user_status = friend.createUserStatusDict()
    # friend.get_friend('@cd6ec55721dbed471f992ad8de4b5877c06bb7243814b62fff0bb26a656a5d10')
    # print(user_status)
    # print(tmp)
    # scheduler = BlockingScheduler()
    # scheduler = BackgroundScheduler()
    # # scheduler.add_job(print_time, 'date', run_date='2019-12-7 14:35:00')
    # scheduler.add_job(login, 'cron', hour='6', minute='30')
    # # scheduler.add_job(print_time, 'interval', seconds=10)
    # scheduler.add_job(sendMS.sendMsg, trigger='cron', hour='15', minute='03')
    # scheduler.add_job(sendMS.sendMsg, args=['起床啦，新的一天从微笑开始！',], trigger='cron', hour='15', minute='11')
    # scheduler.start()
    itchat.run()
    # print_time()
    # tmp = weather.getWeatherForecast('北京')
    # tmp = weather.getWeatherHourly('北京')
    # tmp = weather.getWeatherLifestyle('北京')
    # tmp = weather.getWeatherNow('南昌')
    # print(tmp)
    # while True:
    #     pass
    # info  = robot.get_response('123')
    # print(info)

