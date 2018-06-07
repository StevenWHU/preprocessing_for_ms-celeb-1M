#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time    : 2018/6/7 11:29
# @Author  : Steven Chai
# @Email   : stevenchai@whu.edu.cn
# @File    : ms_celeb_1M_clean.py
# @Software: PyCharm

import os
import shutil
import time

# set file path
rootdir = '/home/cxy/Datasets/ms-celeb-1M/'
src_folder = os.path.join(rootdir, '20180605_FaceImageCroppedWithAlignment/')
dst_folder = os.path.join(rootdir, 'ms-celeb-1M_clean/')
clean_list = '/home/cxy/workspace/datasets_processing/ms_celeb_1M/MS-Celeb-1M_clean_list.txt'

# image counter
img_count = 0

def ms_celeb_1M_clean(src, dst, list):

    # open file
    with open(list, 'r') as file_to_read:
        while True:
            lines = file_to_read.readline()  # read data line by line
            if not lines:
                break
                pass
            line = lines.strip()
            img_RP = line.split(' ')[0]  # image relative path
            img_AP = os.path.join(src, img_RP)  # image absolute path

            # whether the image file exists or not
            if os.path.exists(img_AP):
                pass
                # print("current image path: %s" % (img_AP))
            else:
                print("warning:the path doesn`t exist %s" % (img_AP))
                break

            # generate file path information
            path_info = img_AP.split('/')
            parent_dir = path_info[6]
            img_name = path_info[7]
            dst_folder_sub = os.path.join(dst, parent_dir)

            if not os.path.exists(dst_folder_sub):
                os.mkdir(dst_folder_sub)
                print("Create dst dir: %s" % (dst_folder_sub))
            # copyfile
            dst_AP = os.path.join(dst_folder_sub, img_name)
            shutil.copyfile(img_AP, dst_AP)

            # counting the number of images to verify
            img_count = img_count + 1


if __name__ == '__main__':
    startTime = time.clock()

    ms_celeb_1M_clean(src_folder, dst_folder, clean_list)
    print('Total image number is : %d\n' % (img_count))

    endTime = time.clock()
    time_mi = endTime // 60
    time_s = endTime // 1 % 60
    time_ms = ((endTime * 100) // 1) % 100
    print("Total time consume: %02.0f:%02.0f:%2.0f" % (time_mi, time_s, time_ms))
