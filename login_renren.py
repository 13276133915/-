# coding   : utf-8 
# @Time    : 2020/1/28 20:37
# @Author  : 小迷弟
# @File    : login_renren.py
# @Email   : lihu5682@126.com
# @Desc    : NONE
# @Software: PyCharm

import  requests

session = requests.session()
post_rul = "http://www.renren.com/PLogin.do"
post_data = {"email": "13276133915", "password":"5682jkljkl"}
headers = {"user-agent":"Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"}
r = session.post(post_rul, data=post_data, headers=headers )
print(r.status_code)
with open("renren.html", "w", encoding="utf-8") as f:
    f.write(r.content.decode())