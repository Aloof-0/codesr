# 1.cd  切换目录
'''


cd  # 回到当前用户的家目录
# ～  可用于表示用户家目录
cd  /etc # 切换到/etc目录

cd -
# 切换到上一次的目录
cd /tmp 切换到tmp目录下
cd 进入用户主目录；
cd ~ 进入用户主目录；
cd - 返回进入此目录之前所在的目录；
cd .. 返回上级目录；
cd ../.. 返回上两级目录；
cd !$ 把上个命令的参数作为cd参数使用。

'''

# 2.touch  创建文件  touch ： 改变文件或目录的时间，文件不存在时会创建一个空文件。
'''
touch file1 # file1 不存在时被创建
touch -c file1 # 不创建文件
touch -r ref_file file1  更新file1.txt的时间戳和ref+file相同
touch -t 201210120505.25 file1

#  -t  time 使用指定的时间值 time 作为指定文件相应时间戳记的新值．此处的 # # time规定为如下形式的十进制数:      
#  [[CC]YY]MMDDhhmm[.SS]     
#   这里，CC为年数中的前两位，即”世纪数”；YY为年数的后两位，即某世纪中的年数．如果不给出CC的值，则touch  
 将把年数CCYY限定在1969--2068之内．MM为月数，DD为天将把年数CCYY限定在1969--2068之内．MM为月数，DD为天数
 ，hh 为小时数(几点)，mm为分钟数，SS为秒数．此处秒的设定范围是0--61，这样可以处理闰秒．
 这些数字组成的时间是环境变量TZ指定的时区中的一个时 间．由于系统的限制，早于1970年1月1日的时间是错误的。
'''

# 3.man  获取帮助
'''
man man  # 查看man命令的手册  
man  cd 
man  pwd 
man 5 passwd
man -k passwd # 模糊查找
man -f  passwd  # 精确查找 
'''

# 4.mkdir     用来创建目录，要求创建目录的用户在当前目录中具有写权限，并且指定的目录名不能是当前目录中已有的目录。
'''
　　使用帮助命令：man mkdir或mkdir -help
　　-m --mode=模式，设定权限<模式> (类似 chmod)，而不是 rwxrwxrwx 减 umask
  　-p --parents 递归创建目录
　　-v, --verbose 每次创建新目录都显示信息
　　　  --help 显示此帮助信息并退出
　　    --version 输出版本信息并退出
'''

# 5.rm      Remove，功能：1）删除目录，2）删除文件。
"""
-f：不提示，强制删除文件或目录；
-i：删除已有文件或目录之前先询问用户；
-r,-R：递归删除，将指定目录下的所有文件与子目录一并删除；
-v：显示指令的详细执行过程。

rm -f  file1 # 强制删除文件
rm -r  a/b/file1  # 删除指定目录及其下的所有文件和目录
rm -rf  a/b/file1  #  强制删除指定目录及其下的所有文件和目录
rmdir (目录) 删除空目录
"""

# 6.mv   移动或重命令文件或目录
"""
-b ：若需覆盖文件，则覆盖前先行备份。 
-f ：force 强制的意思，如果目标文件已经存在，不会询问而直接覆盖；
-i ：若目标文件 (destination) 已经存在时，就会询问是否覆盖！
-u ：若目标文件已经存在，且 source 比较新，才会更新(update)
    -t  ： --target-directory=DIRECTORY move all SOURCE arguments into DIRECTORY，
           即指定mv的目标目录，该选项适用于移动多个源文件到一个目录的情况，此时目标目录在前，源文件在后。

mv test.log test.txt  # 文件改名
mv test1.txt dir1/      #移动文件
mv test1.txt  test2.tx  test3.tx dir1/      #移动多个文件
"""

# 7.cp ： 复制
'''
cp SOURCE DEST # 复制文件

cp -i  SOURCE DEST  #   如果遇到需要覆盖的情况，则提示
cp -r  dir1  dir2  # 若给出的源文件是一目录文件，此时cp将递归复制该目录下所有的子目录和文件。此时目标文件必须为一个目录名
cp -p  file1 file2  #  此时cp除复制源文件的内容外，还将把其修改时间和访问权限也复制到新文件中。
cp -rp dir1  dir2
'''