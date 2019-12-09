import itchat


def sendMsg():
    itchat.send('hello,nice to meet you!', '@cd6ec55721dbed471f992ad8de4b5877c06bb7243814b62fff0bb26a656a5d10')


def sendMsgByNickName(nickName,msg):
    info = itchat.search_friends(nickName)
    itchat.send(msg, info['UserName'])