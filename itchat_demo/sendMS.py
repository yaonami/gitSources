import itchat
import time
import os

import message
import weather
import robot
import friend


# 发送消息给文件传输助手
def sendMsg(msg):
    itchat.send(msg, 'filehelper')


# 通过昵称发送消息
def sendMsgByNickName(nickName,msg):
    info = itchat.search_friends(nickName)[0]
    itchat.send(msg, info['UserName'])

# 发送图片给文件传输助手
def sendPicture(picture):
    itchat.send_image(picture, 'filehelper')


# 通过昵称发送图片
def sendPictureByNickName(nickName,picture):
    info = itchat.search_friends(nickName)[0]
    print(info)
    itchat.send_image(picture, info['UserName'])


# 发送每日推荐句子
def sendSentence(remarkNames):
    content,note,voicePath = message.getSentence()
    msg = '今天分享的句子：' + '\n' + content + '\n' + note +'\n'+'下面是音频文件'
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        time.sleep(2)
        itchat.send_msg(msg, info['UserName'])
        time.sleep(2)
        itchat.send_file(voicePath, info['UserName'])


# 发送机器人使用提示
def sendTips(remarkNames):
    msg = '小叮咚上线啦' + '\n' + '每天22:00-8:00' + '\n' + '开启聊天请回复"小叮咚"' + '\n' + '结束聊天请回复"小叮咚再见"'
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        time.sleep(2)
        itchat.send_msg(msg, info['UserName'])


# 发送早上好
def sendMorning(remarkNames):
    msg = ' 任何收获都不是巧合，而是用日复一日的付出换来。不怕你每天迈的步子太小，只怕你停滞不前；不怕你每天做的事太少，' \
          '只怕你无所事事。今日一点一滴的进步，终会塑造一个与众不同的你。新的一天，早安！'
    today = time.strftime("%Y%m%d")
    picture = './picture/' + today + '-morning.gif'
    # print(picture)
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        time.sleep(2)
        itchat.send_msg(msg, info['UserName'])
        if os.path.exists(picture):
            time.sleep(2)
            itchat.send_image(picture, info['UserName'])


# 发送天气使用提示
def sendWeatherTips(remarkNames):
    msg = '天气小助手上线啦' + '\n' + '回复数字后面内容：' + '\n' + '1.实况天气-所在城区' + '\n' \
          + '2.未来7天天气预报-所在城区' + '\n' + '3.未来24小时天气预报-所在城区' + '\n' + '4.生活小贴士-所在城区' + '\n'
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        itchat.send_msg(msg, info['UserName'])


# 发送晚安语
def sendEvening(remarkNames):
    msg_list = ['让夜风带走一天的疲惫，让月光驱走一天的烦恼，让星星点亮一天的好心情，祝你轻松入眠，美梦连篇，晚安。',
                '白天不论再忙，夜晚也是要睡的；工作不论再烦，休息也是必须的；无论心里有多少千头万绪，记住，没有过不去的坎儿，'
                '休息好了什么都可以搞定！晚安。',
                '人生中，我们有太多的烦恼与浮躁，伴随着这个冬季的寒冷而来。只有晚上，家是温暖的，心是清闲的，'
                '因而我们应懂得享受。晚安。',
                '生活总会有酸有甜，能微笑面对便是强者；人生总会有得有失，能平淡看待便是智者；朋友总会有聚有散，'
                '能经常联系便是知己。晚安。',
                '幸福很简单，就是每天过得平淡美好。每天花点时间，满足自己的饥渴。因为我们追求的是自己的幸福，'
                '而不是比别人幸福，晚安。',
                '大千世界，我们并不是缺少一个说话的朋友，而是渴望一个理解自己读懂自己的伙伴。晚安。',
                '总有人会穿越人海找到你，拥抱你，无论海水涨潮还是退潮，无论日出还是日落，他都会坚定地奔向你，不退缩，'
                '不犹豫。晚安。']
    msg = '总有人会穿越人海找到你，拥抱你，无论海水涨潮还是退潮，无论日出还是日落，他都会坚定地奔向你，不退缩，不犹豫。晚安。'
    today = time.strftime("%Y%m%d")
    picture = 'picture/' + str(today) + '-evening.gif'
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        itchat.send_msg(msg, info['UserName'])
        # print(picture)
        # print(os.path.exists(picture))
        # itchat.send('@%img@%s' % picture, info['UserName'])
        if os.path.exists(picture):
            itchat.send_image(picture, info['UserName'])


# 发送语言检测助手使用说明
def sendDetectLanguageTips(remarkNames):
    msg = '语言检测助手上线啦' + '\n' + '开启检测请回复"语言检测助手"' + '\n' + '结束检测请回复"结束检测"'
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        itchat.send_msg(msg, info['UserName'])


# 发送翻译助手使用说明
def sendTranslationTips(remarkNames):
    msg = '小小翻译官上线啦\n目前小小翻译官支持：\n中-英互译\n中-法互译\n中-日互译\n中-德互译\n中-韩互译\n========\n开启翻译请回复:"小小翻译官"\n结束翻译请回复:"小小翻译官再见"'
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        itchat.send_msg(msg, info['UserName'])


# 程序启动提示
def sendMsgTips(remarkNames):
    msg = '小叮咚今日重新上线啦，请您踊跃体验小叮咚功能,谢谢您!'
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        itchat.send_msg(msg, info['UserName'])


# 发送小叮咚使用说明
def sendRobotUseGuide(remarkNames):
    msg = '小叮咚使用指南\n启动小叮咚请回复(小叮咚)\n关闭小叮咚请回复(小叮咚再见)\n小叮咚下设自动聊天,翻译和天气查询功能\n' \
          '开启翻译请回复(翻译)\n开启天气查询请回复(天气)\n自动聊天请回复你想说的话'
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        itchat.send_msg(msg, info['UserName'])


# 给特定某一人发送小叮咚使用指南
def sendRobotUseGuideToOne(username):
    msg = '小叮咚使用指南\n启动小叮咚请回复(小叮咚)\n关闭小叮咚请回复(小叮咚再见)\n小叮咚下设自动聊天,翻译和天气查询功能\n' \
          '开启翻译请回复(翻译)\n开启天气查询请回复(天气)\n自动聊天请回复你想说的话'
    itchat.send(msg, username)


# 给特定的某一人发送开启小叮咚使用指南
def sendStartRobotUseGuideToOne(username):
    msg = '小叮咚使用指南\n启动小叮咚请回复(小叮咚)\n关闭小叮咚请回复(小叮咚再见)'
    itchat.send(msg, username)


# 给特定的某一人发送翻译助手使用指南
def sendTranslationUseGuide(username):
    msg = '小小翻译官使用指南\n开启翻译请回复(翻译)\n结束翻译请回复(小小翻译官再见)\n小小翻译官目前支持中英互译和中日互译\n' \
          '选择中英互译请回复(中英互译)\n选择中日互译请回复(中日互译)'
    itchat.send(msg, username)


# 给特定的某人发送天气使用指南
def sendWeatherUseGuide(username):
    msg = '天气小助手使用指南\n开启天气小助手请回复(天气)\n结束天气小助手请回复(天气小助手再见)\n天气小助手目前支持' \
          '查询实时天气，未来24小时天气，未来7天天气\n查询实时天气请回复(实时天气)\n退出实时天气查询请回复(关闭实时天气)' \
          '\n查询未来7天天气请回复(7天天气)\n退出未来7天天气查询请回复(关闭7天天气)\n' \
          '查询未来24小时天气请回复(24小时天气)\n退出未来24小时天气查询请回复(关闭24小时天气)'
    itchat.send(msg, username)


def sendPictureTips(remarkNames):
    msg = '发送给我一张图片，还你一张更好玩的图片，不试会后悔哦~~~'
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        itchat.send_msg(msg, info['UserName'])
