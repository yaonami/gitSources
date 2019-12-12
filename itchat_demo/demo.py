


# @itchat.msg_register(TEXT)
# def sendDetectLanguage(msg):
#     global user_status
#     print(msg)
#     if user_status[msg['FromUserName']]:
#         if msg['Text'] == '结束检测':
#             itchat.send('语言检测助手下线啦', msg['FromUserName'])
#             user_status[msg['FromUserName']] = False
#         else:
#             info = translation.detect_language(msg['Text'])
#             itchat.send(info, msg['FromUserName'])
#     else:
#         if msg['Text'] == '语言检测助手':
#             itchat.send('语言检测助手到', msg['FromUserName'])
#             user_status[msg['FromUserName']] = True


# @itchat.msg_register(TEXT)
# def sendMsgByQYKRobot(msg):
#     print(msg)
#     global user_status
#     if user_status[msg['FromUserName']]:
#         if msg['Text']=='小叮咚再见':
#             itchat.send('再见!', msg['FromUserName'])
#             user_status[msg['FromUserName']] = False
#         else:
#             info = robot.QINGYUNKERobot(msg['Text'])
#             time.sleep(2)
#             itchat.send(info, msg['FromUserName'])
#     else:
#         if msg['Text'] == '小叮咚':
#             itchat.send('在的呢!', msg['FromUserName'])
#             user_status[msg['FromUserName']] = True


# @itchat.msg_register(TEXT)
# def sendWeather(msg):
#     print(msg)
#     type_info = msg['Text'].split('-')[0]
#     area = msg['Text'].split('-')[1]
#     res = ''
#     if type_info=='实况天气':
#         weather_info = weather.getWeatherNow(area)
#         print(weather_info)
#         info = '当前所在地区：'+weather_info['地区']+'\n'+'天气更新时间：'+weather_info['更新时间']+'\n'+'当前天气：'\
#                +weather_info['当前天气']+'\n'+'当前风向：'+weather_info['当前风向']+'\n'+'当前风力：'\
#                +weather_info['当前风力']+'级'+'\n'+'能见度：'+weather_info['能见度']+' KM'+'\n'+'当前温度：'\
#                +weather_info['当前温度']+'℃'+'\n'+'体感温度：'+weather_info['体感温度']+'℃'
#         res = info
#     elif type_info=='未来7天天气预报':
#         weather_info = weather.getWeatherForecast(area)
#         print(weather_info)
#         infos = ''
#         for w in weather_info:
#             info = '日期：'+w['日期']+'\n'+'白天天气：'+w['白天天气']+'\n'+'夜间天气：'+w['夜间天气']+'\n'+'风向：'\
#                    +w['风向']+'\n'+'风力：'+w['风力']+'级'+'\n'+'最低温度：'+w['最低温度']+'℃'+'\n'+'最高温度：'\
#                    +w['最高温度']+'℃'+'\n'+'能见度：'+w['能见度']+' KM'+'\n'+'--------'+'\n'
#             infos = infos + info
#         res = infos
#     elif type_info=='未来24小时天气预报':
#         weather_info = weather.getWeatherHourly(area)
#         print(weather_info)
#         infos = ''
#         for w in weather_info:
#             info = '时间：'+w['时间']+'\n'+'天气：'+w['天气']+'\n'+'风向：'+w['风向']+'\n'+'风力：'\
#                    +w['风力']+'级'+'\n'+'温度：'+w['温度']+'℃'+'\n'+'--------'+'\n'
#             infos = infos + info
#         res = infos
#     elif type_info == '生活小贴士':
#         weather_info = weather.getWeatherLifestyle(area)
#         infos = ''
#         for w in weather_info:
#             f,b = str(w)[1:len(str(w))-1].split(':')
#             info = f[1:len(f)-1] + '：'+b[2:len(b)-1]+'\n'+'========'+'\n'
#             infos = infos + info
#         res = infos
#     return res


# @itchat.msg_register(TEXT)
# def sendMsgByTLRobot(msg):
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


# @itchat.msg_register(TEXT)
# def sendTranslation(msg):
#     global user_status
#     print(msg)
#     if user_status[msg['FromUserName']]:
#         if msg['Text'] == '小小翻译官再见':
#             itchat.send('再见~', msg['FromUserName'])
#             user_status[msg['FromUserName']] = False
#         else:
#             language = translation.detect_language(msg['Text'])
#             itchat.send('您当前输入的语言为：'+language, msg['FromUserName'])
#             results = translation.translationText(msg['Text'],language)
#             if len(results)==0:
#                 itchat.send('很抱歉无法为您匹配对应的翻译，我会持续改进的，感谢您的使用', msg['FromUserName'])
#             else:
#                 for result in results:
#                     itchat.send(result['language']+'翻译为：\n'+result['content']+'\n下面是'+result['language']+'读音', msg['FromUserName'])
#                     itchat.send_file(result['voice'], msg['FromUserName'])
#     else:
#         if msg['Text'] == '小小翻译官':
#             itchat.send('在的呢，您可以输入您想翻译的内容哦~', msg['FromUserName'])
#             user_status[msg['FromUserName']] = True


# if __name__ == "__main__":
#     global user_status
#     login()
#     user_status = friend.createUserStatusDict()
    # print(user_status)
    # user_status = friend.createUserStatusRWDict()
    # print(user_status)
    # sentence_remarkNames = ['A大树','D肖健伟','XC罗','X度小囡','X李涛','X十一','X云熙','XL先生']
    # sentence_remarkNames = ['A大树']
    # itchat.send_image('picture/20191211-evening.gif', 'filehelper')
    # sendMS.sendEvening(sentence_remarkNames)
    # sendMS.sendMorning(sentence_remarkNames)
    # sendMS.sendTranslationTips(sentence_remarkNames)
    # sendMS.sendDetectLanguageTips(sentence_remarkNames)
    # sendMS.sendMsgTips(sentence_remarkNames)
    # sendMS.sendEvening(sentence_remarkNames)
    # sendMS.sendMorning(sentence_remarkNames)
    # sendMS.sendTips(sentence_remarkNames)
    # sendMS.sendWeatherTips(sentence_remarkNames)
    # sendMS.sendSentence(sentence_remarkNames)
    # itchat.send_file('1.mp3', 'filehelper')
    # sendMS.sendPicture('pic7.gif')
    # sendMS.sendPictureByNickName('一人一歌一世界','pic7.gif')
    # friend.get_friend('文件传输助手')
    # print(user_status)
    # print(tmp)
    # scheduler = BlockingScheduler()
    # scheduler = BackgroundScheduler()
    # # scheduler.add_job(print_time, 'date', run_date='2019-12-7 14:35:00')
    # scheduler.add_job(sendMsgByQYKRobot, trigger='cron', hour='20', minute='18')
    # scheduler.add_job(sendWeather, trigger='cron', hour='20', minute='20')
    # scheduler.add_job(login, 'cron', hour='21', minute='00')
    # scheduler.add_job(sendMS.sendTranslationTips, args=[sentence_remarkNames,], trigger='cron', hour='21', minute='01')
    # scheduler.add_job(sendMS.sendTranslationTips, args=[sentence_remarkNames,], trigger='cron', hour='20', minute='33')
    # scheduler.add_job(sendMS.sendTips, args=[sentence_remarkNames,], trigger='cron', hour='22', minute='01')
    # scheduler.add_job(sendMS.sendTips, args=[sentence_remarkNames,], trigger='cron', hour='20', minute='36')
    # scheduler.add_job(sendMS.sendEvening, args=[sentence_remarkNames,], trigger='cron', hour='22', minute='30')
    # scheduler.add_job(sendMS.sendEvening, args=[sentence_remarkNames,], trigger='cron', hour='20', minute='37')
    # # scheduler.add_job(print_time, 'interval', seconds=10)
    # scheduler.add_job(sendMS.sendMsg, trigger='cron', hour='15', minute='03')
    # scheduler.add_job(sendMS.sendMsg, args=['起床啦，新的一天从微笑开始！',], trigger='cron', hour='15', minute='11')
    # scheduler.add_job(sendMS.sendMorning, args=[sentence_remarkNames, ], trigger='cron', hour='7', minute='0')
    # scheduler.add_job(sendMS.sendMorning, args=[sentence_remarkNames, ], trigger='cron', hour='20', minute='38')
    # scheduler.add_job(sendMS.sendSentence, args=[sentence_remarkNames,], trigger='cron', hour='7', minute='30')
    # scheduler.add_job(sendMS.sendSentence, args=[sentence_remarkNames,], trigger='cron', hour='20', minute='39')
    # scheduler.add_job(sendMS.sendWeatherTips, args=[sentence_remarkNames,], trigger='cron', hour='8', minute='0')
    # scheduler.start()
    # print_time()
    # tmp = weather.getWeatherForecast('北京')
    # tmp = weather.getWeatherHourly('北京')
    # tmp = weather.getWeatherLifestyle('北京')
    # tmp = weather.getWeatherNow('南昌')
    # print(tmp)
    # itchat.run()
    # while True:
    #     pass
    # info  = robot.get_response('123')
    # print(info)