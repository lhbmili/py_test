# re 高低位
import string
import re
payloads = string.ascii_letters+string.digits+string.punctuation
with open("4.txt",'r') as f:
    #114个
    list1 = [0,]*32
    #得到数组
    for i in f:
        #每行：  v11 = 100;  正则表达式取出数据
        s = ''.join(re.findall(r'= (.*?);',i))
        num = ''.join(re.findall(r'v(.*?) =',i))
        #从v2开始
        list1[int(num)-2] = int(s)
    #运算
for i in range(32):
    for n in range(128):
        if ((n>>4|n*16) & 0xff == list1[i] & 0xff):
            print(chr(n),end="")
# for i in range(32):
#     for p1 in payloads:
#         p = bin(ord(p1))[2:].zfill(8)
#         p_xunhuan = p[4:]+p[:4]
#         r = int(p_xunhuan,2)
#         if r == list1[i] & 0xff:
#             print(p1,end="")