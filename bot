from graia.ariadne.app import Ariadne
from graia.ariadne.entry import config
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import *
from graia.ariadne.model import Group
from wbspider import get_weibo


# # 获得微博内容
weibo=get_weibo()

# =====================================================
from graia.ariadne.app import Ariadne
from graia.ariadne.entry import config
from graia.ariadne.message.chain import MessageChain
from graia.ariadne.message.element import Plain
from graia.ariadne.model import Group

# 获取机器人实例
app = Ariadne(
    config(
        verify_key="INITKEY48lKMK6Z",  # 填入 VerifyKey
        account=2696849938,  # 你的机器人的 qq 号
    ),
)

# 监听命令，返回微博
@app.broadcast.receiver("GroupMessage")
async def wbmsg(app: Ariadne, group: Group, message: MessageChain):
    if str(message) == "/ff14wb":
        await app.send_message(group, MessageChain(weibo))

app.launch_blocking()
# =====================================================


