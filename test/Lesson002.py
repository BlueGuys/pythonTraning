#!/usr/bin/python
# coding=utf-8
import os


def write_test(s):
    write_file = open('./Test.txt', 'a')
    write_file.write(s)
    write_file.write('\n')
    write_file.close()


def start_read(file_name):
    if '.js' not in file_name:
        return
    read_file = open(file_name)
    for line in read_file:
        if '.png' in line and '@2x' not in line:
            write_test('---------------------------------------------------------------------------')
            write_test(file_name.replace('/Users/wangning/Work/JDB/react/RNMainProject/', '', 1))
            write_test(line)
    read_file.close()


def start(path):
    list_dirs = os.walk(path)
    for root, dirs, files in list_dirs:
        for f in files:
            start_read(os.path.join(root, f))

start('/Users/wangning/Work/JDB/react/RNMainProject/js/JDBRN')
