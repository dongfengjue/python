import subprocess
# linux 调用默认打开文件
file_path = "/Users/chenbing/Documents/file/1.mp3"
# subprocess.call(["open", file_path])

cmd = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome /Users/chenbing/Documents/file/1.mp3"
# subprocess.call(cmd, shell=True) 

# adb 连接手机 控制adb命令 控制手机
adbShell = 'adb shell input keyevent 82'
subprocess.call(adbShell, shell=True) 
