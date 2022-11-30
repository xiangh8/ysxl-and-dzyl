# -*- coding: utf-8 -*-
# __author__ = 'SnkrGao'
# __time__ = '2022/9/9 11:14'
from parseAttitude import *
from parseRepost import *
from parseComments import *

if __name__ == '__main__':
    f=open('a.txt')
    line = f.readline().strip() #读取第一行
    ids=[]
    ids.append(str(line))
    while line:  # 直到读取完文件
        line = f.readline().strip() # 读取一行文件，包括换行符
        if len(line)==0:
            break
        ids.append(line)
    f.close()  # 关闭文件
    print(ids)
    # weibo_id = 'L9FEpyN39'
    cookie='_T_WM=28441536733; SCF=AlWvll8oFMo0tvl1OqlA9sEReTf1FUx7KLZD9kpnQUYouglt4drPl544tLXxtkE1Qr94q1WXyWlVf62qRjKbXjQ.; SUB=_2A25OhBZxDeRhGeFK7FoW8yjEzD2IHXVthro5rDV6PUJbktAKLXLYkW1NQu7si1AgRszvjCd3F1CPeysuRamqAHht; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF11EseTs9BdXZUNCgaPjV.5JpX5K-hUgL.FoMXS0nNe0qRS022dJLoIEXLxKML1heLBKBLxKML1hBLBKqLxKML1-2L1hBLxKqLBK2L1KBLxK-LB-BL1K5t; ALF=1671951137; XSRF-TOKEN=5f06f8; WEIBOCN_FROM=1110006030; mweibo_short_token=56522fc499; MLOGIN=1'
    
    for weibo_id in ids:
        # parseattitude = parseAttitude(weibo_id=weibo_id, cookie=cookie)
        # parseattitude.SpiderAttitude()
        # parserepost = parseRepost(weibo_id=weibo_id, cookie=cookie)
        # parserepost.SpiderTransmit()
        parsecomments = parseComments(weibo_id=weibo_id, cookie=cookie)
        parsecomments.main()
