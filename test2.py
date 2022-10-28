# -*- coding: utf-8 -*-
import socket
import ctypes

# 调用c++动态链接库
from rospy import sleep

so = ctypes.cdll.LoadLibrary
lib = so("/home/lqg/KDevProjects/CohandDriver/lib.so")

# socket连接（主机ip需改为192.168.1.1）
HOST = "192.168.1.2"    # The remote host
PORT = 30003        # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# 6个参数是[x,y,z,rx,ry,rz];
strL1 = b"movej(p[-0.10,-0.10,0.50,0.0125,-0.0146,0.8],a=0.5,v=0.3)\n"

strL2 = b"movej(p[-0.2,-0.3,0.4,-0.08,-1.57,0.13],a=0.5,v=0.3)\n"

strHome = b"movej(p[-0.18755,-0.10356,0.38232,-0.92082,-0.80881,-0.03977],a=0.5,v=0.3)\n"    # 悬停位置1

strHover1 = b"movej(p[-0.21366,-0.13995,0.24717,-0.77758,-1.41499,-0.24230],a=0.5,v=0.3)\n"    # 悬停位置1
strHover2 = b"movej(p[-0.25159,0.02282,0.28840,-1.02040,-1.25050,-0.85284],a=0.5,v=0.3)\n"    # 悬停位置2

strGrasp1 = b"movej(p[-0.22932,-0.13010,0.12470,-0.53857,-1.53347,-0.40823],a=0.5,v=0.3)\n"    # 抓笔位置1
strGrasp2 = b"movej(p[-0.29096,0.04557,0.17647,-1.08496,-1.28257,-0.97088],a=0.5,v=0.3)\n"    # 抓笔位置2

#  ************************************************************************************************
strW0 = b"movej(p[-0.15874,0.04791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite00 = b"movej(p[-0.15874,0.04791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 新0
strWrite01 = b"movej(p[-0.16874,0.03791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite02 = b"movej(p[-0.16874,0.03791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strW1 = b"movej(p[-0.16874,0.06291,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite10 = b"movej(p[-0.16874,0.06291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 新1
strWrite11 = b"movej(p[-0.16874,0.02291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite12 = b"movej(p[-0.16874,0.02291,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strW2 = b"movej(p[-0.16874,0.05791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite20 = b"movej(p[-0.16874,0.05791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 新2
strWrite21 = b"movej(p[-0.17874,0.04791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite22 = b"movej(p[-0.17874,0.04791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strW3 = b"movej(p[-0.16874,0.02791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite30 = b"movej(p[-0.16874,0.02791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 新3
strWrite31 = b"movej(p[-0.17874,0.03791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite32 = b"movej(p[-0.17874,0.03791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strW4 = b"movej(p[-0.17874,0.06791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite40 = b"movej(p[-0.17874,0.06791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 新4
strWrite41 = b"movej(p[-0.17874,0.01791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite42 = b"movej(p[-0.17874,0.01791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strW5 = b"movej(p[-0.18874,0.05791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite50 = b"movej(p[-0.18874,0.05791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 新5
strWrite51 = b"movej(p[-0.18874,0.02791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite52 = b"movej(p[-0.18874,0.02791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strW6 = b"movej(p[-0.17874,0.04291,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite60 = b"movej(p[-0.18074,0.04291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 新6
strWrite61 = b"movej(p[-0.21874,0.04291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite62 = b"movej(p[-0.20874,0.04791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite63 = b"movej(p[-0.20874,0.04791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strW7 = b"movej(p[-0.19874,0.04791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite70 = b"movej(p[-0.19874,0.04791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 新7
strWrite71 = b"movej(p[-0.20874,0.05791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite72 = b"movej(p[-0.20874,0.05791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strW8 = b"movej(p[-0.19874,0.03791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite80 = b"movej(p[-0.19874,0.03791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 新8
strWrite81 = b"movej(p[-0.20874,0.02791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite82 = b"movej(p[-0.20874,0.02791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strW9 = b"movej(p[-0.15874,-0.00291,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite90 = b"movej(p[-0.15874,-0.00291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 新9
strWrite91 = b"movej(p[-0.16874,0.01291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite92 = b"movej(p[-0.20874,0.02291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite93 = b"movej(p[-0.20874,0.02291,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strW10 = b"movej(p[-0.17874,0.01291,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite100 = b"movej(p[-0.17874,0.01291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 新10
strWrite101 = b"movej(p[-0.17874,-0.00709,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite102 = b"movej(p[-0.17874,-0.00709,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strW11 = b"movej(p[-0.17874,0.00291,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite110 = b"movej(p[-0.17874,0.00291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 新11
strWrite111 = b"movej(p[-0.21874,0.00291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWrite112 = b"movej(p[-0.21874,0.00291,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
#  ************************************************************************************************
strN0 = b"movej(p[-0.22874,0.04791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteN00 = b"movej(p[-0.22874,0.04791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 年0
strWriteN01 = b"movej(p[-0.24874,0.05791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteN02 = b"movej(p[-0.24874,0.05791,0.10805,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strN1 = b"movej(p[-0.23874,0.04991,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteN10 = b"movej(p[-0.23874,0.04991,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 年1
strWriteN11 = b"movej(p[-0.23874,0.00791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteN12 = b"movej(p[-0.23874,0.00791,0.10805,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strN2 = b"movej(p[-0.24874,0.04791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteN20 = b"movej(p[-0.24874,0.04791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 年2
strWriteN21 = b"movej(p[-0.24874,0.01291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteN22 = b"movej(p[-0.24874,0.01291,0.10805,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strN3 = b"movej(p[-0.24874,0.04791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteN30 = b"movej(p[-0.24874,0.04791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 年3
strWriteN31 = b"movej(p[-0.25874,0.04791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteN32 = b"movej(p[-0.25874,0.04791,0.10805,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strN4 = b"movej(p[-0.25874,0.05791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteN40 = b"movej(p[-0.25874,0.05791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 年4
strWriteN41 = b"movej(p[-0.25874,0.00791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteN42 = b"movej(p[-0.25874,0.00791,0.10805,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strN5 = b"movej(p[-0.23874,0.02791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteN50 = b"movej(p[-0.24074,0.02791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 年5
strWriteN51 = b"movej(p[-0.27874,0.02791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteN52 = b"movej(p[-0.27874,0.02791,0.10805,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
#  ************************************************************************************************
strK0 = b"movej(p[-0.30874,0.05791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK00 = b"movej(p[-0.30874,0.05791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 快0
strWriteK01 = b"movej(p[-0.31874,0.06791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK02 = b"movej(p[-0.31874,0.06791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strK1 = b"movej(p[-0.29874,0.05291,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK10 = b"movej(p[-0.29874,0.05291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 快1
strWriteK11 = b"movej(p[-0.34874,0.05291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK12 = b"movej(p[-0.34874,0.05291,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strK2 = b"movej(p[-0.30874,0.04791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK20 = b"movej(p[-0.30874,0.04791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 快2
strWriteK21 = b"movej(p[-0.31874,0.03791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK22 = b"movej(p[-0.31874,0.03791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strK3 = b"movej(p[-0.30874,0.03791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK30 = b"movej(p[-0.30874,0.03791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 快3
strWriteK31 = b"movej(p[-0.30874,0.00791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK32 = b"movej(p[-0.32374,0.00791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK33 = b"movej(p[-0.32374,0.00791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strK4 = b"movej(p[-0.32374,0.04291,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK40 = b"movej(p[-0.32374,0.04291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 快4
strWriteK41 = b"movej(p[-0.32374,-0.00209,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK42 = b"movej(p[-0.32374,-0.00209,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strK5 = b"movej(p[-0.29874,0.02291,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK50 = b"movej(p[-0.29874,0.02291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 快5
strWriteK51 = b"movej(p[-0.32874,0.02291,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK52 = b"movej(p[-0.34874,0.03791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK53 = b"movej(p[-0.34874,0.03791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strK6 = b"movej(p[-0.33874,0.01791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK60 = b"movej(p[-0.33874,0.01791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 快6
strWriteK61 = b"movej(p[-0.34874,0.00791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteK62 = b"movej(p[-0.34874,0.00791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
#  ************************************************************************************************
strLL0 = b"movej(p[-0.35874,0.01791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteL00 = b"movej(p[-0.35874,0.01791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 乐0
strWriteL01 = b"movej(p[-0.36874,0.04791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteL02 = b"movej(p[-0.38874,0.04791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteL03 = b"movej(p[-0.38874,0.00791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteL04 = b"movej(p[-0.38874,0.00791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strLL1 = b"movej(p[-0.37374,0.02791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteL10 = b"movej(p[-0.37374,0.02791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 乐1
strWriteL11 = b"movej(p[-0.41874,0.02791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteL12 = b"movej(p[-0.40874,0.03791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteL13 = b"movej(p[-0.40874,0.03791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strLL2 = b"movej(p[-0.39874,0.03791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteL20 = b"movej(p[-0.39874,0.03791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 乐2
strWriteL21 = b"movej(p[-0.40874,0.04791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteL22 = b"movej(p[-0.40874,0.04791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"

strLL3 = b"movej(p[-0.39874,0.01791,0.11005,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteL30 = b"movej(p[-0.39874,0.01791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"    # 乐3
strWriteL31 = b"movej(p[-0.40874,0.00791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"
strWriteL32 = b"movej(p[-0.40374,0.00791,0.10235,-1.16667,-1.28886,-1.08622],a=0.5,v=0.3)\n"


# ×××××××××××××××××动作：写字××××××××××××××××××××
lib.openPort()
lib.pose(0)
lib.threeFLoosen()
s.send(strHover1)
sleep(7)
s.send(strGrasp1)
sleep(3)

# 到达位置
lib.threeFGrasp(500)
sleep(2)
s.send(strHover1)
sleep(3)
s.send(strHover2)
sleep(5)
s.send(strGrasp2)
sleep(5)
#  ************************************************************************************************
# 书写:新
s.send(strW0)
sleep(2)
s.send(strWrite00)  # 0
sleep(4)
s.send(strWrite01)
sleep(3)
s.send(strWrite02)

sleep(2)
s.send(strW1)
sleep(2)
s.send(strWrite10)  # 1
sleep(2)
s.send(strWrite11)
sleep(2)
s.send(strWrite12)

sleep(2)
s.send(strW2)
sleep(2)
s.send(strWrite20)  # 2
sleep(2)
s.send(strWrite21)
sleep(2)
s.send(strWrite22)

sleep(2)
s.send(strW3)
sleep(2)
s.send(strWrite30)  # 3
sleep(2)
s.send(strWrite31)
sleep(2)
s.send(strWrite32)

sleep(2)
s.send(strW4)
sleep(2)
s.send(strWrite40)  # 4
sleep(2)
s.send(strWrite41)
sleep(2)
s.send(strWrite42)

sleep(2)
s.send(strW5)
sleep(2)
s.send(strWrite50)  # 5
sleep(2)
s.send(strWrite51)
sleep(2)
s.send(strWrite52)

sleep(2)
s.send(strW6)
sleep(2)
s.send(strWrite60)  # 6
sleep(2)
s.send(strWrite61)
sleep(2)
s.send(strWrite62)
sleep(2)
s.send(strWrite63)

sleep(2)
s.send(strW7)
sleep(2)
s.send(strWrite70)  # 7
sleep(2)
s.send(strWrite71)
sleep(2)
s.send(strWrite72)

sleep(2)
s.send(strW8)
sleep(2)
s.send(strWrite80)  # 8
sleep(2)
s.send(strWrite81)
sleep(2)
s.send(strWrite82)

sleep(2)
s.send(strW9)
sleep(2)
s.send(strWrite90)  # 9
sleep(2)
s.send(strWrite91)
sleep(2)
s.send(strWrite92)
sleep(2)
s.send(strWrite93)

sleep(2)
s.send(strW10)
sleep(2)
s.send(strWrite100)  # 10
sleep(2)
s.send(strWrite101)
sleep(2)
s.send(strWrite102)

sleep(2)
s.send(strW11)
sleep(2)
s.send(strWrite110)  # 11
sleep(2)
s.send(strWrite111)
sleep(2)
s.send(strWrite112)
#  ************************************************************************************************
# 书写:年
sleep(2)
s.send(strN0)
sleep(2)
s.send(strWriteN00)  # 0
sleep(2)
s.send(strWriteN01)
sleep(2)
s.send(strWriteN02)

sleep(2)
s.send(strN1)
sleep(2)
s.send(strWriteN10)  # 1
sleep(2)
s.send(strWriteN11)
sleep(2)
s.send(strWriteN12)

sleep(2)
s.send(strN2)
sleep(2)
s.send(strWriteN20)  # 2
sleep(2)
s.send(strWriteN21)
sleep(2)
s.send(strWriteN22)

sleep(2)
s.send(strN3)
sleep(2)
s.send(strWriteN30)  # 3
sleep(2)
s.send(strWriteN31)
sleep(2)
s.send(strWriteN32)

sleep(2)
s.send(strN4)
sleep(2)
s.send(strWriteN40)  # 4
sleep(2)
s.send(strWriteN41)
sleep(2)
s.send(strWriteN42)

sleep(2)
s.send(strN5)
sleep(2)
s.send(strWriteN50)  # 5
sleep(2)
s.send(strWriteN51)
sleep(2)
s.send(strWriteN52)
#  ************************************************************************************************
# 书写:快
sleep(2)
s.send(strK0)
sleep(2)
s.send(strWriteK00)  # 0
sleep(2)
s.send(strWriteK01)
sleep(2)
s.send(strWriteK02)

sleep(2)
s.send(strK1)
sleep(2)
s.send(strWriteK10)  # 1
sleep(2)
s.send(strWriteK11)
sleep(2)
s.send(strWriteK12)

sleep(2)
s.send(strK2)
sleep(2)
s.send(strWriteK20)  # 2
sleep(2)
s.send(strWriteK21)
sleep(2)
s.send(strWriteK22)

sleep(2)
s.send(strK3)
sleep(2)
s.send(strWriteK30)  # 3
sleep(2)
s.send(strWriteK31)
sleep(2)
s.send(strWriteK32)
sleep(2)
s.send(strWriteK33)

sleep(2)
s.send(strK4)
sleep(2)
s.send(strWriteK40)  # 4
sleep(2)
s.send(strWriteK41)
sleep(2)
s.send(strWriteK42)

sleep(2)
s.send(strK5)
sleep(2)
s.send(strWriteK50)  # 5
sleep(2)
s.send(strWriteK51)
sleep(2)
s.send(strWriteK52)
sleep(2)
s.send(strWriteK53)

sleep(2)
s.send(strK6)
sleep(2)
s.send(strWriteK60)  # 6
sleep(2)
s.send(strWriteK61)
sleep(2)
s.send(strWriteK62)
#  ************************************************************************************************
# 书写:乐
sleep(2)
s.send(strLL0)
sleep(2)
s.send(strWriteL00)  # 0
sleep(2)
s.send(strWriteL01)
sleep(2)
s.send(strWriteL02)
sleep(2)
s.send(strWriteL03)
sleep(2)
s.send(strWriteL04)

sleep(2)
s.send(strLL1)
sleep(3)
s.send(strWriteL10)  # 1
sleep(2)
s.send(strWriteL11)
sleep(2)
s.send(strWriteL12)
sleep(2)
s.send(strWriteL13)

sleep(2)
s.send(strLL2)
sleep(2)
s.send(strWriteL20)  # 2
sleep(2)
s.send(strWriteL21)
sleep(2)
s.send(strWriteL22)

sleep(2)
s.send(strLL3)
sleep(2)
s.send(strWriteL30)  # 3
sleep(2)
s.send(strWriteL31)
sleep(2)
s.send(strWriteL32)


# 回收
sleep(4)
s.send(strHover2)
sleep(4)
s.send(strHover1)
sleep(3)
s.send(strGrasp1)
sleep(3)
lib.threeFLoosen()
s.send(strHome)
s.close()


# ×××××××××××××××××抓手测试××××××××××××××××××××

# lib.openPort()
# lib.pose(0)
# lib.poseParallelism()
# sleep(3)
# lib.poseSymmetry()
# sleep(2)
# lib.threeFGrasp(500)
# sleep(5)
# lib.threeFLoosen()
# sleep(2)
