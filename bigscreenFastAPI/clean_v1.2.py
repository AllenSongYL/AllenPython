# _*_ coding: utf-8 _*_

import os
import arrow
import shutil


class Clean:
    # 属性：所有对象共享。
    toady_format = arrow.utcnow().format("YYYYMMDD")
    fiften_later = arrow.utcnow().shift(days=-15).format("YYYYMMDD")
    full_toady_format = arrow.utcnow().format("YYYY-MM-DD HH:mm:ss")

    def __init__(self, root_dir, bak_file):
        self.root_dir = root_dir
        self.bak_file = bak_file

    # 创建备份目录
    def mkfile_bak(self):
        if not os.path.exists(self.bak_file):
            os.mkdir(self.bak_file)

    def mv_csv(self):
        os.chdir(self.root_dir)
        tmp_dict = {}
        for i in sorted(os.listdir(self.root_dir),reverse=True):
            if os.path.isfile(i):
                if '_' in i:
                    apiname = i.split("_")[0]
                    timename = i.split("_")[1].split(".")[0]
                    if apiname in tmp_dict.keys():
                        shutil.move(os.path.join(self.root_dir, i), os.path.join(self.bak_file, i))
                        print(f"time: {self.full_toady_format} {i}  移动到 ===> {self.bak_file}")
                    else:
                        tmp_dict[apiname] = timename
                else:
                    shutil.move(os.path.join(self.root_dir, i), os.path.join(self.bak_file, i))
                    print(f"time: {self.full_toady_format} {i} 移动到 ===> {self.bak_file}")


if __name__ == '__main__':
    cleaner = Clean(
        root_dir=r'/home/ueba/easygo-agent/data/ueba-dashboard/report',
        bak_file=r'/home/ueba/easygo-agent/data/ueba-dashboard/report_bak'
    )

    cleaner.mkfile_bak()
    cleaner.mv_csv()
