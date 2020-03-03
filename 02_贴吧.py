# coding   : utf-8 
# @Time    : 2020/1/27 19:44
# @Author  : 小迷弟
# @File    : 02_贴吧.py
# @Email   : lihu5682@126.com
# @Desc    : NONE
# @Software: PyCharm


import requests


class TieBa_spider(object):
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36"}

    def run(self):
        # 1、url列表
        url_list = self.get_urllist()
        # 2、遍历发送请求，获取response
        for url in url_list:
            html_str = self.parse_url(url)
            page_num = url_list.index(url) + 1
            # 3、保存
            self.save(html_str, page_num)

    def get_urllist(self):  # url列表
        url_list = []
        for i in range(1000):
            url_list.append(self.url_temp.format(i * 50))
        return url_list

    def parse_url(self, url):  # url请求
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save(self, html_str, page_num):  # 保存HTML 字符串
        file_path = "D:/software/Python/code/{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf-8") as f:  # 李毅-第一页
            f.write(html_str)


if __name__ == '__main__':
    TieBa_spider = TieBa_spider("lol")
    TieBa_spider.run()
