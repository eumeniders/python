#!/usr/bin/env python
# coding=utf-8
import urllib
import urllib2
import socket

STUID = ''
STUPASS = ''

def getv6ip():
    if socket.has_ipv6:
        addrinfos = socket.getaddrinfo(socket.gethostname(), 80, 0, 0, socket.IPPROTO_TCP)
        for addrinfo in addrinfos:
            if addrinfo[4][0].startswith('2001'):
                return addrinfo[4][0]


url = 'http://202.204.48.82/'


def main():
    getv6ip()
    data = {'g××××××××': STUID, '××××××××': STUPASS, '0MKKey': '123456789', 'v6ip': getv6ip()}
    request = urllib2.Request(url, urllib.urlencode(data))
    response = urllib2.urlopen(request)
    print response.getcode()

if __name__ == '__main__':
    main()
