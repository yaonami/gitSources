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
@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
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
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
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
    itchat.send('@%s@%s' % ('img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
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
@itchat.msg_register(TEXT, isGroupChat=True)
def reply_group(msg):
    print(msg)
    print(msg.isAt)
    print(msg.actualNickName)
    print(msg.text)
    if msg.text:
        itchat.send(msg.text, msg['FromUserName'])


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
    friends = itchat.search_friends(name=name)
    # 获取备注，微信号，昵称分别等于相应键值的用户
    # friends = itchat.search_friends(wechatAccount=name)
    # itchat.search_friends(name=name,wechatAccount=name)
    for friend in friends:
        print(friend)


if __name__ == "__main__":
    # # 扫描二维码登录，enableCmdQR=True表示在命令行显示二维码，enableCmdQR=-1表示控制台背景为浅色（默认暗色），enableCmdQR=2表示部分linux系统
    # itchat.auto_login(hotReload=True,enableCmdQR=True)
    # # 扫描二维码登录，hotReload=True表示不需要重新扫描
    itchat.auto_login(hotReload=True)
    # # newInstance = itchat.new_instance()
    # # newInstance.auto_login(hotReload=True,statusStorageDir='newInstance.pkl')
    # # sleep(5)
    # get_friend('一人一歌一世界')
    # # itchat.send('hello',toUserName="filehelper")
    itchat.run()
    # print(get_response('今天什么日子呀'))
    # String = '/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8f' \
    #          'ExciJCIeJBweHx7/2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eH' \
    #          'h7/wAARCACMAHkDASIAAhEBAxEB/8QAHQAAAAYDAQAAAAAAAAAAAAAAAAECAwUIBAYHCf/EAEYQAAEDAwIDBQUEBQgLAQAAAAECAwQABR' \
    #          'ESIQYxQQcTUWFxCBQigZEyQqGxFSMkUsEzNFNictHh8BYXJUNUY3OCkqLC0v/EABsBAAEFAQEAAAAAAAAAAAAAAAMAAQIEBQYH/8QALxE' \
    #          'AAgIBAwMCBAQHAAAAAAAAAQIAAxEEEiEFMUEiUQYTYYEycbHBI1JikdHw8f/aAAwDAQACEQMRAD8AtxQo8Cj2oshE0KVQpRRNDpmlVrPa' \
    #          'PxpY+BeG3r7fpPdMI+FttG7j6+jaE9T+VIRjjzJq43GDbmwubLbjpVkJCjurHPAHPFatP7UOB4TzqHb/ABiGUguOA5SlR+76+VUj7S+2zi' \
    #          'vjW4vLj6rVGW4SktPqDhT91OoEAADbAxuSTk71qDUqdb2C+p5151x4OLOrKVjqSM7n1zRRWPMEbfaej1o4z4UurLL8HiO0vIf3a0y0BSvL' \
    #          'TnOa2AEEZByMZ28K8srfcUTLp+tDSO8XkFSSo/Wu89hnaxf+Er3H4fmTzKtEk6WGZbpCW1E7d24c6M+Bynly50mrx2jrZnvLqUKwrFdI93' \
    #          'tzcyNqSFbLbUMKbV1SR0IrPoULE0KVScUooVFSiNqLFKKLoYo8UKUULFDFHQpRQlbJJqiftk8Vyrp2hSbTIkrUYLvcMxkqBaZY0pIOobF' \
    #          'bislWPshKR41eS6d17g+l95TLS0FKlpOCnPw5B8ckY868y+16c7ce0O6vuqQrQ6GEaEaAA38AGPHCd/EkmiVDJgrSQs163NPOByQhrvSg' \
    #          'asHkB4msi1xbnd7k0xFjuuqUofA2jO3yrq/s3cMWy/TVC4xxIYZUFqaUNlKz1HXFW3sVks0BCPcbXCjZAHwMJBx9KrX67YxQCW9P04WIH' \
    #          'Jnn5dbFJtl1damwVNN69O4I05qcluuxbCjvUhehYDT5T8QOMpCvQgjNWR7d+DoMyeJS4oLMmHIQSNil1KC42oeYKMfOqtcRT3TbmYqjto' \
    #          'IKeisYIVjxIO9F095u4g9XpBTggy9nsw8RI4q7OWruHB3wCI8gZyoONjSSrzOxz1511bfO436+VU59gG7yBxRxDaPeAGH4iJRYJ+04hWN' \
    #          'Q+St6uOMAYHSpOMGDQ5ETR0dFioyUI0MUeKFKKKxQxR0KUULFDFHQpsxSI4wsieIeGplp97ehqfSO7kNEamnEqCkKGfBQH0rzh7ZOFp' \
    #          'PCvaHcLG+8/J7t0rEh5OkvE5JXjmMnNemiuWcZA3/z41S72txDvfakxc4MdxUGGtq1T7hpy0ZQBWWweqkpIzjrkdKIjbeZFk3cTQ+xbi9' \
    #          'XBkeUpVpbk63EkrVJDShgY21HfNWV4S7Rxf7PLlw7PMTLt7AdeiKA1kdMYyDnpXLexPsztkyDHvdxfaeW6srXGcYQsJKVbbqzvXYezi' \
    #          'PAa424kEFhDbcRhiKopTgKUMkjA8M1kah1dzib+nqausBjORdoHa9drrc4kAWli0Bt3ViUhUhxadOCClIwNia4RLtEua1JmhBUzHYbIW' \
    #          'EnSMg6fkQkjPjV477wZZLrM/SBjgSUr18yBn5VzLjvsxs8KzXW4JdkFCYbiI8JBwgKOSnbO4CiSB4miU6gVkAQdulW4d5yr2PHLhb+3' \
    #          'CxiIhC25qH2H8KyA33ZUr5jAP0q/gFVS9jjh+xWvtC4gYMll+6QIrZYSgghKXAA4Qf3k8j61a6tEtuOZihNnphYoYo6FNHiaGKVSaU' \
    #          'UVQHOjoUooKBHXGaOgPQ/SoxSC4zdlps62YbzkZx9Xd982cLbGCSUnocA79K412+2u18PezPLYhstMpHcuRiU50uLcSdf9ojOT5mu7X' \
    #          'NqK9FWzMIQ2v72rSUkbgg9Mc81Tf2wO0iCvh+F2bWmczcTDcSZkxpwKDgQPgScHGvO5NEUZOJFjgcd4XZJxwlqKzcGzqjymwXWxt3bo2' \
    #          'UPmd6zuE7zcGeObv73xnHscKae9WUKQX19DpBBCSBnfBzXBezm7uWnCXiRFeVlY/cX0X/fXcezqHcZdz94tci1w0rIUuQ8wh1Z9E4z8' \
    #          '81j3gJYZ2GnqLUqzzvlmutql21Btl7buhaQG3H+8ClqI6rAAwo+lcc9qPiYQeB3bU09+2XRxLSQDultJClq8egHzrpNxnw7PZyuVckTH' \
    #          '1fCC02lCnFHoAOZPKqze0O9JVxhalzCP5mpSkA7IJczj6AZ86jpVFlwBlPXA1aV3Am1+yTDkR+KHJMEKblsxw80DyWMDKfQ8vnV1Yrzcm' \
    #          'K1IZ3adQFo9CMiqgex0xeHOI3pirO+qK0yULmLUG2UtkYA3GVKyE4A8DVurS2W4LSMaRjIGMYyc8unOtuwAHic2nbvMuio6FDzJQqT' \
    #          'SzScU4ii8UkqSElROAOZPLHjmse8zE260TbgtOpMWO4+U5xnQkqx5cqorP7UuJ+0pTz98ubrDKV7W+MotsIQd0nA3UeYyon8cVXvvFK7' \
    #          'jzNTpHSn6ncKlbb9TLc8V9r3Z9w0+5Fn8QMvSm9lsREGQpJ8Do2B8ia55ffaYs7ef0DwvcZwBxrkuIYT64Go1XhUVhjS6EJwThWBsP' \
    #          'Cn2mW2pKkKGWnBlP8AGsqzqTn8IxPQ9L8D6OsD5zFjNq469prjdUSTBb4Z4fjxntSVd82t8aD93cgH1qtt3nKuc5T3ucKOFKCu6it6EJ' \
    #          '8QBv8AnXYZ1sZlsuQnkoOndOeah41qcrhVhvV3kdKz0UNjj1FWaOpqVw3eZXUvgl1t36c5X2kRbnf2dKAGXG9P2XNiKzbZeJ9rBTbZ7z' \
    #          'Kc7NkpWn5bgisRVlmxnSYQW5g7IUM/jUva4twCWpL9u71KhkZdCQD0Bz12oVjr+LvL2n0juBU64I+k2C1XHiFSkXSZeJDb4TpbwAdA8R4' \
    #          'HzxULxCXrk8iIl2RLuDy8qW58RI671L/pFCE6JsNxIIGUqaAB9CpQFOsyYjTmY0SSHV4yW3m0Z9VAnH1qktrK26b93TtPdV8pcAeeJun' \
    #          'ZNxNxL2e3Bj3Ev3C1urBmQpScpJxjLSiPgI+YNWp4K7Q+HuJ0JbZddhTSMqjygEKJ/qqzpV8j8qpa2lbigpcVsn91b7rv45CayGFXT7' \
    #          'MV6NHwrIS2hSyPMZPOiV9QtU+rtKWt+DtDqq/4YKt4I/cS/PQHlncZo6pzwn2h9oPDLza41/XPipOFxJzepKk+A3yn1BqxnAHadw3x' \
    #          'UhmL336Puy0grgvkg6hz0KOyx6H5VqafXVXcdjOA6t8Mazpw3Ebl9x+/tN5oqMb0MVeAnOhd3acp9pXtBhcH8ESLcVNqn3aO4ykH/ds' \
    #          'kaXHCPQ4A6k+RqkcYoiOt8QRGltxnFd08yDsG+Sfnjf5VPdv/ABvK414zlXFzU22tSQyznPdNJz3afXmo+ZrH927ng5xvTsljUR+Oax9' \
    #          'TduwfBnpXQum/IVq8epQCT/V/gSeYcQ62pCld4kjcgbEcwR6jem0lZCoq1YdbPwK8+hrAtT7bfdx8kBTSHGQdipBG4/7VbehqQeQHX' \
    #          'G3MrQpGxUMYI8KyHXa076m4WVhgYv3hDrkZAV3cgZ2PQDmPrTrqNjkDB6eHpWCiOn9KmaVHKm9C0n8xUocEDJx50z8doWti2czFdbQh' \
    #          'la2kgqAxjrucfxrJW0yhenQNGAnHpTSkaVE9KfyHilaF7EHIKcFJqB5EJwDHUIbDeED4T06fSibaabOW2m0HxSgCiZ2BGc07io5zJY' \
    #          'B5hhSuWT9acDi841Gm6MU0fMe16hhWCKx7jJeYDQZfcbWVpSFJUcp36HpSgr7XkKwpqivuTnfvEmknDZg7OVIlu+w/ipXFPBLTsl3XP' \
    #          'hq93kk81bZSr5pI+hrecmqv+zRxAbXx5+inFYj3VvusE7B1OVI/+hVnO8FdToL/AJlQJnh/xPoh07qDKMBW9Q+/j7GeX60mXLQtz7ci' \
    #          'QEjyANbre1JYsEo/8rQPUkAfnWrWpoLvUFgj+TBcV9K2LiNfeNwYQ294kIB9E7/wrKv5ZVE9I0QNdVr+Tx/v3Mj+MHH4K7ZKZOg' \
    #          'NNlKfAbbg/wCelP2G4yZLriHkpSUpSpIT1B86l7/Fal2d9pxOyRrSeqTWscHhbVxfjr3UhvAHjgg1FSr1n6Q9tdmn1gAPpb9QJtaA' \
    #          'dKnEr1Y2JP3ayw7+qBGkjxNY5Wy1ISCoDvB8O/OlojxgCtDQznJB3APjiqZm6pAJEeyXCMHb7woyvcJHyphb6QdKlhvzzTDjyUuFp' \
    #          'j9a8R9jP2fMnpTbSRmOXHaSUdwq1b9cU+FVgxx3aQAcnqfPrTzbydWFbVArCBuJlA5oasU0HAfCgVjB3FNiPuhuuaW1+OKYdOpLP/U' \
    #          'FNPuDvy3kct/L/OaC1/zZHi7/AAqeJDfjBkhYri7ar1EuMc4divoeR0yUnOPzqz/+ujhH+n/9aqevZQOcb053yv3jR6dS9Qwsw+rdB0' \
    #          '3U2Rru6jE0jhdId4gkOHcttBI+ZqSmOd/xhDZG6Y7KlqHgSP8AEVj8CNakS5J5re5+Q2pvh90S+Mbi9z0o0j6/4VYfl2+glfTnFVQ/n' \
    #          'bP2H/JtFwP+z5OP3DXP1yHI1075helYSD610NSdaVIUPhUCD6Vrtw4WbdS45HccL+n4M8vIULTWKvDS91TS23KrV+JF+8XN4+9KZRLZW' \
    #          'cFtKeRHlzBqZs90StSS08paeSm3DhaPLPUetRNvU/blKkLQpyOCESkJ5pBOyvkRUtOiqf0So2hUtA1JUnYSEHf6kUWzaeMSppzYpJBOR3' \
    #          'ElH4LE1/v1PPDbHdoXoT/fWSzEZgoxGb0NLO4Cirf1O5+da9GujQcSlp7WtRwhnB1pPgRWwQXFBK40o4d+8PXliqtilRibOmtSz1Y5i1' \
    #          'EpcScEgHfFGVNr3SMeINJwpsltWdSfxFLCW3AFoI3G3mKFLEQlJG6SQPWgtSkAq17DnkUFrQ2ficTnoM8zUXelTUNYcWnuiOgxiiIobv' \
    #          'A22/LXMFsf94mylDHwuYBHXlUk5/LRf7R/I1rnCHeHv3lDCHnFafRKgKn3lftMUf1j+RqVibWxK+ltNtIc+THnTypGaDhyTvTfzoIl09' \
    #          '5DcLo9z4eLh+0lKl58agOD5Cm7zMlKOe9Vpz+NTEeY45wq4nShOlITlI3IzULw6kCE/j+lVv6VogcMT5nKWOBbQidlyf7CdBYWFJyOt' \
    #          'Otg6jpODz+davZ5khaUoUvIBwNqn4Dy3o+teNSVkDFUrKyOZ0tGoFgBkLMWYF9+IAsvjcdMHb86bjJVbrkbU9vDkEuW9w/cV95vP5Vn' \
    #          'cWtI/RjT330uYB9RSXI7dx4aU3JyShvvULScKQpI2INFRsqPY8Sjqaijbk7rk/mPIP5/rM5DLEhJUpCA/jAd0gKB8z1FEkB4YcBRI' \
    #          'ZOPMVhWaQ6/bochwguOshSzjmckZ/CsyeShbD6dlq+BX9YedDddp2y3SwesOoxmZIX37eM/rEcjUddYqn4xLbimlpOQoHGD5+VPyFqb' \
    #          'caWnmokH5U+4SMLHPnUVyphCBYMGa8mw3E6VqfQFHl8ZJFYHEUt+C0iGt4yJJ2aQDnc9TU/Glvsz5MZtWGm0AoT4ZIz+daZbHlp44b' \
    #          '1EOa5DjR7z4sAbjHnV6gFySfEwOqXChErTI3nbN6gR2YlviMtD+Sa0qJ5k5yT9aC1ftUXfksj8KShR75aegO1NTVFCmFp596Kq47mb' \
    #          'CqECqPHEy3HU6jg0nvRTMsAFRA5E/mP763b/AEKtn/Fzv/JH/wCKeuksMiV9b1NNMRvB59p//9k='
    # img = base64_to_PIL(String)
    # img.show()
