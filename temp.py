# # import urllib2
# #
# #
# # def abc(url):
# #     u = urllib2.urlopen(url).read()
# #     print len(u)
# #
# #
# # abc()
# import json
#
# import requests
# from instagram.client import InstagramAPI
#
# client_id = '3d011df4fd924065bab4bc8a1c126e5e'
# client_secret = '91ce37323843407a8922766491fe69d3'
# redirect_uri = 'http://localhost/'
#
# api = InstagramAPI(client_secret=client_secret, client_id=client_id, redirect_uri=redirect_uri)
#
# api.get_authorize_login_url(scope='')
#
# code = raw_input()
# # access_token, user_info = api.exchange_code_for_access_token(code)
#
# url = u'https://api.instagram.com/oauth/access_token'
# data = {
#     u'client_id': client_id,
#     u'client_secret': client_secret,
#     u'code': code,
#     u'grant_type': u'authorization_code',
#     u'redirect_uri': redirect_uri
# }
#
# response = requests.post(url, data=data)
#
# account_data = json.loads(response.content)
# aceess_token = '233924208.3d011df.7b19c3ea531749a79b7bd1e81d7ec12a'
#
# recent_media, next_ = api.user_recent_media(user_id="233924208", count=50)
#
# for media in recent_media:
#     break
import cookielib
import datetime
import re
import urllib2
import uuid

from bs4 import BeautifulSoup


def openurl(url):
    try:
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders.append(('User-Agent',
                                  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'))
        opener.addheaders.append(('Accept-Encoding', 'utf-8'))
        html = opener.open(url).read().decode('utf-8', 'ignore')
        return html
    except Exception, e:
        req = urllib2.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'})
        req.add_header('Accept-Encoding', 'utf-8')
        html = urllib2.urlopen(req).read().decode('utf-8', 'ignore')
        return html


def instagram_image_url(url):
    html = openurl(url)
    soup = BeautifulSoup(html)
    a = soup.findAll('meta')
    imgurl = ''
    name = ''
    send_json = {}
    for item in a:
        try:
            if item['property'] == 'og:image':
                imgurl = item['content']
            elif item['property'] == 'og:title':
                name = item['content']

        except Exception, e:
            print e

    if name == '':
        imgName = "Instagram Image"
    else:
        imgName = name.split(' ')[0]
        imgName = imgName + '\'s image'
    print imgName

    if imgurl:
        send_json['Path'] = imgurl
        send_json['Name'] = imgName
        send_json['Url'] = imgurl
        send_json['FileModified'] = datetime.datetime.now()
        send_json['FileAccessed'] = datetime.datetime.now()
        send_json['FileCreated'] = datetime.datetime.now()
        send_json['Extension'] = 'jpg'
    else:
        send_json['Error'] = 'Instagram Exception:Image not found'
    return send_json


def instagram_validator(url):
    print "Inside Instagram_url_validation: ", url
    Instagram_regex = r'(?:(?:http|https):\/\/)?(?:www.)?(?:instagram.com|instagr.am)\/([A-Za-z0-9-_]+)'
    if re.match(Instagram_regex, url):
        print "matched"
        return True
    else:
        print "unmatched"
        return False


def download_img(send_json):
    path = '/Users/mayankshekhar/Downloads/inst_img'
    if send_json.get('Url'):
        with open(path + '/' + send_json['Name'] + '_' + str(uuid.uuid4())[:5] + '.jpg', 'w') as f:
            cj = cookielib.CookieJar()
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            opener.addheaders.append(('User-Agent',
                                      'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'))
            opener.addheaders.append(('Accept-Encoding', 'utf-8'))
            html = opener.open(send_json['Url']).read()
            f.write(html)
            print 'done ', path + '/' + send_json['Name'] + '_' + str(uuid.uuid4())[:5] + '.jpg'


urls = ['https://www.instagram.com/p/Bg7D9DGh707/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/Bef86KxhMvb/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BdmnNJLh2qE/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/Bd49x0ZBmBt/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/Bd-AzrfB3P1/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BeSDVRhBL4w/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BeVOeF5B4to/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BeVbkfDAqqP/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BeakZQeh7q1/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/Bdk6W3FBVle/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BXLs1h0ADym/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BW-9sEJg4VM/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BXNDdkkAg0t/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BXQ7VX6Aa9D/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BcNalkBhzny/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BcSgjdgBd-W/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BcaQ0cmhVb2/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BdS0Vqmh9KM/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BdXN0QphnEo/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BdaP2NSBZ27/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BdfhDZDBhte/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/zsBK-hwaUt/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/8if2aSwaRX/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/8ntbFAQaXr/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BBndweMQaUb/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BEW4jFgQaQS/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BGBvjvawabS/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BLjIkqYDmWL/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BN2ZnMXDz47/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BODFF9ADcCI/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BVu6wa4gcZc/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BWDsF1aANpP/?taken-by=thekreativeadda',
        'https://www.instagram.com/p/BV9TO6Tg4Gk/?taken-by=thekreativeadda']
import time
import random

for url in urls:
    send_json = instagram_image_url(url)
    download_img(send_json)
    sleep_time = random.randint(2, 7)
    print 'loop done ', url, sleep_time
    time.sleep(sleep_time)
