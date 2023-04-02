'''
author by Mr.wdd
version 1.0
练习构造数据包
'''
from scapy.all import *
a=Ether()/IP(dst="www.baidu.com")/TCP()/"GET HTTP/1.1\r"
#输出16进制
hexdump(a)
#raw返回字节流
b=raw(a)
#读取pcap文件
c=rdpcap("http_25K_8000.pcap")
#for p in c:
    #打印概要
  #  print(p.summary())

