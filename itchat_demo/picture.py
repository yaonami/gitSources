import requests


def getPicture():
    url = 'https://qq.yh31.com/sx/zw/'
    html = requests.get(url).content
    print(html)


if __name__ == '__main__':
    getPicture()