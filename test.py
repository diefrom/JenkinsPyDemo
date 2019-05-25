import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print("This is {}".format(sys.argv[1]))
    else:
        print("hello jenkins")
