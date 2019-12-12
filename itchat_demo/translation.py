from googletrans import Translator
from handleJS import Py4Js
import urllib.parse
import requests
import json
import time


translator = Translator(service_urls=['translate.google.cn'])


LANGUAGES_EN = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-CN': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}


LANGUAGES_ZH_CN = {
    'af': '南非语',
    'sq': '阿尔巴尼亚语',
    'am': '阿姆哈拉语',
    'ar': '阿拉伯语',
    'hy': '亚美尼亚语',
    'az': '阿塞拜疆语',
    'eu': '巴斯克语',
    'be': '白俄罗斯语',
    'bn': '孟加拉语',
    'bs': '波斯尼亚语',
    'bg': '保加利亚语',
    'ca': '加泰罗尼亚语',
    'ceb': '宿务语',
    'ny': '奇切瓦语',
    'zh-CN': '中文简体',
    'zh-tw': '中文繁体',
    'co': '科西嘉语',
    'hr': '克罗地亚语',
    'cs': '捷克语',
    'da': '丹麦语',
    'nl': '荷兰语',
    'en': '英语',
    'eo': '世界语',
    'et': '爱沙尼亚语',
    'tl': '菲律宾语',
    'fi': '芬兰语',
    'fr': '法语',
    'fy': '弗里斯兰语',
    'gl': '加利西亚语',
    'ka': '乔治亚风语',
    'de': '德语',
    'el': '希腊语',
    'gu': '古吉拉特语',
    'ht': '海地克里奥尔语',
    'ha': '哈萨语',
    'haw': '夏威夷语',
    'iw': '希伯来语',
    'hi': '印地语',
    'hmn': '苗语',
    'hu': '匈牙利语',
    'is': '冰岛语',
    'ig': '伊博语',
    'id': '印度尼西亚语',
    'ga': '爱尔兰语',
    'it': '意大利语',
    'ja': '日语',
    'jw': '爪哇语',
    'kn': '卡纳达语',
    'kk': '哈萨克语',
    'km': '高棉语',
    'ko': '韩语',
    'ku': '库尔曼吉语',
    'ky': '吉尔吉斯斯坦语',
    'lo': '老挝语',
    'la': '拉丁语',
    'lv': '拉脱维亚语',
    'lt': '立陶宛语',
    'lb': '卢森堡语',
    'mk': '马其顿语',
    'mg': '马尔加什语',
    'ms': '马来语',
    'ml': '马拉雅拉姆语',
    'mt': '马耳他语',
    'mi': '毛利语',
    'mr': '马拉地语',
    'mn': '蒙语',
    'my': '缅甸语',
    'ne': '尼泊尔语',
    'no': '挪威语',
    'ps': '普什图语',
    'fa': '波斯语',
    'pl': '波兰语',
    'pt': '葡萄牙语',
    'pa': '旁遮普语',
    'ro': '罗马尼亚语',
    'ru': '俄语',
    'sm': '萨摩亚语',
    'gd': '苏格兰盖尔语',
    'sr': '塞尔维亚语',
    'st': '塞索托语',
    'sn': '绍纳语',
    'sd': '信德语',
    'si': '辛哈拉语',
    'sk': '斯洛伐克语',
    'sl': '斯洛文尼亚语',
    'so': '索马里语',
    'es': '西班牙语',
    'su': '巽他语',
    'sw': '斯瓦希里语',
    'sv': '瑞典语',
    'tg': '塔吉克语',
    'ta': '泰米尔语',
    'te': '泰卢固语',
    'th': '泰语',
    'tr': '土耳其语',
    'uk': '乌克兰语',
    'ur': '乌尔都语',
    'uz': '乌兹别克语',
    'vi': '越南语',
    'cy': '威尔士语',
    'xh': '科萨语',
    'yi': '依地语',
    'yo': '约鲁巴语',
    'zu': '祖鲁语',
    'fil': '菲律宾语',
    'he': '希伯来语'
}


LANGUAGES_ZH_CN_S = dict(map(reversed, LANGUAGES_ZH_CN.items()))


translationUrls = {
    '中文转英语':'https://translate.google.cn/translate_a/single?client=webapp&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=2&ssel=0&tsel=0&kc=1&',
    '英语转中文':'https://translate.google.cn/translate_a/single?client=webapp&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ssel=3&tsel=6&kc=0&',
    '中文转日语':'https://translate.google.cn/translate_a/single?client=webapp&sl=zh-CN&tl=ja&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ssel=3&tsel=3&kc=0&',
    '日语转中文':'https://translate.google.cn/translate_a/single?client=webapp&sl=ja&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ssel=4&tsel=3&kc=0&'
}


pronunciationUrls = {
    '中文':'https://translate.google.cn/translate_tts?ie=UTF-8&tl=zh-CN&client=webapp&',
    '英语':'https://translate.google.cn/translate_tts?ie=UTF-8&tl=en&client=webapp&',
    '日语':'https://translate.google.cn/translate_tts?ie=UTF-8&tl=ja&client=webapp&'
}


URL_LIST_DICT = {
    'translationUrl':translationUrls,
    'pronunciationUrl':pronunciationUrls
}


# 检测单一语言
def detect_language(text):
    r = translator.detect(text)
    res = LANGUAGES_ZH_CN[r.lang]
    return res


# 检测输入的语言（多语言）
def detect_languages(text):
    results = []
    for t in text:
        r = translator.detect(t)
        print(r)
        res = LANGUAGES_ZH_CN[r.lang]
        results.append(res)
    return results


# 翻译文本为指定语言
def translateLanguage(text,case):
    dest = LANGUAGES_ZH_CN_S[case]
    r = translator.translate(text,dest=dest)
    print(r)
    res = r.text
    return res


# 生成谷歌翻译的URL
def buildUrl(text,srcL):
    js = Py4Js()
    tk = js.getTk(text)
    q = urllib.parse.quote(text)
    baseUrls = []
    if srcL=='中文简体':
        # 中文翻译成英文
        baseUrl1 = 'https://translate.google.cn/translate_a/single?client=webapp&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=2&ssel=0&tsel=0&kc=1&'
        baseUrl1 += 'tk=' + str(tk) + '&'
        baseUrl1 += 'q=' + q
        baseUrl1_dict = {'url':baseUrl1,'language':'英语'}
        baseUrls.append(baseUrl1_dict)
        # 中文翻译成日语
        baseUrl2 = 'https://translate.google.cn/translate_a/single?client=webapp&sl=zh-CN&tl=ja&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ssel=3&tsel=3&kc=0&'
        baseUrl2 += 'tk=' + str(tk) + '&'
        baseUrl2 += 'q=' + q
        baseUrl2_dict = {'url': baseUrl2, 'language': '日语'}
        baseUrls.append(baseUrl2_dict)
        # 中文翻译成德语
        baseUrl3 = 'https://translate.google.cn/translate_a/single?client=webapp&sl=zh-CN&tl=de&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=1&ssel=3&tsel=4&kc=1&'
        baseUrl3 += 'tk=' + str(tk) + '&'
        baseUrl3 += 'q=' + q
        baseUrl3_dict = {'url': baseUrl3, 'language': '德语'}
        baseUrls.append(baseUrl3_dict)
        # 中文翻译成法语
        baseUrl4 = 'https://translate.google.cn/translate_a/single?client=webapp&sl=zh-CN&tl=fr&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=1&ssel=6&tsel=4&kc=1&'
        baseUrl4 += 'tk=' + str(tk) + '&'
        baseUrl4 += 'q=' + q
        baseUrl4_dict = {'url': baseUrl4, 'language': '法语'}
        baseUrls.append(baseUrl4_dict)
        # 中文翻译成韩语
        baseUrl5 = 'https://translate.google.cn/translate_a/single?client=webapp&sl=zh-CN&tl=ko&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&swap=1&ssel=5&tsel=5&kc=1&'
        baseUrl5 += 'tk=' + str(tk) + '&'
        baseUrl5 += 'q=' + q
        baseUrl5_dict = {'url': baseUrl5, 'language': '韩语'}
        baseUrls.append(baseUrl5_dict)
    elif srcL=='英语':
        # 英文翻译成中文
        baseUrl = 'https://translate.google.cn/translate_a/single?client=webapp&sl=en&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ssel=3&tsel=6&kc=0&'
        baseUrl += 'tk=' + str(tk) + '&'
        baseUrl += 'q=' + q
        baseUrl_dict = {'url': baseUrl, 'language': '中文简体'}
        baseUrls.append(baseUrl_dict)
    elif srcL=='日语':
        # 日语翻译成中文
        baseUrl = 'https://translate.google.cn/translate_a/single?client=webapp&sl=ja&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ssel=4&tsel=3&kc=0&'
        baseUrl += 'tk=' + str(tk) + '&'
        baseUrl += 'q=' + q
        baseUrl_dict = {'url': baseUrl, 'language': '中文简体'}
        baseUrls.append(baseUrl_dict)
    elif srcL=='德语':
        # 德语翻译成中文
        baseUrl = 'https://translate.google.cn/translate_a/single?client=webapp&sl=de&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&pc=1&otf=1&ssel=3&tsel=6&kc=1&'
        baseUrl += 'tk=' + str(tk) + '&'
        baseUrl += 'q=' + q
        baseUrl_dict = {'url': baseUrl, 'language': '中文简体'}
        baseUrls.append(baseUrl_dict)
    elif srcL=='法语':
        # 法语翻译成中文
        baseUrl = 'https://translate.google.cn/translate_a/single?client=webapp&sl=fr&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&swap=1&ssel=5&tsel=5&kc=1&'
        baseUrl += 'tk=' + str(tk) + '&'
        baseUrl += 'q=' + q
        baseUrl_dict = {'url': baseUrl, 'language': '中文简体'}
        baseUrls.append(baseUrl_dict)
    elif srcL=='韩语':
        # 韩语翻译成中文
        baseUrl = 'https://translate.google.cn/translate_a/single?client=webapp&sl=ko&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&' \
                  'dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ssel=5&tsel=5&kc=1&'
        baseUrl += 'tk=' + str(tk) + '&'
        baseUrl += 'q=' + q
        baseUrl_dict = {'url': baseUrl, 'language': '中文简体'}
        baseUrls.append(baseUrl_dict)
    return baseUrls


# 生成获取读音的URL
def buildMp3Url(text,language):
    js = Py4Js()
    tk = js.getTk(text)
    q = urllib.parse.quote(text)
    if language=='英语':
        # 获取英文发音
        baseMp3Url = 'https://translate.google.cn/translate_tts?ie=UTF-8&q='+q+'&tl=en&tk='+tk+'&client=webapp&ttsspeed=0.24'
    elif language=='中文简体':
        # 获取中文发音
        baseMp3Url = 'https://translate.google.cn/translate_tts?ie=UTF-8&q='+q+'&tl=zh-CN&tk='+tk+'&client=webapp'
    elif language=='德语':
        # 获取德语发音
        baseMp3Url = 'https://translate.google.cn/translate_tts?ie=UTF-8&q='+q+'&tl=de&tk='+tk+'&client=webapp'
    elif language=='日语':
        # 获取日语发音
        baseMp3Url = 'https://translate.google.cn/translate_tts?ie=UTF-8&q='+q+'&tl=ja&tk='+tk+'&client=webapp'
    elif language=='法语':
        # 获取法语发音
        baseMp3Url = 'https://translate.google.cn/translate_tts?ie=UTF-8&q='+q+'&tl=fr&tk='+tk+'&client=webapp'
    elif language=='韩语':
        # 获取韩语发音
        baseMp3Url = 'https://translate.google.cn/translate_tts?ie=UTF-8&q='+q+'&tl=ko&tk='+tk+'&client=webapp'
    return baseMp3Url


# 翻译文本
def translationText(text,srcL):
    # hearder = {
    #     'cookie':'NID=192=FA_DDDxD8ClpS0bp7K1keVr96sAp9G79Pa-thBEen5hlyJy3ZgaOJ5ffIpwqGHDvqtcZqrRtai9mUFlPAvPcK6XdskQb'
    #              'K9_60F-qXClHt9w-gSAz0C0Uw8tlsX6KyPpb6j27lwPXi66Pr2WDsspMV4rq9vF6o8ndzKntxNRtoho',
    #     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome'
    #                  '/78.0.3904.108 Safari/537.36'
    # }
    baseUrls = buildUrl(text,srcL)
    # print(baseUrls)
    results = []
    if len(baseUrls)==0:
        results = []
    else:
        for baseUrl in baseUrls:
            url = baseUrl['url']
            language = baseUrl['language']
            try:
                r = requests.get(url)
                # print(r)
                res = json.loads(r.content.decode('utf-8'))
                # print(res)
                result = res[0][0][0]
                # print(result)
                Mp3Url = buildMp3Url(result,language)
                try:
                    rl = requests.get(Mp3Url)
                    # print(rl)
                    voicePath = language+'-'+str(int(time.time()))+'.mp3'
                    with open(voicePath,'wb') as f:
                        f.write(rl.content)
                    # print(rl.content)
                    trans_res = {'content':result,'voice':voicePath,'language':language}
                    results.append(trans_res)
                except Exception as e:
                    print(Mp3Url)
                    print('获取发音失败')
                    print(e)
            except Exception as e:
                print(url)
                print('翻译失败')
                print(e)
    return results


# 根据url获取翻译后的内容
def getContent(url):
    content = ''
    if url=='':
        return content
    else:
        try:
            r = requests.get(url)
            res = json.loads(r.content.decode('utf-8'))
            content = res[0][0][0]
        except Exception as e:
            print(e)
        finally:
            return content


# 根据url获取发音
def getPronunciation(url):
    voicePath = ''
    if url=='':
        return voicePath
    else:
        try:
            r = requests.get(url)
            res = r.content
            if not res=='':
                voicePath = 'voice/' + str(int(time.time())) + '.mp3'
                with open(voicePath, 'wb') as f:
                    f.write(res)
        except Exception as e:
            print(e)
        finally:
            return voicePath


# 中英互译
def translationZE(text):
    js = Py4Js()
    tk1 = js.getTk(text)
    q1 = urllib.parse.quote(text)
    content = ''
    voicePath = ''
    res = detect_language(text)
    if res=='中文简体' or res=='中文繁体':
        baseUrl = URL_LIST_DICT['translationUrl']['中文转英语']
        url = baseUrl + 'q=' + q1 + '&tk=' + str(tk1)
        content = getContent(url)
        tk2 = js.getTk(content)
        q2 = urllib.parse.quote(content)
        baseMp3Url = URL_LIST_DICT['pronunciationUrl']['英语']
        mp3Url = baseMp3Url + 'q=' + q2 + '&tk=' +str(tk2)
        voicePath = getPronunciation(mp3Url)
    elif res=='英语':
        baseUrl = URL_LIST_DICT['translationUrl']['英语转中文']
        url = baseUrl + 'q=' + q1 + '&tk=' + str(tk1)
        content = getContent(url)
        tk2 = js.getTk(content)
        q2 = urllib.parse.quote(content)
        baseMp3Url = URL_LIST_DICT['pronunciationUrl']['中文']
        mp3Url = baseMp3Url + 'q=' + q2 + '&tk=' + str(tk2)
        voicePath = getPronunciation(mp3Url)
    return content,voicePath


# 中日互译
def translationZJ(text):
    js = Py4Js()
    tk1 = js.getTk(text)
    q1 = urllib.parse.quote(text)
    content = ''
    voicePath = ''
    res = detect_language(text)
    if res=='中文简体' or res=='中文繁体':
        baseUrl = URL_LIST_DICT['translationUrl']['中文转日语']
        url = baseUrl + 'q=' + q1 + '&tk=' + str(tk1)
        content = getContent(url)
        tk2 = js.getTk(content)
        q2 = urllib.parse.quote(content)
        baseMp3Url = URL_LIST_DICT['pronunciationUrl']['日语']
        mp3Url = baseMp3Url + 'q=' + q2 + '&tk=' +str(tk2)
        voicePath = getPronunciation(mp3Url)
    elif res=='日语':
        baseUrl = URL_LIST_DICT['translationUrl']['日语转中文']
        url = baseUrl + 'q=' + q1 + '&tk=' + str(tk1)
        content = getContent(url)
        tk2 = js.getTk(content)
        q2 = urllib.parse.quote(content)
        baseMp3Url = URL_LIST_DICT['pronunciationUrl']['中文']
        mp3Url = baseMp3Url + 'q=' + q2 + '&tk=' + str(tk2)
        voicePath = getPronunciation(mp3Url)
    return content,voicePath


if __name__ == '__main__':
#     # tx = '做个小测试，接下来的几天可能会不定时收到来自本账号的消息，如果觉得被打扰，请微信回复本账号。'
#     # tx = '你好吗'
# #     # tx = 'Happiness is a way station between too much and too little.'
#     tx = '今日はいい日です'
#     s = translationText(tx,'日语')
#     print(s)
#     print(p)
#     # c = ['我是谁','嗨','hi','hello','νλκμκλ','нмшмн','ぬねのねぬ']
#     # result = detect_languages(c)
#     # print(result)
    text = 'Companionship is the most confession Keeping together is the warmest promise Waiting is the greenest romance' \
           ' Smile is the best memory Tolerance is the most true love'
    tx = '陪伴是最长情的告白 相守是最温暖的承诺 等待是最青涩的恋情 微笑是最美好的回忆 宽容是最真是的爱情'
    t = '輸入你要查詢的簡體字，點擊轉換按鈕，就能轉換為繁體字。'
    re = detect_language(t)
    print(re)
    # t = 'think you know everything so do not say the pain.'
#     d = '中文简体'
#     # d = LANGUAGES_ZH_CN_S[x]
#     # print(d)
#     rr = translateLanguage(t,d)
#     print(rr)
