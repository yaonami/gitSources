import execjs
import cv2


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
    print(ctx)
    result = ctx.call('result', r, g, b)
    return result


def getEmojiColors(file):
    js = getJSContent(file)
    ctx = execjs.compile(js)
    result = ctx.eval('emojiColors')
    return result


if __name__ == '__main__':
    # emojiColors = getEmojiColors('emojiColors.js')
    # print(type(emojiColors))
    # print(contents)
    path = 'wyf.jpg'
    img = cv2.imread(path)
    print(img.shape)
    width = str(img.shape[1]+400)
    height = str(img.shape[0]+400)
    radius = '8'
    margin = '100'
    contents = getPoissonResult(width, height, radius, margin, 'poisson-disc-sampler-modify.js')
    # print(contents)
    for content in contents:
        w = int(content[0]-100)
        h = int(content[1]-100)
        if w >= img.shape[1] or h >= img.shape[0]:
            red = '0'
            green = '0'
            blue = '0'
            # red = 0
            # green = 0
            # blue = 0
        else:
            red = str(img[h, w, 2])
            green = str(img[h, w, 1])
            blue = str(img[h, w, 0])
            # red = img[h, w, 2]
            # green = img[h, w, 1]
            # blue = img[h, w, 0]
            # print(red)
            # color = [red, green, blue]
            # color = str(color)
            # color[0] = red
            # color[1] = green
            # color[2] = blue
        res = getClosestEmoji(red, green, blue, 'emoji.js')
        print(res)
