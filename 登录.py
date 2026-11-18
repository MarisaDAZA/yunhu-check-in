#!/usr/local/bin/python3
from websocket import create_connection, WebSocketException
from json import dumps
from time import sleep

def 连接云湖(用户标识, 令牌):
    登录 = dumps({
        "cmd": "login",
        "data": {
            "userId": 用户标识,
            "token": 令牌,
            "platform": "Web",
            "deviceId": "web-device-id"
        }
    })

    心跳 = dumps({
        "cmd": "heartbeat",
        "data": {}
    })

    网络套接字 = create_connection('wss://chat-ws-go.jwzhd.com/ws')
    网络套接字.send(登录)
    网络套接字.send(心跳)
    网络套接字.recv()
    print(用户标识, "登录成功！")
    sleep(1)
    网络套接字.close()