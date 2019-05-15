import subprocess
import time
import logging


class runUiautomatorApp(object):
    """Classes are used to control Uiautomator script,

     Install script to phone,Get return information during execution, Transfer parameters to the script, Add permissions to the script app
    Attributes:
        file: Save the LOG file for execution and return information
        apk: Uiautomator script to be installed
        **kwargs: Incoming script parameters
    """
    def __init__(self,file,apk,**kwargs):
        """Incoming parameter initialization,Open the file that stores the returned information"""
        self.file = file
        self.apk = apk
        self.kwargs = kwargs

        self.adb_rm = ['adb','shell','rm','-r','/storage/emulated/0/log.txt']
        self.adb_push =['adb','push',self.apk,'/data/local/tmp/com.example.jennyhe.mytest']
        self.adb_install = ['adb','shell','pm','install','-t','-r','/data/local/tmp/com.example.jennyhe.mytest']

        self.adb_readper = ['adb', 'shell', 'pm', 'grant', 'com.example.jennyhe.mytest', 'android.permission.READ_EXTERNAL_STORAGE']
        self.adb_writeper = ['adb', 'shell', 'pm', 'grant', 'com.example.jennyhe.mytest', 'android.permission.WRITE_EXTERNAL_STORAGE']  # 通过adb 给予读写外部存储卡的权限



        self.f = open(file, 'w')
        if self.kwargs:
            list =[]
            for arg, value in kwargs.items():
                list.append('-e')
                list.append(arg)
                list.append(str(value))
            print(list)
            self.agr = list
            self.adb_run = ['adb', 'shell', 'nohup', 'am', 'instrument', '-w', '-r', '-e', 'package',
                            'com.example.jennyhe.mytest', '-e', 'debug', 'false'] + self.agr + [
                               'com.example.jennyhe.mytest.test/android.support.test.runner.AndroidJUnitRunner', '2>&1',
                               '|tee', '-a', '/storage/emulated/0/log.txt']  # 传入参数的adb命令
        else:
            self.adb_run = ['adb', 'shell', 'nohup', 'am', 'instrument', '-w', '-r', '-e', 'package',
                            'com.example.jennyhe.mytest', '-e', 'debug', 'false'] + [
                               'com.example.jennyhe.mytest.test/android.support.test.runner.AndroidJUnitRunner', '2>&1',
                               '|tee', '-a', '/storage/emulated/0/log.txt']  # 不传入参数的adb命令

    def subproc(self,command):
        """Create a child process and save the returned results in a file

        Args:
            command:Incoming adb command
        :return:
        """
        if not isinstance(command, list):
            command = command.split()
        subprocess.Popen(command,stdout = self.f.fileno(), stderr = self.f.fileno()).wait()
        self.f.flush()
    def initApp(self):
        """Install the uiautomator script

        Args:
        :return:
        """
        self.subproc(self.adb_rm)
        self.subproc(self.adb_push)
        self.subproc(self.adb_install)
    def getpermission(self):
        """Give uiautomator script apk plus permissions

        Args:
        :return:
        """
        self.subproc(self.adb_readper)
        self.subproc(self.adb_writeper)
    def runApp(self,times=None):
        """Run the script and save the results back in the file

        Args:
            times:Script execution times
        :return:
        """
        self.initApp()
        self.getpermission()
        if times:
            for self.i in range(1,times+1):
                print("第%i轮测试"%self.i, file=self.f)
                self.f.flush()
                time.sleep(1)
                self.subproc(self.adb_run)
        self.f.close()

if __name__ == "__main__":
    file = "runApp.log" #存储返回值的文件
    #apk = 'Uiautomator_file.apk'#安装测试脚本的apk
    apk = 'Uiautomator.apk'  # 安装测试脚本的apk
    runUiautomatorApp(file,apk).runApp(times=800)
    #RunUiautomatorApp(file, apk,key=10086,phonenumber='10000').runApp()
    #runUiautomatorApp(file, apk).runApp(times=5)

