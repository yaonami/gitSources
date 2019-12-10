import itchat


# 发送消息给自己
def sendMsg(msg):
    itchat.send(msg, '@b5bc0ef02627f80b23f63efdf6b0fd22764f9533945900cd51726a2767a234d1')


# 通过昵称发送消息
def sendMsgByNickName(nickName,msg):
    info = itchat.search_friends(nickName)[0]
    itchat.send(msg, info['UserName'])


