import requests


if __name__ == '__main__':
    # f = open(path, 'rb')
    url = 'http://ericandrewlewis.github.io/emoji-mosaic/?ref=producthunt'
    r = requests.get(url)
    print(r)
    res = r.content
    print(res)
