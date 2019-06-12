# coding: utf-8
import os

if __name__ == '__main__':
    value = os.getenv("key")
    print("hello {}".format(value))
