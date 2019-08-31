import subprocess
# linux 调用默认打开文件
file_path = "/Users/chenbing/Documents/file/1.mp3"
# subprocess.call(["open", file_path])

cmd = "/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome /Users/chenbing/Documents/file/1.mp3"
subprocess.call(cmd, shell=True) 