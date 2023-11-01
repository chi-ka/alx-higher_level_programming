#!/usr/bin/python3
class LockedClassi:
    """ loked class"""
    def __setattr__(self, name, value):
        """ sets an attribute"""
        if name == "first_name":
            super().__setattr__(name, value)
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
