# coding: utf-8
import os

if __name__ == '__main__':
    file_path= "{}/{}".format(os.path.dirname(os.path.abspath(__file__)),
                              "setting.json")
    with open(file_path) as f:
        content = f.read()
        print(content)
