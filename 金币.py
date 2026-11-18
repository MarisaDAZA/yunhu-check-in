from json import loads
from time import sleep
from 用户机器人 import 接口

def 抽奖(token):
    接口实例=接口(token)
    def 点击按钮(消息表示, 值):
        接口实例.点击按钮('62518108', 3, '62518108', 消息表示, 值)
    for _ in range(3):
        消息列表 = 接口实例.列出消息('62518108',3)
        for 消息 in 消息列表:
            文本 = 消息.content.text.splitlines()[0]
            if 消息.content.buttons:
                print(文本)
                按钮 = loads(消息.content.buttons)
                if 文本.startswith('今日获得'):
                    # 去抽奖
                    点击按钮(消息.id, 按钮[0][1]['value'])
                elif 文本.startswith('恭喜获得'):
                    # 加入钱包
                    点击按钮(消息.id, 按钮[0][0]['value'])
                else:
                    点击按钮(消息.id, 按钮[1][0]['value'])
        sleep(1)
