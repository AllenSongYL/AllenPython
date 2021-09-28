# _*_ coding: utf-8 _*_

from fastapi import FastAPI, HTTPException
import read_file
import uvicorn
import os


app = FastAPI()


@app.get("/")
def index1():
    read_file.save_index(indexdirs=indexdir, indexfiles=indexfile)
    indexs_api = read_file.get_index(root_dir, indexfile)
    return indexs_api


@app.get('/{filename}')
def search_filename(filename: str):
    filename = filename.replace('_', '-')
    bigbases = read_file.rex_file(root_dir, filename)
    return bigbases

# way 2
@app.get("/index")
def index2():
    read_file.save_index(indexdirs=indexdir, indexfiles=indexfile)
    indexs_api = read_file.get_index(root_dir, indexfile)
    return indexs_api


@app.get('/index/{nums}')
def search(nums: int):
    indexs_api = read_file.get_index(root_dir, indexfile)
    indexs_len = indexs_api["count"]
    if 0 < nums <= int(indexs_len):
        onemessage = read_file.read_files(root_dir, nums, indexfile)
    else:
        raise HTTPException(status_code=404, detail='超出索引页，请输入正确的页数！')
    return onemessage


if __name__ == '__main__':
    root_dir = r'/home/ueba/easygo-agent/data/ueba-dashboard/report'
    indexdir = os.path.join(root_dir, 'Index')
    indexfile = os.path.join(indexdir, 'index.txt')
    uvicorn.run(app=app,
                host="10.212.1.55",
                port=12321,
                workers=1)
