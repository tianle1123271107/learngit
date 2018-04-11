# 用Python来编写脚本简化日常的运维工作是Python的一个重要用途。在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如ps，top，free等等。
# 要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。
#
# 在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，
# 它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。

# 获取CPU信息
# 我们先来获取CPU的信息：
import psutil
# print(psutil.cpu_count())# CPU逻辑数量
# print(psutil.cpu_count(logical=False))# CPU物理核心  # 2说明是双核超线程, 4则是4核非超线程

# 统计CPU的用户／系统／空闲时间：
# print(psutil.cpu_times())


# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
# for x in range(10):
#     print(psutil.cpu_percent(interval=1,percpu=True))
# cpu_percent#每秒
#interval 时间间隔
#percpu 每cup
# 获取内存信息
# 使用psutil获取物理内存和交换内存信息，分别使用：
# print(psutil.virtual_memory())
# print(psutil.swap_memory())
# # 返回的是字节为单位的整数，可以看到，总内存大小是8589934592 = 8 GB，已用=4260409344= 4.2GB，使用了50.3%。
# # 而交换区大小是25541652480 = 2.5 GB。
#
# # 交换内存:打个比方：你的内存（主仓库）放满了，就临时把内存（主仓库）暂时不用的东西放到硬盘里（副仓库），这样内存（主仓库）可以放新的东西。如果要用旧的东西再从硬盘里（副仓库）搬回来
#
#
# # 获取磁盘信息(电脑磁盘)
# # 可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：
# print(psutil.disk_partitions())# 磁盘分区信息
# print(psutil.disk_usage('C:\\'))# 磁盘使用情况
# print(psutil.disk_io_counters())# 磁盘IO
# 可以看到，磁盘'C:\\'的总容量是107375226880 = 100 GB，使用了37.1%。文件格式是NTFS，opts中包含rw表示可读写


# 获取网络信息
# psutil可以获取网络接口和网络连接信息：
# print(psutil.net_io_counters())# 获取网络读写字节／包的个数
# print(psutil.net_if_addrs())# 获取网络接口信息
# print(psutil.net_if_stats()) # 获取网络接口状态


# 要获取当前网络连接信息，使用net_connections()：
# print(psutil.net_connections())

# 获取进程信息
# 通过psutil可以获取到所有进程的详细信息：
# print(psutil.pids()) # 所有进程ID
# # print(psutil.Process(3800))#获取指定进程ID=3800的基本信息，其实就是360sd.exe'
# p=psutil.Process(1900)
print(p.name())# 进程名称
# print(p.exe())#进程exe路径
# print(p.cwd())# 进程工作目录
# print(p.cmdline())# 进程启动的命令行
# print(p.ppid())#查看父进程ID
# print(p.parent())#查看父进程
# print(p.children())#查看子进程
# print(p.status())#查看进程状态
# print(p.username())#进程用户名
# print(p.create_time())#进程创建时间
# print(p.memory_info())# 进程使用的内存
# print( p.open_files())# 进程打开的文件
# print(p.connections()) # 进程相关网络连接
# print(p.num_threads())# 进程的线程数量
# print(p.threads())# 所有线程信息
# print(p.environ()) # 进程环境变量

# 和获取网络连接类似，获取一个root用户的进程需要root权限，启动Python交互环境或者.py文件时，需要sudo权限。
# psutil还提供了一个test()函数，可以模拟出ps命令的效果：
# print(psutil.test())
# USER         PID %MEM     VSZ     RSS TTY           START    TIME  COMMAND
# SYSTEM         0    ?       ?      24 ?             10:44   31:01  System Idle Process
# SYSTEM         4    ?     124     368 ?             10:44   05:26  System
#              160  0.2    7604   14356 ?             10:44   00:03  svchost.exe
#              324    ?     552    1236 ?             10:44   00:00  smss.exe
#              360  0.5   24464   39388 ?             10:44   00:17  svchost.exe
#              504  0.1    2800    5756 ?             10:44   00:00  csrss.exe
#              552  0.1    1816    5352 ?             10:44   00:00  wininit.exe
#              576  0.9    3420   76676 ?             10:44   00:14  csrss.exe
#              640  0.1    5108    9348 ?             10:44   00:03  services.exe
#              648  0.1    3508    8516 ?             10:44   00:00  winlogon.exe
#              676  0.2    5288   13260 ?             10:44   00:10  lsass.exe
#              680  0.1    3244    8180 ?             10:44   00:00  svchost.exe
#              688  0.1    2556    4592 ?             10:44   00:00  lsm.exe
#              784  0.1    4520   10216 ?             10:44   00:03  svchost.exe
# Administra   812  0.1    3788   11620 ?             11:46   00:00  helputility.exe
#              860  0.1    4872    9168 ?             10:44   00:00  svchost.exe
#              944  0.2   17680   20192 ?             10:44   00:09  svchost.exe
#              984  2.6  210104  215908 ?             10:44   01:29  svchost.exe
#             1064  0.1    2020    7164 ?             10:44   00:00  igfxCUIService.exe
#             1164  0.7   44980   54132 ?             10:44   00:04  ZhuDongFangYu.exe
#             1176  0.6   53428   50360 ?             10:45   00:33  SearchIndexer.exe
#             1228  0.2   14628   16136 ?             10:44   00:04  svchost.exe
#             1248  1.9  174028  160952 ?             10:45   00:00  mysqld.exe
#             1400  0.1    6096   12236 ?             10:44   00:00  spoolsv.exe
#             1428  0.1    9068    9120 ?             10:44   00:00  svchost.exe
#             1524  0.1    4748    9944 ?             10:44   00:00  svchost.exe
#             1544  0.4   24400   36512 ?             10:44   00:10  Connect.Service.ContentService.exe
#             1572  0.2   18184   19240 ?             10:44   00:00  jenkins.exe
# Administra  1612    ?   16880    4108 ?             10:44   00:13  360wpsrv.exe
# Administra  1664  0.1    2512    6844 ?             10:44   00:00  taskeng.exe
# Administra  1716  0.1    2932    8196 ?             10:48   00:00  chrome.exe
# Administra  1748  0.1    3760    5000 ?             11:00   00:09  fsnotifier64.exe
# Administra  1768  0.5   29452   44380 ?             10:44   01:39  dwm.exe
# Administra  1828  1.4   60912  118972 ?             10:44   02:08  explorer.exe
# Administra  1840  0.2   13060   14972 ?             10:44   00:02  taskhost.exe
# Administra  1900  1.9  108016  155692 ?             10:48   06:03  chrome.exe
#             2000  0.1    5412   10344 ?             10:44   00:00  svchost.exe
#             2036  0.3   11944   23796 ?             10:44   01:20  svchost.exe
#             2084  0.3   27568   20888 ?             10:45   00:00  PresentationFontCache.exe
#             2088  0.2   18764   18380 ?             10:45   00:01  QQProtect.exe
#             2100  2.0  176124  166836 ?             10:45   00:15  java.exe
#             2220  0.1    1492    4692 ?             10:45   00:00  conhost.exe
#             2224  0.2    6320   13012 ?             10:45   01:25  WmiPrvSE.exe
#             2284  0.2    6616   18252 ?             10:45   00:00  TeamViewer_Service.exe
#             2376  0.1    6628   11444 ?             10:45   00:00  svchost.exe
#             2404  0.2    8988   17264 ?             10:45   00:27  svchost.exe
#             2816  0.1    6952    9292 ?             10:45   00:00  dllhost.exe
# Administra  2892    ?   10568    2628 ?             10:45   00:01  guardhp.exe
# Administra  3060  0.4   14228   30336 ?             10:53   01:14  SogouCloud.exe
# Administra  3236    ?    7956    1736 ?             10:47   00:01  NavPlugin.exe
# Administra  3388  1.2   71608  101516 ?             11:01   03:21  chrome.exe
# Administra  3412  0.1   14868   11040 ?             10:45   00:00  RtkNGUI64.exe
# Administra  3636  0.5  137928   39044 ?             10:45   01:21  360tray.exe
# Administra  3644  1.0   56292   83440 ?             10:45   00:43  baidunetdisk.exe
# Administra  3660  0.1    6232   11924 ?             10:45   00:00  yundetectservice.exe
# Administra  3676  1.3   61740  105948 ?             10:45   00:46  WeChat.exe
# Administra  3724  0.5   31704   39424 ?             11:09   00:07  QQExternal.exe
# Administra  3800    ?   37868    2192 ?             10:45   00:02  360sd.exe
#             4052  0.1    1896    5936 ?             10:45   00:00  svchost.exe
# Administra  4144  0.1    4392    8396 ?             10:48   00:00  chrome.exe
# Administra  4176  1.9   83984  155784 ?             10:48   04:47  chrome.exe
# Administra  4208  0.6   67164   47292 ?             10:48   01:17  ThunderPlatform.exe
# Administra  4268  0.1    4292   11488 ?             10:45   00:00  igfxEM.exe
# Administra  4560    ?   52688    2348 ?             10:46   00:29  wpscloudsvr.exe
# Administra  4724  3.9  243992  322800 ?             10:45   04:47  TIM.exe
# Administra  4848  0.1   28508   11264 ?             10:45   00:38  ComputerZTray.exe
# Administra  4888    ?    2472    2592 ?             10:45   00:00  TXPlatform.exe
#             5096  0.1    4404    8108 ?             10:45   00:15  SearchProtocolHost.exe
#             5280  0.1    3080    6872 ?             10:47   00:05  svchost.exe
# Administra  5496  1.1   80112   90076 ?             10:48   02:35  chrome.exe
# Administra  5500  0.4   44268   33952 ?             10:46   00:56  360rp.exe
# Administra  5528  0.3   26012   20740 ?             10:46   00:02  WeChatWeb.exe
# Administra  5564    ?    1628    4004 ?             14:54   00:00  conhost.exe
# Administra  6340    ?    9332    2092 ?             10:46   00:34  ComputerZService.exe
# Administra  6404  0.2    6500   19860 ?             10:47   00:14  wpscenter.exe
# Administra  6464  0.5   37768   38984 ?             10:49   01:07  360se.exe
# SYSTEM      6536  0.1    3656    8616 ?             14:53   00:00  SearchFilterHost.exe
# Administra  6604    ?    3796     528 ?             10:47   00:00  MobileDeviceSrv.exe
# Administra  6696  1.1   58164   93660 ?             10:49   01:33  360se.exe
# Administra  6796  0.7   44332   57920 ?             11:15   00:04  chrome.exe
# Administra  6932  0.2   10340   14064 ?             10:49   00:00  wdswfsafe.exe
# Administra  7244  0.4   27032   29744 ?             10:49   00:00  360se.exe
# Administra  7280  1.1   63312   90908 ?             11:42   00:20  chrome.exe
# Administra  7508  7.7  671072  638200 ?             10:59   08:13  pycharm64.exe
# Administra  7732    ?    1608    3980 ?             11:00   00:00  conhost.exe
# Administra  7780  1.0   77820   84688 ?             10:49   03:59  360se.exe
# Administra  8140  0.1    1992    7552 ?             11:40   00:00  notepad.exe
# Administra  9040  0.2    8896   13616 ?             14:54   00:00  python.exe


# psutil使得Python程序获取系统信息变得易如反掌。
# psutil还可以获取用户信息、Windows服务等很多有用的系统信息，具体请参考psutil的官网：https://github.com/giampaolo/psutil