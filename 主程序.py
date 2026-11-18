import os
from 登录 import 连接云湖
from 金币 import 抽奖

for 用户 in os.environ['ID_TOKEN'].splitlines():
    if 用户.strip():
        标识, 令牌 = 用户.split()
        连接云湖(标识, 令牌)
        抽奖(令牌)