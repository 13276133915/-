# coding   : utf-8 
# @Time    : 2020/1/28 21:06
# @Author  : 小迷弟
# @File    : 字典推导式.py
# @Email   : lihu5682@126.com
# @Desc    : NONE
# @Software: PyCharm

cookies = "anonymid=k5xv8d2r-bet58; depovince=AH; _r01_=1; JSESSIONID=abcJQi9BZJ9nP5TA_jS-w; ick_login=74cc0794-d50b-4915-b147-385143f1d06e; taihe_bi_sdk_uid=669025658f32d666b4bb349237241997; taihe_bi_sdk_session=039ffccbed911098ade04b3e4d5a62c8; springskin=set; jebe_key=544f4c26-0956-4c04-8d70-0db6b643d5de%7C8363a659e39cfc4e68dcd5c2c79eb788%7C1580215720676%7C1%7C1580215702238; jebe_key=544f4c26-0956-4c04-8d70-0db6b643d5de%7C8363a659e39cfc4e68dcd5c2c79eb788%7C1580215720676%7C1%7C1580215702244; vip=1; wp_fold=0; wp=0; ick=ec1f77ab-4668-448e-8ce7-848502c016c3; first_login_flag=1; ln_uact=13276133915; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; loginfrom=null; t=e432064478768531e2399443989b58e32; societyguester=e432064478768531e2399443989b58e32; id=973559642; xnsid=13c5bbb9; ver=7.0; jebecookies=12b58e19-9ed1-45e7-890e-40deb53db796|||||"
cookies = {i.split("=")[0] : i.split("=")[1] for i in  cookies.split("; ")}
for i in  cookies:
    print(i, cookies.get(i), sep=" = ")
