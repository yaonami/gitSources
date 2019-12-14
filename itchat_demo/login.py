import itchat
from itchat.content import *
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import time
import os

import sendMS
import weather
import robot
import friend
import translation
import emojiUrl


def login():
    itchat.auto_login(hotReload=True)


def print_time():
    print(time.time())


# @itchat.msg_register(TEXT)
# def auto_reply(msg):
#     print(msg)


@itchat.msg_register(PICTURE)
def auto_reply_picture(msg):
    print(msg)
    path1 = r'D:\gitSources\itchat_demo\emoji_picture'
    picture_path = os.path.join(path1,msg.fileName)
    msg.download(picture_path)
    emojiUrl.getEmoji(msg['FromUserName'],picture_path)
    path1 = r'D:\gitSources\itchat_demo\emoji_image'
    emoji_path = os.path.join(path1, msg['FromUserName'],'emoji-mosaic.jpg')
    itchat.send_image(emoji_path, msg['FromUserName'])


@itchat.msg_register(TEXT)
def auto_reply_text(msg):
    global user_status,function_status
    print(msg)
    msg_text = msg['Text']
    username = msg['FromUserName']
    if user_status[username]:
        if msg_text=='小叮咚再见':
            itchat.send('再见，期待下次与你相遇！', username)
            sendMS.sendStartRobotUseGuideToOne(username)
            user_status[username] = False
            function_status[username] = friend.setFunctionStatusFalse()
        else:
            user_status[username] = True
            if function_status[username]['translation']['status']:
                if function_status[username]['translation']['中英互译']:
                    # 执行中英互译方法
                    content,voicePath = translation.translationZE(msg_text)
                    if content=='':
                        itchat.send('非常抱歉，未能对您回复的内容进行翻译', username)
                    else:
                        itchat.send(content, username)
                    if not voicePath=='':
                        itchat.send_file(voicePath, username)
                    function_status[username]['translation']['中英互译'] = False
                    itchat.send('本次翻译任务已经完成\n如果想要退出翻译，请回复括号中内容(小小翻译官再见)\n如果想要再次翻译，请回复需要翻译的语言(中英互译或中日互译)', username)
                elif function_status[username]['translation']['中日互译']:
                    # 执行中日互译方法
                    content, voicePath = translation.translationZJ(msg_text)
                    if content == '':
                        itchat.send('非常抱歉，未能对您回复的内容进行翻译', username)
                    else:
                        itchat.send(content, username)
                    if not voicePath == '':
                        itchat.send_file(voicePath, username)
                    function_status[username]['translation']['中日互译'] = False
                    itchat.send('本次翻译任务已经完成\n如果想要退出翻译，请回复括号中内容(小小翻译官再见)\n如果想要再次翻译，请回去需要翻译的语言(中英互译或中日互译)', username)
                else:
                    if msg_text=='小小翻译官再见':
                        function_status[username]['translation']['status'] = False
                        itchat.send('感谢使用小小翻译官，再见~', username)
                        itchat.send('启动小小翻译官请回复(翻译)', username)
                    elif msg_text=='中英互译':
                        function_status[username]['translation']['中英互译'] = True
                        function_status[username]['translation']['中日互译'] = False
                        itchat.send('请回复您要翻译的内容', username)
                    elif msg_text=='中日互译':
                        function_status[username]['translation']['中日互译'] = True
                        function_status[username]['translation']['中英互译'] = False
                        itchat.send('请回复您要翻译的内容', username)
                    else:
                        itchat.send('小小翻译官无法识别需要翻译的内容，请阅读下面的小小翻译官使用说明', username)
                        sendMS.sendTranslationUseGuide(username)
            elif function_status[username]['weather']['status']:
                if function_status[username]['weather']['实时天气']:
                    if msg_text=='关闭实时天气':
                        function_status[username]['weather']['实时天气'] = False
                        itchat.send('已为您关闭实时天气查询\n重新开启实时天气请回复(实时天气', username)
                        sendMS.sendWeatherUseGuide(username)
                    else:
                        res = weather.getWeatherNowByLocation(msg_text)
                        if len(res)==0:
                            itchat.send('未获取到您所查询的地区天气情况，请确定您输入的地区是否正确', username)
                        else:
                            for r in res:
                                if len(r)==0:
                                    itchat.send('未获取到您所查询的地区天气情况，请确定您输入的地区是否正确', username)
                                else:
                                    weather_content = r[0]
                                    send_content = '地区:'+weather_content['地区']+'\n获取时间:'\
                                                   +weather_content['更新时间']+'\n当前温度:'\
                                                   +weather_content['当前温度']+'\n体感温度:'\
                                                   +weather_content['体感温度']+'\n天气情况:'\
                                                   +weather_content['当前天气']+'\n当前风向:'\
                                                   +weather_content['当前风向']+'\n当前风力:'\
                                                   +weather_content['当前风力']+'\n能见度:'+weather_content['能见度']
                                    itchat.send(send_content, username)
                        itchat.send('结束查询请回复(关闭实时天气)\n继续查询请回复查询地区', username)
                elif function_status[username]['weather']['小时天气']:
                    if msg_text == '关闭24小时天气':
                        function_status[username]['weather']['小时天气'] = False
                        itchat.send('已为您关闭24小时天气查询\n重新开启实时天气请回复(24小时天气', username)
                        sendMS.sendWeatherUseGuide(username)
                    else:
                        res = weather.getWeatherDayByLocation(msg_text)
                        if len(res)==0:
                            itchat.send('未获取到您所查询的地区天气情况，请确定您输入的地区是否正确', username)
                        else:
                            for r in res:
                                if len(r)==0:
                                    itchat.send('未获取到您所查询的地区天气情况，请确定您输入的地区是否正确', username)
                                else:
                                    for result in r:
                                        hour_weather = '地区:'+result['地区']+'\n时间:'+result['时间']+'\n天气:'\
                                                       +result['天气']+'温度:'+result['温度']+'\n风力:'\
                                                       +result['风力']+'\n风向:'+result['风向']
                                        itchat.send(hour_weather, username)
                        itchat.send('结束查询请回复(关闭24小时天气)\n继续查询请回复查询地区', username)
                elif function_status[username]['weather']['多天天气']:
                    if msg_text == '关闭7天天气':
                        function_status[username]['weather']['多天天气'] = False
                        itchat.send('已为您关闭7天天气查询\n重新开启实时天气请回复(7天天气', username)
                        sendMS.sendWeatherUseGuide(username)
                    else:
                        res = weather.getWeatherRecentByLocation(msg_text)
                        if len(res)==0:
                            itchat.send('未获取到您所查询的地区天气情况，请确定您输入的地区是否正确', username)
                        else:
                            for r in res:
                                if len(r)==0:
                                    itchat.send('未获取到您所查询的地区天气情况，请确定您输入的地区是否正确', username)
                                else:
                                    for result in r:
                                        day_weather = '地区:'+result['地区']+'\n日期:'+result['日期']+'\n最高温度:'\
                                                      +result['最高温度']+'\n最低温度:'\
                                                      +result['最低温度']+'\n白天天气:'\
                                                      +result['白天天气']+'\n夜间天气:'\
                                                      +result['夜间天气']+'\n风向:'\
                                                      +result['风向']+'\n风力:'\
                                                      +result['风力']+'\n能见度:'+result['能见度']
                                        itchat.send(day_weather, username)
                        itchat.send('结束查询请回复(关闭7天天气)\n继续查询请回复查询地区', username)
                else:
                    if msg_text=='实时天气':
                        function_status[username]['weather']['实时天气'] = True
                        function_status[username]['weather']['小时天气'] = False
                        function_status[username]['weather']['多天天气'] = False
                        itchat.send('请回复您想要查询的地区名称', username)
                    elif msg_text=='24小时天气':
                        function_status[username]['weather']['实时天气'] = False
                        function_status[username]['weather']['小时天气'] = True
                        function_status[username]['weather']['多天天气'] = False
                        itchat.send('请回复您想要查询的地区名称', username)
                    elif msg_text=='7天天气':
                        function_status[username]['weather']['实时天气'] = False
                        function_status[username]['weather']['小时天气'] = False
                        function_status[username]['weather']['多天天气'] = True
                        itchat.send('请回复您想要查询的地区名称', username)
                    elif msg_text=='天气小助手再见':
                        function_status[username]['weather']['status'] = False
                        itchat.send('感谢使用天气小助手，再见~', username)
                        itchat.send('启动天气小助手请回复(天气)', username)
                    else:
                        itchat.send('天气小助手无法识别您想要查询的内容，请阅读下面的天气小助手使用说明', username)
                        sendMS.sendWeatherUseGuide(username)
            else:
                if msg_text=='翻译':
                    function_status[username]['translation']['status'] = True
                    function_status[username]['weather']['status'] = False
                    sendMS.sendTranslationUseGuide(username)
                elif msg_text=='天气':
                    function_status[username]['weather']['status'] = True
                    function_status[username]['translation']['status'] = False
                    sendMS.sendWeatherUseGuide(username)
                else:
                    # 启用聊天机器人
                    robotResult = robot.QINGYUNKERobot(msg_text)
                    itchat.send(robotResult, username)
    else:
        if msg_text=='小叮咚':
            itchat.send('在的呢~~\n接下来让小叮咚陪你愉快玩耍吧!!!', username)
            sendMS.sendRobotUseGuideToOne(username)
            user_status[username] = True
        else:
            user_status[username] = False



if __name__ == "__main__":
    global user_status,function_status
    login()
    # itchat.auto_login(hotReload=True)
    user_status = friend.createUserStatusDict()
    function_status = friend.createFunctionStatusDict()
    # itchat.run()
    sentence_remarkNames = ['A大树', 'D肖健伟', 'XC罗', 'X度小囡', 'X李涛', 'X十一', 'X云熙', 'XL先生']
    # sentence_remarkNames = ['A大树']
    # sendMS.sendPictureTips(sentence_remarkNames)
    scheduler = BackgroundScheduler()
    scheduler.add_job(sendMS.sendMorning, args=[sentence_remarkNames, ], trigger='cron', hour='7', minute='0')
    scheduler.add_job(sendMS.sendSentence, args=[sentence_remarkNames, ], trigger='cron', hour='7', minute='30')
    scheduler.add_job(login, 'cron', hour='20', minute='58')
    scheduler.add_job(sendMS.sendPictureTips, args=[sentence_remarkNames, ], trigger='cron', hour='21', minute='00')
    # scheduler.add_job(sendMS.sendRobotUseGuide, args=[sentence_remarkNames, ], trigger='cron', hour='22', minute='01')
    scheduler.add_job(sendMS.sendEvening, args=[sentence_remarkNames, ], trigger='cron', hour='22', minute='30')
    scheduler.start()
    while True:
        itchat.configured_reply()
        time.sleep(1)
        # pass