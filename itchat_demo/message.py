import requests
import time


# 获取每日句子
def getSentence():
    url = 'http://open.iciba.com/dsapi'
    html = requests.get(url).json()
    content = html['content']
    note = html['note']
    print(html)
    print(content)
    print(note)
    voice = requests.get(html['tts'])
    print(voice)
    today = time.strftime("%Y%m%d")
    voice_path = 'voice/' + today + '.mp3'
    with open(voice_path, 'wb') as f:
        f.write(voice.content)
    print(voice_path)
    return content,note,voice_path


# if __name__ == '__main__':
#     getSentence()