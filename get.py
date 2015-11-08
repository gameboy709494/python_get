#!/usr/bin/env python3


import urllib.request
from bs4 import BeautifulSoup


request = urllib.request.urlopen("http://www.ishadowsocks.com")
soup = BeautifulSoup(request.read(), "lxml")


class SSServer:
    address = "null"
    port    = 0
    password= "null"
    method  = "null"
    def __init__(self):
        pass
    def __init__(self, address, port, password, method):
        self.address    = address
        self.port       = port
        self.password   = password
        self.method     = method


server_list = []

for section in soup.find_all("section"):
    if section.get("id") != "free":
        # not the "free" section we wanted
        continue

    # got it
    for account in section.find_all(class_="col-lg-4 text-center"):
        # walk through all accounts
        #print("-------------")
        address = "null"
        port    = 0
        password= "null"
        method  = "null"
        is_got = 0

        for field in account.find_all("h4"):
            #print(field)
            if is_got == 4:
                server_list.append( SSServer( address, port, password, method ) )
                break

            result = field.string.split(':')

            if is_got == 0:
                address = result[1]
            if is_got == 1:
                port = result[1]
            if is_got == 2:
                password = result[1]
            if is_got == 3:
                method = result[1]

            is_got = is_got + 1
        pass
    pass

for i in server_list:
    print( i.address, i.port, i.password, i.method )


