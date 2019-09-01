import psutil

#获取CPU信息
# @staticmethod
def GetCpuInfo():
    cpu_count = psutil.cpu_count(logical=False)  #1代表单核CPU，2代表双核CPU  
    xc_count = psutil.cpu_count()                #线程数，如双核四线程
    cpu_slv = round((psutil.cpu_percent(1)), 2)  # cpu使用率
    list = [cpu_count,xc_count,cpu_slv]
    return list

#获取内存信息
# @staticmethod
def GetMemoryInfo():
    memory = psutil.virtual_memory()
    total_nc = round(( float(memory.total) / 1024 / 1024 / 1024), 2)  # 总内存
    used_nc = round(( float(memory.used) / 1024 / 1024 / 1024), 2)  # 已用内存
    free_nc = round(( float(memory.free) / 1024 / 1024 / 1024), 2)  # 空闲内存
    syl_nc = round((float(memory.used) / float(memory.total) * 100), 2)  # 内存使用率
 
    ret_list = [total_nc,used_nc,free_nc,syl_nc]
    return ret_list

#获取硬盘信息
# @staticmethod
def GetDiskInfo():
    list = psutil.disk_partitions() #磁盘列表
    ilen = len(list) #磁盘分区个数
    i=0
    retlist1=[]
    retlist2=[]
    while i< ilen:
        diskinfo = psutil.disk_usage(list[i].device)
        total_disk = round((float(diskinfo.total)/1024/1024/1024),2) #总大小
        used_disk = round((float(diskinfo.used) / 1024 / 1024 / 1024), 2) #已用大小
        free_disk = round((float(diskinfo.free) / 1024 / 1024 / 1024), 2) #剩余大小
        syl_disk = diskinfo.percent
 
        retlist1=[i,list[i].device,total_disk,used_disk,free_disk,syl_disk]  #序号，磁盘名称，
        retlist2.append(retlist1)  
        i=i+1
 
    return retlist2

def GetProcessInfo():
    retlist = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
        except psutil.NoSuchProcess:
            pass
        else:
            retlist.append(pinfo)

    return retlist    
        # print(pinfo)

print(GetCpuInfo())    
print(GetMemoryInfo())    
print(GetDiskInfo())    
for item in GetProcessInfo():
    print(item)