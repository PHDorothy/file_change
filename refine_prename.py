"""
给定python文件以及文件目录（可从电脑文件那直接复制地址），输出文件名不包含后缀，并且>重定向到**.tXt文件里,**可自己定义
在shell里面执行，命令行示意
python '.\refine_prename.py' D:\Data\研一\浙一相关文件\班级个人照\22级硕士6班-1寸照 > **t.txt
"""

# windows path C:\home\jake\Code
# Linux path /home/jake/Code

import os
import re
import sys

def main():
    # Step1: 获取命令行参数
    # print(len(sys.argv))

    work_dir   = sys.argv[1]

    try:
        dir_list = os.listdir(work_dir)
    except FileNotFoundError:
        print("error! your input path: {} is illegal!".format(work_dir))
        return

    for full_name in dir_list:
        list_name = full_name.split(sep=".")

        prename = list_name[0]

        print("prename={}".format(prename))
   

if __name__ == '__main__':
    main()