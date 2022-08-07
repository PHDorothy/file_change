""" 
批量改变文件后缀
要遍历文件夹文件，提取文件后缀，并判断是否是需要的后缀，若不是则修改后缀。这里有个问题我要怎么修改才能放回去原文件？
 listdir函数 os.listdir(path)  
 path -- 需要列出的目录路径
 返回指定路径下的文件和文件夹列表
splitext函数
作用是分离文件名与扩展名，返回一个元组
import os
print (os.path.splitext('a_3.py'))---> ('a_3' '.py')
路径还是不会???
 """

import os 

#路径到底要怎样输入？
path="D:\\Code\\test\\"
file_list= os.listdir(path)
print(file_list)
for file in file_list:
    file_split = os.path.splitext(file)
    print(file_split)
    if len(file_split)==2:
        #这里的'txt'备替换
        if file_split[-1]== '.doc':
            #这里的'Word'替换结果
            newfile =file_split[0]+'.txt'
            os.rename(path+file,path+newfile)
