import itchat
import time

import message
import weather
import robot
import friend


# 发送消息给自己
# def sendMsg(msg):
#     itchat.send(msg, '@b5bc0ef02627f80b23f63efdf6b0fd22764f9533945900cd51726a2767a234d1')


# 通过昵称发送消息
def sendMsgByNickName(nickName,msg):
    info = itchat.search_friends(nickName)[0]
    itchat.send(msg, info['UserName'])

# 发送图片给自己
# def sendPicture(picture):
#     itchat.send_image(picture, '@b5bc0ef02627f80b23f63efdf6b0fd22764f9533945900cd51726a2767a234d1')


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
        itchat.send_msg(msg, info['UserName'])
        itchat.send_file(voicePath, info['UserName'])


# 发送提示
def sendTips(remarkNames):
    msg = '小叮咚上线啦' + '\n' + '每天22:00-8:00' + '\n' + '开启聊天请回复"小叮咚"' + '\n' + '结束聊天请回复"小叮咚再见"'
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        itchat.send_msg(msg, info['UserName'])


# 发送早上好
def sendMorning(remarkNames):
    msg = '新的一天从微笑开始,早安！'
    today = time.strftime("%Y%m%d")
    picture = 'picture/' + today + '-morning.gif'
    # print(picture)
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        itchat.send_msg(msg, info['UserName'])
        itchat.send_image(picture, info['UserName'])


# 发送天气提示
def sendWeatherTips(remarkNames):
    msg = '天气小助手上线啦' + '\n' + '回复数字后面内容：' + '\n' + '1.实况天气-所在城区' + '\n' \
          + '2.未来7天天气预报-所在城区' + '\n' + '3.未来24小时天气预报-所在城区' + '\n' + '4.生活小贴士-所在城区' + '\n'
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        itchat.send_msg(msg, info['UserName'])


def sendEvening(remarkNames):
    msg = '让夜风带走一天的疲惫，让月光驱走一天的烦恼，让星星点亮一天的好心情，祝你轻松入眠，美梦连篇，晚安。'
    today = time.strftime("%Y%m%d")
    picture = 'picture/' + today + '-evening.gif'
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        itchat.send_msg(msg, info['UserName'])
        itchat.send_image(picture, info['UserName'])


# 程序启动提示
def sendMsgTips(remarkNames):
    msg = '做个小测试，接下来的几天可能会不定时收到来自本账号的消息，如果觉得被打扰，请微信回复本账号，' \
          '如果有任何建议或意见，也可以微信回复，谢谢您'
    for remarkName in remarkNames:
        info = itchat.search_friends(remarkName)[0]
        itchat.send_msg(msg, info['UserName'])