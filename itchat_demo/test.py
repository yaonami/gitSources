import itchat
from itchat.content import *
from time import sleep
import requests
import json
import base64
import six
from PIL import Image


# itchat.auto_login(hotReload=True)


# TEXT:文本-------文本内容
# MAP:地图--------位置文本
# CARD:名片-------推荐人字典
# NOTE:通知-------通知文本
# SHARING:分享----分享名称
@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def print_text(msg):
    print(msg['Text'])
    # return itchat.send(get_response(msg['Text']),'filehelper')
    # res = get_response(msg['Text'])
    res = QINGYUNKERobot(msg['Text'])
    sleep(2)
    return res


# PICTURE:图片/表情------下载方法
# RECORDING:语音---------下载方法
# ATTACHMENT:附件--------下载方法
# VIDEO:小视频-----------下载方法
@itchat.msg_register([PICTURE,RECORDING,ATTACHMENT,VIDEO])
def show_picture(msg):
    # print(type(picture))
    print(msg)
    msg.download(msg.fileName)
    # typeSymbol = {
    #     'Picture':'img',
    #     'Attachment':'fil',
    #     'Video':'vid',
    #     'Recording':'fil'
    # }
    # 根据消息类型，返回发送的消息
    # itchat.send('@%s@%s' % (typeSymbol[msg['Type']],msg['FileName']),msg['FromUserName'])
    # 消息类型是图片返回图片，消息类型不是图片全部当作文件
    itchat.send('@%s@%s' % ('img' if msg['Type']=='Picture' else 'fil' ,msg['FileName']),
        msg['FromUserName']
    )
    return '%s received' % msg['Type']

# FRIENDS:好友邀请-----添加好友所需参数
@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')


# isGroupChat:是否是群消息
# isAt:是否@本账号
@itchat.msg_register(TEXT,isGroupChat=True)
def reply_group(msg):
    print(msg)
    print(msg.isAt)
    print(msg.actualNickName)
    print(msg.text)
    if msg.text:
        itchat.send(msg.text,msg['FromUserName'])


# base64编码转换为PIL图片
def base64_to_PIL(String):
    try:
        base64_data = base64.b64decode(String)
        buf = six.BytesIO()
        buf.write(base64_data)
        buf.seek(0)
        img = Image.open(buf).convert('RGB')
        return img
    except:
       raise
        # return None


def QINGYUNKERobot(mes):
    engine = "http://api.qingyunke.com/api.php?key=free&appid=0&msg="
    try:
        url = engine + mes
        res = requests.get(url).json()
        return res["content"]
    except:
        raise
        # return "出错了"


# 图灵机器人
def get_response(msg):
    KEY = '8edce3ce905a4c1dbb965e6b35c3834d'
    apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'
    dat = {
        "perception": {
            "inputText": {
                "text": msg
            },
            "inputImage": {
                "url": "imageUrl"
            },
            "selfInfo": {
                "location": {
                    "city": "北京",
                    "province": "北京",
                    "street": "信息路"
                }
            }
        },
        "userInfo": {
            "apiKey": KEY,
            "userId": "fool"
        }
    }
    dat = json.dumps(dat)
    r = requests.post(apiUrl, data=dat).json()
    # print(r["results"][0]["values"]["text"])
    return r["results"][0]["values"]["text"]


# base64_image = '@c47f29c5e3529983fee22cf8aba59f93185ab892c02306e53ae823cc4ffca1f66298ea79a71c703c4ef9f1ad7992656415d4c438983cdf6e1208eac02c2cbf7abfa516e78db801e6115ee3bb90a0601625f21abf1e6bc09b67b97022079820d3a229e85b5d84a17c4be03cf8e67f4aa938ee93c4f14692788dafa356b546d52de8ac491009b397cd2ea2c54e5a523daecf9eb5a19d77aab02d8b79a8b3a58e42c41737f70959bc01b10a4d4091da0d41ba906200c86843b7c6b93647a228c4efdfb1b8604d24d467e1c7906f7c282a0af24db21798683dc2fe8fafc752f10a9c6aaff28e17791d7e9da3f526b61e1e7670f5f579984d853490e82b5dab65fb24459f751ec57ae1c85fd05d3c2108a6891c56f22554170193324d3bfa4b7820d591f1836224dc8bd0c254c3397c3917748cdecfe5e3d706c54bc09539a2a3a3c78dd0d1926fb5f23edffa4baa1a65b6c9358b381d1b16a87d15f4b6cd78b770d4c83c67a1aeeace07485bb4e3f0ce5aff0f067d95be69d8a304c8e4690e85507f8576116bb5716b91bc18764f548a0415091caaeaaaf174247927d83908604c608b7b605750519678bddb31a41109fe722a307315948204ac770251d6ed7d4c3cc55173718a5bde4664439fe51588e571939e3b3667b808b070a6d47feab7a9b9a4e5c73b21c92cf6e69e7394b49cc078ab6137ec2bacad08d8c2f804b83b2a1db4fd350d5690fa858d3b159daf7d7dee159e5c95331b9b14f6089291baeedf5df9915220563e92f420417d6d1efb430a5343fb9e78973e44bf9c22f41d4f36b619bd197efc65e91286c888bb8fb208a7d852c4454bfeb5f8d4ad0a51ad53a9be294fda1ecb749b715650723b6a475bcabc55deb21dbfab7f5dce7403db0100a99ae5df1248e91a75d5a347c3807615dad8f0c443e4bb564b375ef9b8350563011fba8378e34bfe1828a49541d85aed74c462a0f5598354f6393260e9b9e6f8effcdd87cb528ad99072c98a5b460a5dd55d0e0c282ed7d096683b75581409fb0d'
# image = base64_to_PIL(base64_image)
# image.show()


# 获取好友信息
def get_friend(name):
    # 获取自己的用户信息
    # myself = itchat.search_friends()
    # print(myself)
    # 获取特定的用户信息，userName=UserName(好友信息中UserName的值)
    # friend = itchat.search_friends(userName=name)
    # 获取任何一项等于name的用户（备注，微信号，昵称任何一项等于）
    # friend = itchat.search_friends(name=name)
    # 获取备注，微信号，昵称分别等于相应键值的用户
    friends = itchat.search_friends(wechatAccount=name)
    # itchat.search_friends(name=name,wechatAccount=name)
    for friend in friends:
        print(friend)


if __name__ == "__main__":
    # 扫描二维码登录，enableCmdQR=True表示在命令行显示二维码，enableCmdQR=-1表示控制台背景为浅色（默认暗色），enableCmdQR=2表示部分linux系统
    # itchat.auto_login(hotReload=True,enableCmdQR=True)
    # 扫描二维码登录，hotReload=True表示不需要重新扫描
    itchat.auto_login(hotReload=True)
    # newInstance = itchat.new_instance()
    # newInstance.auto_login(hotReload=True,statusStorageDir='newInstance.pkl')
    # sleep(5)
    # get_friend('')
# itchat.send('hello',toUserName="filehelper")
    itchat.run()
#     # print(get_response('今天什么日子呀'))