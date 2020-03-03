# coding   : utf-8 
# @Time    : 2020/1/28 21:38
# @Author  : 小迷弟
# @File    : save_jpg.py
# @Email   : lihu5682@126.com
# @Desc    : NONE
# @Software: PyCharm

import requests

response = requests.get("https://dss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=1925586250,1389404571&fm=58&s=2B62CC12E9E65E11004D18D60200D0B1")
with open("a.png", "wb") as f:
    f.write(response.content)
