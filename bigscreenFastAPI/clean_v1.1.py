# _*_ coding: utf-8 _*_

import os
import statistics
import re
import arrow
import shutil
import psutil
from operator import itemgetter


class Clean:
    # 属性：所有对象共享。
    toady_format = arrow.utcnow().format("YYYYMMDD")
    fiften_later = arrow.utcnow().shift(days=-15).format("YYYYMMDD")
    full_toady_format = arrow.utcnow().format("YYYYMMDDHHmmss")
    files_list = []
    dir_list = []

    def __init__(self, root_dir, bak_file):
        self.root_dir = root_dir
        self.bak_file = bak_file

    # 创建备份目录
    def mkfile_bak(self):
        if not os.path.exists(self.bak_file):
            os.mkdir(self.bak_file)

    # 跳过目录，筛选 名成_时间类型的文件
    # 不符合条件的文件移动到今天日期的"20210830.bak"目录下

    def return_list(self):
        os.chdir(self.root_dir)
        for i in os.listdir(self.root_dir):
            if os.path.isfile(i):
                if Clean.toady_format in i:
                    if '_' in i:
                        Clean.files_list.append(i)
                    else:
                        try:
                            shutil.move(i, self.bak_file)
                            print(f"time: {Clean.full_toady_format} {i} 移动到 ===> {self.bak_file}")
                        except:
                            shutil.move(i, os.path.join(self.bak_file, i + Clean.full_toady_format))
                            print(f"time: {Clean.full_toady_format} {i} 移动到 ===> {os.path.join(self.bak_file, i + Clean.full_toady_format)}")
                else:
                    try:
                        shutil.move(i, self.bak_file)
                        print(f"time: {Clean.full_toady_format} {i} 移动到 ===> {self.bak_file}")
                    except:
                        shutil.move(i, os.path.join(self.bak_file, i + Clean.full_toady_format))
                        print(f"time: {Clean.full_toady_format} {i} 移动到 ===> {os.path.join(self.bak_file, i + Clean.full_toady_format)}")
        return Clean.files_list

    def mv_little(self):
        os.chdir(self.root_dir)
        clist = []
        panlist = []
        for i in Clean.files_list:
            b = i.split('_')
            clist.append([i, b[0], b[1].split('.')[0]])

        clist.sort()
        if not panlist:
            panlist = clist[0]
        for i in clist:
            if i[1] == panlist[1]:
                # 如果新时间大,则将表中的文件名移动到备份目录，并更新表,
                if i[-1] > panlist[-1]:
                    shutil.move(panlist[0], self.bak_file)
                    print(f"time: {Clean.full_toady_format} {panlist[0]} 移动到 ===> {self.bak_file}")
                    panlist[-1] = i[-1]
                    panlist[0] = i[0]
                elif i[-1] == panlist[-1]:
                    pass
                # 如果新时间小，则移动至备份目录
                else:
                    shutil.move(i[0], self.bak_file)
                    print(f"time: {Clean.full_toady_format} {i[0]} 移动到 ===> {self.bak_file}")
            else:
                panlist = i


if __name__ == '__main__':
    cleaner = Clean(
        root_dir=r'G:\2.Python_Env\bigscreenAPI\data_test',
        bak_file=r'G:\2.Python_Env\bigscreenAPI\report_bak')

    cleaner.mkfile_bak()
    cleaner.return_list()
    cleaner.mv_little()
