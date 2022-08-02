"""
python 第一个小项目，文件管理脚本。
1、第一步，批量给文件重新修改后缀。

用户使用的时候类似这样。
rename.py work_dir cur_suffix new_suffix

比如
rename.py D:\dorjake txt pdf
就是把D:\dorjake目录下的txt结尾的文件，都重新命名成pdf结尾。
"""

# windows path C:\home\jake\Code
# Linux path /home/jake/Code

import os
import re
import sys

# C:\Users\Jake-VM\Desktop\code\test_dir

def main():
    # Step1: 获取命令行参数
    # print(len(sys.argv))
    if len(sys.argv) != 4:
        print("error! please use: rename.py work_dir cur_suffix new_suffix")
        return

    work_dir   = sys.argv[1]
    cur_suffix = sys.argv[2]
    new_suffix = sys.argv[3]

    try:
        dir_list = os.listdir(work_dir)
    except FileNotFoundError:
        print("error! your input path: {} is illegal!".format(work_dir))
        return

    # Step2: 获取需要修改的文件放入pending_changed
    # full_name = prefix.suffix
    pending_changed = []
    for full_name in dir_list:
        list_name = full_name.split(sep=".")

        # 假设文件夹不包含"."
        if len(list_name) == 1:
            # print("过滤掉文件夹 full_name={}".format(full_name))
            continue

        suffix = list_name[-1]

        # print("full_name={}, suffix={}".format(full_name, suffix))

        if suffix == cur_suffix:
            pending_changed.append(full_name)

    # Step3: 修改pending_changed中的文件名称
    

if __name__ == '__main__':
    main()