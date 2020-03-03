# coding   : utf-8 
# @Time    : 2020/1/30 17:32
# @Author  : 小迷弟
# @File    : paurse_url.py
# @Email   : lihu5682@126.com
# @Desc    : NONE
# @Software: PyCharm

import  requests
from retrying import retry

@retry(stop_max_attempt_number=3)
def _paurse_url(url, method):
    if method == "get":
        response = requests.get(url, headers=headers, timeout=3)
    else:
        response = requests.post(url, headers=headers, timeout=3)
    print("*")
    assert response.status_code == 200
    return response.content.decode()


def paurse_url(url, method):
    try:
        html_str = _paurse_url(url)
    except:
        html_str = None

    return html_str

if __name__ == '__main__':
    url = "https://m.douban.com/movie/"
    headers = {"user-agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Mobile Safari/537.36"}
    print(paurse_url(url, "post"))
