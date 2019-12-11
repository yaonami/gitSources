import itchat


# 获取全部好友的UserName信息
def getAllFriends():
    friends = itchat.get_friends(update=True)
    friends_UserName = []
    for friend in friends:
        friends_UserName.append(friend['UserName'])
    return friends_UserName


# 将好友与控制机器人的状态组成字典
def createUserStatusDict():
    UserNameList = getAllFriends()
    statusList = []
    for i in range(len(UserNameList)):
        statusList.append(False)
    user_status = dict(zip(UserNameList, statusList))
    return user_status


# 将好友与天气和机器人组成字典
def createUserStatusRWDict():
    UserNameList = getAllFriends()
    status = []
    for i in range(len(UserNameList)):
        userStatus = {'weather':False,'robot':False}
        status.append(userStatus)
    user_status = dict(zip(UserNameList,status))
    return user_status


# 根据UserName，昵称，微信号，备注名获取好友信息
def get_friend(name):
    friends = itchat.search_friends(name=name)
    print(friends)
    for friend in friends:
        print(friend)