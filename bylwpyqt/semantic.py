import globallob.alllib as alllib



def setcmdflagfunc(msg,ustr,num):
    flag = 0
    for i in ustr:
        if str(msg).find(i) == -1:
            flag = -1
    if flag == 0:
        alllib.cmdflag = num

def getsemantic(msg):
    setcmdflagfunc(msg,u"开灯",1)
    setcmdflagfunc(msg,u"关灯",2)
    setcmdflagfunc(msg,u"温湿",3)
    setcmdflagfunc(msg,u"关机",4)
    return 0
