import subprocess
import time
import logging
def log():
    log_name ="log.log"
    logging.basicConfig(filename=log_name,level=logging.DEBUG,format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
class runUiautomatorApp(object):
    def __init__(self,file,apk,**kwargs):
        self.kwargs = kwargs
        if self.kwargs:
            list =[]
            for arg, value in kwargs.items():
                list.append(arg)
                list.append(value)
            print(list)

        self.file = file
        self.apk = apk

        self.f = open(file,'w')

        self.adb_push = 'adb push '+ self.apk + ' /data/local/tmp/com.example.jennyhe.mytest'
        self.adb_install = 'adb shell pm install -t -r "/data/local/tmp/com.example.jennyhe.mytest"'

        self.adb_readper = 'adb shell pm grant com.example.jennyhe.mytest android.permission.READ_EXTERNAL_STORAGE'
        self.adb_writeper = 'adb shell pm grant com.example.jennyhe.mytest android.permission.WRITE_EXTERNAL_STORAGE'  # 通过adb 给予读写外部存储卡的权限



        #self.adb_run='adb shell "nohup am instrument -w -r   -e package com.example.jennyhe.mytest -e debug false com.example.jennyhe.mytest.test/android.support.test.runner.AndroidJUnitRunner 2>&1 |tee -a /storage/emulated/0/log.txt"'
        self.adb_run='adb shell "nohup am instrument -w -r -e package com.example.jennyhe.mytest -e debug false -e key 10086  com.example.jennyhe.mytest.test/android.support.test.runner.AndroidJUnitRunner 2>&1 |tee -a /storage/emulated/0/log.txt" '  # 传入参数的adb命令
    def subproc(self,cmd):
        return subprocess.Popen(cmd, shell=True,stdout = self.f.fileno(), stderr = self.f.fileno()).wait()
    def initApp(self):
        self.subproc(self.adb_push)
        self.subproc(self.adb_install)
    def getpermission(self):
        self.subproc(self.adb_readper)
        self.subproc(self.adb_writeper)
    def runApp(self,times=None):
        self.initApp()
        self.getpermission()
        if times:
            for self.i in range(times):
                logging.info("第%i测试",self.i)
                self.subproc(self.adb_run)
        self.subproc(self.adb_run)
        self.f.flush()
        self.f.close()

if __name__ == "__main__":
    log()
    file = "runApp.log" #存储返回值的文件
    apk = 'Uiautomator_file.apk'#安装测试脚本的apk
    #runUiautomatorApp(file,apk).runApp(times=2000)
    runUiautomatorApp(file, apk,key=10086,phonenumber=10000).runApp()



