# coding:utf-8

class ModelBase(object):

    def __init__(self, **entries):
        self.__dict__.update(entries)
