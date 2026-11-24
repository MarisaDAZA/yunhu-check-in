from httpx import Client
from yunhu_pb2 import ListMessageBySeq, MessageList, ButtonReport

class 接口:
    def __init__(自己, 令牌):
        自己.客户端 = Client(http2=True, base_url='https://chat-go.jwzhd.com/v1/msg')
        自己.客户端.headers.update({'Token': 令牌})

    def 列出消息(自己, 聊天标识, 聊天类型):
        请求体 = ListMessageBySeq(
            chat_id = 聊天标识,
            chat_type = 聊天类型
        )
        响应 = 自己.客户端.post("/list-message-by-seq", data=请求体.SerializeToString())

        消息列表 = MessageList()
        消息列表.ParseFromString(响应.content)
        return 消息列表.messages

    def 点击按钮(自己, 聊天标识, 聊天类型, 发送者标识, 消息标识, 值):
        请求体 = ButtonReport(
            chat_id = 聊天标识,
            chat_type= 聊天类型,
            sender_id = 发送者标识,
            msg_id = 消息标识,
            value = 值
        )
        自己.客户端.post("/button-report", data=请求体.SerializeToString())
        