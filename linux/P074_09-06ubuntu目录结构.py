# 1.linux没有文件夹 只有目录;linux一切皆文件

# 2.ubuntu  的ls 命令
'''
(1). ls，列出当前目录的内容

(2). ls /，显示根目录的内容

(3). ls -a，显示隐藏的目录和文件

(4). ls -l，显示文件的详细信息，文件目录具有的权限，当前权限文件的数量，拥有者，所属的群组，文件目录的大小，创建或者修改时间，文件目录的名字。可以使用ls -la

(5). ls -ld，查看当前目录的属性

(6). ls -lh，翻译成更加直观的感受。
'''

# 3.LInux目录结构：
'''
/ ： 所有目录都在
/boot : boot 配置文件、内核和其它启动 时所需的文件
/etc ： 存放系统配置有关的文件
/home ： 存放普通用户目录
/mnt ： 硬盘上手动 挂载的文件系统
/media ： 自动挂载（加载）的硬盘分区以及类似CD、数码相机等可移动介质。
/cdrom ： 挂载光盘？ 
/opt ： 存放一些可选程序,如某个程序测试版本,安装到该目录的程序的所有数据,库文件都存在同个目录下
/root ： 系统管理员的目录，对于系统来说，系统管理员好比上帝，他可以对系统做任何操作，比如删除你的文件，一般情况下不要使用root用户。
/bin ： 存放常用的程序文件（命令文件）。
/sbin ： 系统管理命令，这里存放的是系统管理员使用的管理程序 
/tmp ： 临时目录，存放临时文件，系统会定期清理该目录下的文件。
/usr ： 在这个目录下，你可以找到那些不适合放在/bin或/etc目录下的额外的工具。比如游戏、打印工具等。/usr目录包含了许多子目录： /usr/bin目录用于存放程序;/usr/share用于存放一些共享的数据，比如音乐文件或者图标等等;/usr/lib目录用于存放那些不能直接 运行的，但却是许多程序运行所必需的一些函数库文件。/usr/local ： 这个目录一般是用来存放用户自编译安装软件的存放目录；一般是通过源码包安装的软件，如果没有特别指定安装目录的话，一般是安装在这个目录中。
　　　　/usr/bin/ 非必要可执行文件 (在单用户模式中不需要)；面向所有用户。
　　　　/usr/include/ 标准包含文件。
　　　　/usr/lib/ /usr/bin/和/usr/sbin/中二进制文件的库。
　　　　/usr/sbin/ 非必要的系统二进制文件，例如：大量网络服务的守护进程。
　　　　/usr/share/ 体系结构无关（共享）数据。
　　　　/usr/src/ 源代码,例如:内核源代码及其头文件。
　　　　/usr/X11R6/ X Window系统 版本 11, Release 6.
　　　　/usr/local/ 本地数据的第三层次， 具体到本台主机。通常而言有进一步的子目录， 例如：bin/、lib/、share/.

/var ： 该目录存放那些经常被修改的文件，包括各种日志、数据文件；
/var/cache/ 应用程序缓存数据。这些数据是在本地生成的一个耗时的I/O或计算结果。应用程序必须能够再生或恢复数据。缓存的文件可以被删除而不导致数据丢失。
/var/lib/ 状态信息。 由程序在运行时维护的持久性数据。 例如：数据库、包装的系统元数据等。
/var/lock/ 锁文件，一类跟踪当前使用中资源的文件。
/var/log/ 日志文件，包含大量日志文件。
/var/mail/ 用户的电子邮箱。
/var/run/ 自最后一次启动以来运行中的系统的信息，例如：当前登录的用户和运行中的守护进程。现已经被/run代替[13]。
/var/spool/ 等待处理的任务的脱机文件，例如：打印队列和未读的邮件。
/var/spool/mail/ 用户的邮箱(不鼓励的存储位置)
/var/tmp/ 在系统重启过程中可以保留的临时文件。
/lib : 目录是根文件系统上的程序所需的共享库，存放了根文件系统程序运行所需的共享文件。这些文件包含了可被许多程序共享的代码，以避免每个程序都包含有相同的子程序的副本，故可以使得可执行文件变得更小，节省空间。
/lib32 : 同上
/lib64 ： 同上
/lost+found ： 该目录在大多数情况下都是空的。但当突然停电、或者非正常关机后，有些文件就临时存放在；
/dev : 存放设备文件
/run ： 代替/var/run目录，
/proc : 虚拟文件系统，可以在该目录下获取系统信息，这些信息是在内存中由系统自己产生的，该目录的内容不在硬盘上而在内存里；
/sys ： 和proc一样，虚拟文件系统，可以在该目录下获取系统信息，这些信息是在内存中由系统自己产生的，该目录的内容不在硬盘上而在内存里；
'''

# 4.apt命令:apt 是一个软件包管路器,它会自动到网站下载相应的软件包 进行安装 相当与360软件管家,不过是字符界面
'''
apt 命令	          取代的命令	                      命令的功能
apt install	        apt-get install	                安装软件包
apt remove	        apt-get remove                  移除软件包
apt purge	        apt-get purge	                移除软件包及配置文件
apt update	        apt-get update	                刷新存储库索引
apt upgrade	        apt-get upgrade	                升级所有可升级的软件包
apt autoremove	    apt-get autoremove              自动删除不需要的包
apt full-upgrade	apt-get dist-upgrade	        在升级软件包时自动处理依赖关系
apt search	        apt-cache search	            搜索应用程序
apt show	        apt-cache show	                显示装细节

apt-cache search package 搜索包
apt-cache show package 获取包的相关信息，如说明、大小、版本等
sudo apt-get install package 安装包
sudo apt-get install package –reinstall 重新安装包
sudo apt-get -f install 强制安装
sudo apt-get remove package 删除包
sudo apt-get remove package –purge 删除包，包括删除配置文件等
sudo apt-get autoremove 自动删除不需要的包
sudo apt-get update 更新源
sudo apt-get upgrade 更新已安装的包
sudo apt-get dist-upgrade 升级系统
sudo apt-get dselect-upgrade 使用 dselect 升级
apt-cache depends package 了解使用依赖
apt-cache rdepends package 了解某个具体的依赖
sudo apt-get build-dep package 安装相关的编译环境
apt-get source package 下载该包的源代码
sudo apt-get clean && sudo apt-get autoclean 清理下载文件的存档
sudo apt-get check 检查是否有损坏的依赖
'''

# 5.sudo命令:试用管理员权限干事 是指用管理员ROOT运行这个命令

# 6.date 日期的用法
'''
1.sudo date 查看时间

2.转换格式： sudo date +"%y_%m_%d"                输出:   年_月_日
            sudo  date +"%y_%m_%d %H:%M:%S"      输出:   年_月_日  时:分:秒
         
        注: 1.%y 年   %m 月   %d 日     
            2._之是格式 用什么符号去替代它都可以,如:/ 、 |   

3.设置时间: sudo date-s
          1.sudo date -s 20110314 //先修改年月日
          2.sudo date -s 21:30 //在修改时分
          sudo date -s MM/DD/YY //修改日期
          sudo date -s hh:mm:ss //修改时间
                  
4.
 %%    一个文字的 %
  %a    当前locale 的星期名缩写(例如： 日，代表星期日)
  %A    当前locale 的星期名全称 (如：星期日)         
  %b    当前locale 的月名缩写 (如：一，代表一月)     
  %B    当前locale 的月名全称 (如：一月)             
  %c    当前locale 的日期和时间 (如：2005年3月3日 星期四 23:05:25)
  %C    世纪；比如 %Y，通常为省略当前年份的后两位数字(例如：20)   
  %d    按月计的日期(例如：01)                                   
  %D    按月计的日期；等于%m/%d/%y                               
  %e    按月计的日期，添加空格，等于%_d                           
  %F    完整日期格式，等价于 %Y-%m-%d                             
  %g    ISO-8601 格式年份的最后两位 (参见%G)                     
  %G    ISO-8601 格式年份 (参见%V)，一般只和 %V 结合使用         
  %h    等于%b                                                   
  %H    小时(00-23)                                               
  %I    小时(00-12)                                               
  %c    按年计的日期(001-366)                                     
  %k    时(0-23)                                                 
  %l    时(1-12)                                                 
  %m    月份(01-12)                                               
  %M    分(00-59)                                                 
  %n    换行                                                     
  %N    纳秒(000000000-999999999)                                 
  %p    当前locale 下的"上午"或者"下午"，未知时输出为空           
  %P    与%p 类似，但是输出小写字母                               
  %r    当前locale 下的 12 小时时钟时间 (如：11:11:04 下午)       
  %R    24 小时时间的时和分，等价于 %H:%M                         
  %s    自UTC 时间 1970-01-01 00:00:00 以来所经过的秒数           
  %S    秒(00-60)                                                 
  %t    输出制表符 Tab                                           
  %T    时间，等于%H:%M:%S                                       
  %u    星期，1 代表星期一                                       
  %U    一年中的第几周，以周日为每星期第一天(00-53)
  %V    ISO-8601 格式规范下的一年中第几周，以周一为每星期第一天(01-53)
  %w    一星期中的第几日(0-6)，0 代表周一
  %W    一年中的第几周，以周一为每星期第一天(00-53)
  %x    当前locale 下的日期描述 (如：12/31/99)
  %X    当前locale 下的时间描述 (如：23:13:48)
  %y    年份最后两位数位 (00-99)
  %Y    年份
  %z +hhmm              数字时区(例如，-0400)
  %:z +hh:mm            数字时区(例如，-04:00)
  %::z +hh:mm:ss        数字时区(例如，-04:00:00)
  %:::z                 数字时区带有必要的精度 (例如，-04，+05:30)
  %Z                    按字母表排序的时区缩写 (例如，EDT) 

date -s //设置当前时间，只有root权限才能设置，其他只能查看。
date -s 20061010 //设置成20061010，这样会把具体时间设置成空00:00:00
date -s 12:23:23 //设置具体时间，不会对日期做更改
date -s “12:12:23 2006-10-10″ //这样可以设置全部时间

# 注意： 重新设置时间后需要将时间捅不到硬件时钟。方式如下：
hwclock -w    

'''

# 7.cal  日历得用法
'''
1.cal -y   查看今年的日历

2.cal 2015 查看2015的日历

3.
-1 显示一个月的月历
-3 显示系统前一个月，当前月，下一个月的月历
-s  显示星期天为一个星期的第一天，默认的格式
-m 显示星期一为一个星期的第一天
-j  显示在当年中的第几天（一年日期按天算，从1月1号算起，默认显示当前月在一年中的天数）
-y  显示当前年份的日历
'''

# 8.tzselect 查看时区
'''
1.查看时区 root@ubuntu:/# date -R   

2.修改时区 sudo tzselect

3.
GMT 格林威治标准时间 GMT 
UTC 全球标准时间 GMT 
ECT 欧洲中部时间 GMT+1:00 
EET 东欧时间 GMT+2:00 
ART （阿拉伯）埃及标准时间 GMT+2:00 
EAT 东非时间 GMT+3:00 
MET 中东时间 GMT+3:30 
NET 近东时间 GMT+4:00 
PLT 巴基斯坦拉合尔时间 GMT+5:00 
IST 印度标准时间 GMT+5:30 
BST 孟加拉国标准时间 GMT+6:00 
VST 越南标准时间 GMT+7:00 
CTT 中国台湾时间 GMT+8:00 
JST 日本标准时间 GMT+9:00 
ACT 澳大利亚中部时间 GMT+9:30 
AET 澳大利亚东部时间 GMT+10:00 
SST 所罗门标准时间 GMT+11:00 
NST 新西兰标准时间 GMT+12:00 
MIT 中途岛时间 GMT-11:00 
HST 夏威夷标准时间 GMT-10:00 
AST 阿拉斯加标准时间 GMT-9:00 
PST 太平洋标准时间 GMT-8:00 
PNT 菲尼克斯标准时间 GMT-7:00 
MST 西部山脉标准时间 GMT-7:00 
CST 中部标准时间 GMT-6:00 
EST 东部标准时间 GMT-5:00 
IET 印第安那东部标准时间 GMT-5:00 
PRT 波多黎各和美属维尔京群岛时间 GMT-4:00 
CNT 加拿大纽芬兰时间 GMT-3:30 
AGT 阿根廷标准时间 GMT-3:00 
BET 巴西东部时间 GMT-3:00 
CAT 中非时间 GMT-1:00
'''

# 9.～S 是你的用户主目录，它等于 ：home/<你的用户名>/
'''
ubuntu是你的设备名，也就是你安装ubuntu的设备，一般是你给你的电脑取得别名；
~：是你的用户主目录，它等于 ：home/<你的用户名>/
$：表明你在普通用户模式下，而非root用户
#：表明你现在为root用户


'''

# 10.注销/重启/关机
'''
 logout  # 注销
 reboot  # 重启系统： 需要管理员全新 
 shutdown # 关机： 需要管理员权限
shutdown -r now # 现在立即重启
shutdown -r +5  # 三分钟后重启
shutdown -r 12:12    #在12:12时将重启计算机

shutdown -h now # 现在立即关机
shutdown -h +5  “The System will shutdown after 3 minutes”   # 提示使用者将在三分钟后关机
shutdown -h +5   #  5分钟后关机
shutdown -h 12:00  # 12点钟关机
shutdown -c   # 取消关机操作

'''

