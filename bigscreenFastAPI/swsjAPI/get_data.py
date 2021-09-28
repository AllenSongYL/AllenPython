import requests
#import json
import arrow
#import os
import subprocess

bigbase_url = 'http://10.212.1.6:80/wbdlp/v1/alertmsgletest'

#request_head = {"User-Agent": r"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:42.0) Gecko/20100101 Firefox/42.0",
#                "Accept": r"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#                "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#                "Accept-Encoding": "gzip, deflate",
#                "Connection": "keep-alive",
#                "Cache-Control": "max-age=0",
#                "token": "s8GgvvguRIdYYlwfh4PDpBFxQkYEDb0pqMBrd7E7aP5N4Kt5cQE7BQXKb8zNSf%2B4X%2FUmcgTnzWuDP8ZQSVhgFw%3D%3D"
#                }


request1 = requests.get(url=bigbase_url)
request1 = request1.json()["data"][0]
request1["event_type"] = "swsj_alert"
request1 = str(request1)

#full_today_format = arrow.now('Asia/Shanghai').format("YYYYMMDDHHmmss")
full_time2 = arrow.now('Asia/Shanghai').format("YYYY-MM-DD HH:mm:ss")

write_file = r'/home/ueba/swsjAPI/swsj_alert.log'
command = f"tail -n 1 {write_file}"
docommand = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
lastline = docommand.stdout.read().rstrip().lstrip().decode('utf-8')


if request1 != lastline:
    print(f"{full_time2}, 新增告警: {request1}")
    with open(write_file, 'a+') as f1:
        f1.write(request1 + "\n")
else:
    print(f"{full_time2}, 接口内容未发生变化!")