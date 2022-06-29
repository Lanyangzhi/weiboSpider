import requests
import json
import jsonpath

import re
reg=re.compile('<[^>]*>')

url='https://m.weibo.cn/api/container/getIndex?page=1&count=1&containerid=1076031797798792'
response=requests.get(url)
obj=json.loads(response.text)
wbdate=jsonpath.jsonpath(obj,'$..created_at')

# 类型转换>数组转为字符串
wbdate=str(wbdate)



def get_weibo():
    # 读取缓冲
    a=open('cache.txt','r',encoding='utf-8').readline()
    b=wbdate
    # print(a,b)

    # 比较结果
    if a == b:
        None
    else:
    # 写入缓冲区
        with open('cache.txt','w',encoding='utf-8') as fp:
            fp.write(wbdate)
        # json 提取详情
        wbcontent=jsonpath.jsonpath(obj,'$..text')
        # 转换类型
        wbcontent=str(wbcontent)
        # print(wbcontent)
        # 正则提取，返回原始文本
        rawcontent=reg.sub('',wbcontent)
        return rawcontent



# if __name__=='__main__':
#     rsa=get_WbId()
#     print(rsa)
