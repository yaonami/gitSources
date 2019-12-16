import execjs
import cv2
from PIL import Image
import math
import random


def getJSContent(file):
    with open(file, 'r') as f:
        line = f.readline()
        htmlStr = ''
        while line:
            htmlStr = htmlStr + line
            line = f.readline()
    # print(htmlStr)
    return htmlStr


def getPoissonResult(width, height, radius, margin, file):
    js = getJSContent(file)
    ctx = execjs.compile(js)
    result = ctx.call('poissonDiscSampler', width, height, radius, margin)
    return result


def getClosestEmoji(r, g, b, file):
    js = getJSContent(file)
    ctx = execjs.compile(js)
    # print(ctx)
    result = ctx.call('emoji', r, g, b)
    # print(result)
    return result


def getEmojiColors(file):
    js = getJSContent(file)
    ctx = execjs.compile(js)
    result = ctx.eval('emojiColors')
    return result


def createBGImage(width, height):
    img = Image.new('RGBA', (height, width), (255, 255, 255, 0))
    img.show()
    # img.save()
    return img


if __name__ == '__main__':
    # emojiColors = getEmojiColors('emojiColors.js')
    # print(type(emojiColors))
    # print(contents)
    path = 'emoji_picture/wyf.jpg'
    img = cv2.imread(path)
    # print(img.shape)
    width = str(img.shape[1])
    # width = str(img.shape[1]+400)
    height = str(img.shape[0])
    # height = str(img.shape[0]+400)
    radius = '8'
    margin = '0'
    image = createBGImage(int(width), int(height))
    print(image.size)
    contents = getPoissonResult(width, height, radius, margin, 'poisson-disc-sampler-modify.js')
    for content in contents:
        w = int(content[0])
        # w = int(content[0]-100)
        h = int(content[1])
        # h = int(content[1]-100)
        if w >= img.shape[1] or h >= img.shape[0]:
            red = '0'
            green = '0'
            blue = '0'
        else:
            red = str(img[h, w, 2])
            green = str(img[h, w, 1])
            blue = str(img[h, w, 0])
        res = getClosestEmoji(red, green, blue, 'emoji.js')
        print(res)
        emojiImage = Image.open(res)
        emojiImage = emojiImage.resize((30,30), Image.ANTIALIAS)
        emojiImage = emojiImage.rotate( math.ceil( random.random() * 360 ) * math.pi / 180 )
        # emojiImage.show()
        # print(emojiImage)
        # emojiImage.save()
        # if (not content[0]==0) and (not content[1]==0):
        image.paste(emojiImage,(int(content[0]),int(content[1]),int(content[0]+30),int(content[1]+30)))
        # image.save()
        # image.show()
    image.show()