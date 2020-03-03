# coding   : utf-8 
# @Time    : 2020/1/29 20:53
# @Author  : 小迷弟
# @File    : baidu_fanyi.py
# @Email   : lihu5682@126.com
# @Desc    : NONE
# @Software: PyCharm
import  requests
import json



class BaiduFanyi(object):
    def __init__(self, trans_str):
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.trans_str = trans_str
        self.trans_url = "https://fanyi.baidu.com/basetrans"
        self.headers = {"user-agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Mobile Safari/537.36"}


    def paurse_url(self, url, data):
        response = requests.post(url, data=data, headers=self.headers)
        print(json.loads(response.content.decode()))
        return json.loads(response.content.decode())


    def get_ret(self, dict_response):
        ret = dict_response["trans"][0]["dst"]
        print("result is:", ret)


    def run(self):# 实现主要逻辑
        # 1、获取语言类型
            # 1.1、准备post的url地址，post_date
        lang_detect_date = {"query": self.trans_str}
            # 1.2、发送post请求，获取响应
        lang = self.paurse_url(self.lang_detect_url,lang_detect_date)["lan"]
            # 1.3、提取语言类型
        # 2、准备post数据
        trans_date = {"query": self.trans_str,"token": "bec30407d275d430817164fbbb57414b","from": "zh","to": "en"} if lang == "zh" else \
            {"query": self.trans_str, "token": "bec30407d275d430817164fbbb57414b", "from": "zh", "to": "en"}
        # 3、发送请求，获取相应
        dict_response = self.paurse_url(self.trans_url, trans_date)
        # 4、获取结果
        self.get_ret(dict_response)




if __name__ == '__main__':
    BaiduFanyi = BaiduFanyi("我是谁")
    BaiduFanyi.run()