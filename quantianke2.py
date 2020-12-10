# -*- coding:utf-8 -*-
fp1=open("~/python/hanshu1.py","r",encoding="gbk")
info1=fp1.read()
print("字符串类型：")
print(type(info1))
print("字节类型：")


print(type(info1.encode("utf-8")))#编码为utf-8格式字节类型数据
fp2=open("~/python/hanshu1.py","w",encoding="utf-8")
fp2.write(info1)
fp1.close()
fp2.close()