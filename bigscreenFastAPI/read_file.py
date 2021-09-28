# _*_ coding: utf-8 _*_
import json
import os
import pandas as pd
import codecs
import re
from fastapi import HTTPException

# sys.stdout.encoding('utf-8')
# 获取/home/easy-agent/data/ueba-dashboard/report目录下所有csv报表



# 获取符合条件的文件名列表
def get_list(dirs):
    allfiles = []
    alls = os.listdir(dirs)
    alls.sort(reverse=True)
    for x in alls:
        if os.path.isfile(os.path.join(dirs, x)):
            if '_' in x:
                head = x.split('_')
                if head[0] not in str(allfiles):
                    allfiles.append(x)
    return allfiles

# 将索引数据保存到文件
def save_index(indexdirs, indexfiles):
    if not os.path.isdir(indexdirs):
        os.mkdir(indexdirs)
    if not os.path.isfile(indexfiles):
        open(indexfiles, 'a').close()


# 读CSV并转换的函数
def read_csv(filename):
    f_con = pd.read_csv(filename, encoding='utf-8', engine='c')
    jsoncon = f_con.to_json(orient='records', force_ascii=False)
    jsoncon = json.loads(jsoncon)
    return jsoncon



# get请求返回索引数据
def get_index(dirs, idxf):
    os.chdir(dirs)
    book = {}
    boo_k = {}
    all_files = get_list(dirs)
    book["count"] = len(all_files)
    n = 1

    for i in all_files:
        boo_k[str(n)] = i
        n += 1
    book["report"] = boo_k
    with open(idxf, 'w+', encoding='utf-8') as f1:
        f1.write(str(book["report"]).replace('\'', '"'))
    return book


def read_files(dirs, nums, idxf):
    os.chdir(dirs)
    with codecs.open(idxf, 'r', encoding='utf-8') as f1:
        f_con = f1.readline()
    d_con = json.loads(f_con)
    for i, y in d_con.items():
        if i == str(nums):
            jsonfile = read_csv(y)
    return jsonfile


def rex_file(dirs, filename):
    if '-' not in filename:
        raise HTTPException(status_code=404, detail='接口格式错误！')
    d_content = []
    allfiles = get_list(dirs)
    if filename not in str(allfiles):
        raise HTTPException(status_code=404, detail='接口不存在！')
    for i in allfiles:
        if filename in i:
            d_content = read_csv(os.path.join(dirs, i))
    return d_content


# def all_files(r_dir):
#     file_name = []
#     file_con = []
#     for f1 in os.listdir(r_dir):
#         f2 = os.path.join(r_dir, f1)
#         # print(type(f2))
#         if os.path.isfile(f2):
#             # if f2.endswitch('csv'):
#             # f_list = pd.read_csv(f2, encoding='utf-8').to_json(orient='records', force_ascii=False)
#             f_list = eval(read_files(f2))
#             file_con.append(f_list)
#             file_name.append(os.path.basename(f2))
#
#     results = dict(zip(file_name, file_con))
#     return results


# or command "uvicorn main:app --reload"

if __name__ == '__main__':
    root_dir = r'/home/ueba/easygo-agent/data/ueba-dashboard/report'
    indexdir = os.path.join(root_dir, 'Index')
    indexfile = os.path.join(indexdir, 'index.txt')
    # book = get_index(root_dir, indexfile)
    # read_files(root_dir, 2, indexfile)
    file1 = 'db-legal-person'
    # rex_file(root_dir, file1)
    f1 = get_list(root_dir)
    cont = rex_file(root_dir, file1)
    print(cont)
    # for i in os.listdir(root_dir):
    #     i = os.path.join(root_dir, i)
    #     if os.path.isfile(i):
    #         read_files(i)
    #
    # all_files(root_dir)
    # file_counts(root_dir)
