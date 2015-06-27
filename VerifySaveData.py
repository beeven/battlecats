#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: Beeven Yip
# Created on 2015-6-26

import io
import os.path
import hashlib
import xml.etree.ElementTree as ET

def verifyIOS():
    with open("SAVE_DATA","rb") as f:
        data = f.read()
    print "------ iOS SAVE_DATA ------"
    verify(data)

def verifyAndroid():
    tree = ET.parse("save.xml")
    root = tree.getroot()
    node = root.find("./string[@name='SAVE_DATA']")
    data = base64.b64decode(node.text)
    print "------ Android SAVE_DATA ------"
    verify(data)

def verify(data):
    signature = data[-32:]
    hashed = hashlib.md5("battlecats"+data[:-32]).hexdigest()
    print "Signature: ", signature
    print "Computed:  ", hashed

if __name__ == "__main__":
    if os.path.exists("SAVE_DATA"):
        verifyIOS()
    if os.path.exists("save.xml"):
        verifyAndroid()
