#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Author: Beeven Yip
# Created on 2015-6-26

import hashlib
import base64
import argparse
import os.path
import io
import struct
import xml.etree.ElementTree as ET

class Modifier(object):

    def __init__(self, byte_order, data):
        """ byte_order: '>' big_endian for Android
                        '<' little_endian for iOS
        """
        self.__data = bytearray(data)
        self.__byte_order = byte_order

        self.__known_properties = {
            "cat_food": ("L",7),
            "xp": ("L",75),
            "rare_ticket": ("L",8368),
            "ticket": ("L",8364),
            "id": ("10s", 104153)
        }


    def __getattr__(self, name):
        if self.__known_properties.has_key(name):
            v = self.__known_properties[name]
            return struct.unpack_from(self.__byte_order+v[0],self.__data,v[1])[0]
        else:
            raise AttributeError("name")

    def __setattr__(self, name, value):
        if self.__dict__.has_key("__known_properties") and self.__dict__["__known_properties"].has_key(name):
            v = self.__dict__["__known_properties"][name]
            struct.pack_into(self.__byte_order+v[0], self.__data, v[1], value)
        else:
            super(Modifier,self).__setattr__(name, value)


    @property
    def signature(self):
        return self.__data[-32:]

    @signature.setter
    def signature(self, value):
        self.__data = value

    @property
    def computed_hash(self):
        return hashlib.md5("battlecats"+self.__data[:-32]).hexdigest()

    @property
    def known_properties(self):
        return self.__known_properties.keys()

    def save_to_file(self, filename):
        self.signature = self.computed_hash
        pass



class iOS(Modifier):
    def __init__(self, filename=None):
        if filename is None:
            filename = "SAVE_DATA"
        with open(filename, "rb") as f:
            data = bytearray(f.read())
        Modifier.__init__(self, "<", data)

    def save_to_file(self, filename):
        Modifier.save_to_file(self, filename)
        with open(filename, "wb") as f:
            f.write(self.__data)

class Android(Modifier):
    def __init__(self, filename=None):
        if filename is None:
            filename = "save.xml"
        self.__xmltree = ET.parse(filename)
        data = base64.b64decode(self.__xmltree.getroot().find("./string[@name='SAVE_DATA']").text)
        Modifier.__init__(self, ">",data)

    def save_to_file(self, filename):
        Modifier.save_to_file(self, filename)
        node = self.__xmltree.getroot().find("./string[@name='SAVE_DATA']")
        node.text = base64.b64encode(self.__data)
        self.__xmltree.write(filename)
