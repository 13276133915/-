# coding   : utf-8 
# @Time    : 2020/1/28 19:51
# @Author  : 小迷弟
# @File    : fanyi.py
# @Email   : lihu5682@126.com
# @Desc    : NONE
# @Software: PyCharm
import requests

headers = {"user-agent":"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"}
date = {
    "query": "人生苦短，我用python",
    "from": "en",
    "to": "zh",
    "token": "bec30407d275d430817164fbbb57414b",
    "sign": "289133.35420"
}
post_url = "https://fanyi.baidu.com/basetrans"
response = requests.post(post_url, data=date, headers=headers)
print(response.content.decode())