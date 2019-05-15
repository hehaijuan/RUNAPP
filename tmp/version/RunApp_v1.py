import subprocess
import time
import logging
def log():
    log_name ="log.log"
    logging.basicConfig(filename=log_name,level=logging.DEBUG,format="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
def runApp():
    """无参数无手机内部新建文件"""
    file = "runApp.log"
    f = open(file, 'w')
    cmd01 = 'adb push /Uiautomator.apk /data/local/tmp/com.example.jennyhe.mytest'
    cmd02 = 'adb shell pm install -g -t -r "/data/local/tmp/com.example.jennyhe.mytest"'
    #cmd03 = 'adb shell "am instrument -w -r   -e package com.example.jennyhe.mytest -e debug false com.example.jennyhe.mytest.test/android.support.test.runner.AndroidJUnitRunner"' #不能断开USB线adb命令
    cmd03 = 'adb shell "nohup am instrument -w -r   -e package com.example.jennyhe.mytest -e debug false com.example.jennyhe.mytest.test/android.support.test.runner.AndroidJUnitRunner 2>&1 |tee -a /storage/emulated/0/log.txt"' #不传入参数adb命令
    uiautomator_proc = subprocess.Popen(cmd01, shell=True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT) #将uiautomator.apk push到手机中
    uiautomator_proc.wait()
    uiautomator_proc = subprocess.Popen(cmd02, shell=True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT) #安装uiautomator.apk 到手机中
    uiautomator_proc.wait()
    for i in range(1000):
        logging.info("第%i测试",i)
        uiautomator_proc = subprocess.Popen(cmd03, shell=True,stdout = f.fileno(), stderr = f.fileno()) #执行测试脚本并将返回值存储在runApp.log文件中
        uiautomator_proc.wait()
    f.flush()
    f.close()
    time.sleep(20)
def runAppAgr():
    """有参数无手机内部新建文件"""
    file = "runAppAgr.log"
    f = open(file, 'w')
    cmd01 = 'adb push /Uiautomator_agr.apk /data/local/tmp/com.example.jennyhe.mytest'
    cmd02 = 'adb shell pm install -g -t -r "/data/local/tmp/com.example.jennyhe.mytest"'
    #cmd03 = 'adb shell "am instrument -w -r   -e package com.example.jennyhe.mytest -e debug false com.example.jennyhe.mytest.test/android.support.test.runner.AndroidJUnitRunner"' #不能断开USB线adb命令
    cmd03 = 'adb shell "nohup am instrument -w -r   -e package com.example.jennyhe.mytest -e debug false -e key 10086  com.example.jennyhe.mytest.test/android.support.test.runner.AndroidJUnitRunner 2>&1 |tee -a /storage/emulated/0/log.txt" ' #传入参数的adb命令
    uiautomator_proc = subprocess.Popen(cmd01, shell=True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT) #将uiautomator.apk push到手机中
    uiautomator_proc.wait()
    uiautomator_proc = subprocess.Popen(cmd02, shell=True,stdout = subprocess.PIPE, stderr = subprocess.STDOUT) #安装uiautomator.apk 到手机中
    uiautomator_proc.wait()
    for i in range(5):
        uiautomator_proc = subprocess.Popen(cmd03, shell=True, stdout=f.fileno(),stderr=f.fileno())  # 执行测试脚本并将返回值存储在runApp.log文件中
        uiautomator_proc.wait()
    f.flush()
    f.close()
    time.sleep(20)
def runAppFile():
    """无参数有手机内部新建文件"""
    file = "runApp_File.log"
    f = open(file, 'w')
    cmd01 = 'adb push /Uiautomator.apk /data/local/tmp/com.example.jennyhe.mytest'
    cmd02 = 'adb shell pm install -g -t -r "/data/local/tmp/com.example.jennyhe.mytest"'
    cmd021 = 'adb shell pm grant com.example.jennyhe.mytest android.permission.READ_EXTERNAL_STORAGE'
    cmd022 = 'adb shell pm grant com.example.jennyhe.mytest android.permission.WRITE_EXTERNAL_STORAGE'   #通过adb 给予读写外部存储卡的权限
    cmd03 = 'adb shell "nohup am instrument -w -r   -e package com.example.jennyhe.mytest -e debug false com.example.jennyhe.mytest.test/android.support.test.runner.AndroidJUnitRunner 2>&1 |tee -a /storage/emulated/0/log.txt"' #不传入参数adb命令
    uiautomator_proc = subprocess.Popen(cmd01, shell=True,stdout = f.fileno(), stderr = f.fileno()) #将uiautomator.apk push到手机中
    uiautomator_proc.wait()
    uiautomator_proc = subprocess.Popen(cmd02, shell=True,stdout = f.fileno(), stderr = f.fileno()) #安装uiautomator.apk 到手机中
    uiautomator_proc.wait()
    uiautomator_proc = subprocess.Popen(cmd021, shell=True, stdout=f.fileno(),stderr=f.fileno())
    uiautomator_proc.wait()
    uiautomator_proc = subprocess.Popen(cmd022, shell=True, stdout=f.fileno(),stderr=f.fileno())
    uiautomator_proc.wait()
    uiautomator_proc = subprocess.Popen(cmd03, shell=True,stdout = f.fileno(), stderr = f.fileno()) #执行测试脚本并将返回值存储在runApp.log文件中
    uiautomator_proc.wait()
    f.flush()
    f.close()
    time.sleep(20)
if __name__ == "__main__":
    log()
    #runApp()
    #runAppAgr()
    runAppFile()




