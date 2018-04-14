import os
import os.path

rootlogfile = ".bylw.log"

class fileoperate:
    def __init__(self):
        pass
    def writelogtofile(self,logmsg):
        logfile = open(rootlogfile,"a")
        logfile.write(logmsg)
        logfile.close()
    def readlogfile(self):
        logfile = open(rootlogfile,"r")
        logmsg = logfile.read()
        return logmsg

    def writelog_w(self,path,msg):
        file = open(path,"w")
        file.write(msg)
        file.close()

    def writelog_a(self,path,msg):
        file = open(path,"a")
        file.write(msg)
        file.close()

    def readlog(self,path):
        file = open(path,"r")
        return file.read()