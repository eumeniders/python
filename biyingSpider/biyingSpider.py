# -*- coding:utf-8 -*-
import os
import urllib
import requests
import re
import time
from apscheduler.schedulers.blocking import BlockingScheduler

def my_job():
    url = 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1361089515117&FORM=HYLH1'
    local = time.strftime("%Y.%m.%d")
    con = urllib.urlopen(url).read().decode('utf-8')
    reg = re.compile('"url":"(.*?)","urlbase"', re.S)
    text = re.findall(reg, con)  
    imgurl = 'http://cn.bing.com' + text[0]
    print imgurl
    read = requests.get(imgurl)
    f = open('%s.jpg' % local, 'wb')
    f.write(read.content)
    f.close()
    uri = 'file:///home/eumeniders/Downloads/Python-master/必应爬虫/%s.jpg'% local
    print uri
    cmd = "gsettings set org.gnome.desktop.background picture-uri %s"%uri
    print cmd
    os.system(cmd)

sched = BlockingScheduler()
sched.add_job(my_job, 'interval', days=1)
sched.start()
