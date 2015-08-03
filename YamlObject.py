#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

__author__ = 'Marco Bartel'

import yaml

class YamlObject(object):

    @classmethod
    def load(cls, filePath):
        fd = open(filePath)
        data = yaml.load(fd)
        fd.close()
        obj = cls(data, filePath)
        return obj

    def __init__(self, data, filePath=None, parent=None, name=None):
        self._name = name
        self._parent = parent
        self._filePath = filePath
        self._data = data

    def __repr__(self):
        data = "%s %i" % (self._yamlPath(), id(self))
        return "<YamlObject %s>" % data

    def __dir__(self):
        if sys.version_info[0]==3:
            ret = super().__dir__()
        else:
            ret = set((dir(type(self)) + list(self.__dict__)))
        ret.extend(list(self._data.keys()))
        return ret

    def _yamlPath(self):
        if not self._parent:
            return "."
        else:
            return self._parent._yamlPath()+self._name+"."

    def toDict(self):
        return self._data

    def __getattr__(self, item):
        if item.startswith("_"):
            return object.__getattribute__(item)
        else:
            if item in self._data:
                data = self._data[item]
                if not isinstance(data, dict):
                    return data
                return self.__class__(data, parent=self, name=item)
            else:
                return object.__getattribute__(item)





