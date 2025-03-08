# 1\注释
# 这是单行注释

"""
this is for multiple lines
you can see everything between these are useless

(附加1.1)python 数据类型包括：
number (int float complex[复数] bool)
string
list(有序且可变)
tuple(有序且不可变)
set(无序不重复)
dictionary(无序的key-value)
"""

# !!!多行注释快捷键 ctrl+/

# 2\变量的定义
money = 50
money = money - 10
print("after shopping you have: ", money, "yuan")
print(type(money), end='')
# ”PYTHON“ 数据变量没有类型 type 用于查看数据类型
# print语句默认换行,想不换行需要在后面, end=''
print()
# 上面就是输出一个换行
print(type(str(money)))
money = money - 0.1
print(money)
print(type(money))
print(int(money))
# 我们可以看见float强制转化int为去尾

# 3\特殊符号的运算（在C++基础之上）
# 整除： //
print(11 // 2)
# 结果是5
# 求方
print(2**5)
# 前者为底数 后者为方

# 4\字符串的定义
# 4.1 python 可以使用''| "" | """ """ 都是等效的字符串类型 其中''里可以有"" 反之亦然
"\""
# 4.2 \转义字符,后接什么都无效

# 4.3 字符串的拼接：
# str类型可以直接用+相接
name = "Lin_eclipse"
money = 20394
# print("I am "+ name +money) # X:money 不是str类型
print("I am "+name+", and I have " + str(money)+" yuan")
"""
但这样过于麻烦了
我们不仅需要+和一堆""
我们还需要手动转换类型str
所以我们可以使用格式化
%s:传送门 %：传送门二号
%s 占位并转化str
%d 占位并转化整型
%f 占位并转化浮点型
"""
print("I am %s, and I have %d yuan" % (name, money))
"""
4.4字符串%格式化精度的控制
% a.bf 
%5.2f: 占位5格，小数精确到2位（都是四舍五入）
如果占位小于数字位数，则不生效
% .2f:小数精确到2位（都是四舍五入）

4.5快速格式化（不限类型、无精度控制）[常用]

"""
print(f"I am {name}, and I have {money} yuan")

# 5\ 输入
"""
a = input("提示信息")
注意：默认的输入皆为字符串str类型，我们需要去强制转化类型
"""

# 6\逻辑判断之bool
# 比较运算式子作为变量该类型自动为bool
# 变量= True 、 False 自动为bool
# 7\ if else 等 python 语法 ！！if not 是python中如果不的表达
"""
if 判断条件:  # 注意条件一定是bool
    成立时的操作1
    ...2 （也就是说操作都需要空四个格对齐）
其余代码...
"""
money = int(input("please tell me your money:"))
if money >= 1000000:
    print(f"{name} is a millionaire ")
elif money >= 10000 & money <= 500000:
    print(f"{name} has some money but not rich")
elif money < 1000000 & money > 500000:
    print(f"{name} is a little rich")
else:
    print(f"{name} is just a poor wretch ")
# 判断语句可以直接嫁接到input语句 例如：int(input("请输入你的vip级别(1~5):")) < 1204

# 7\循环while for
"""
7.1 while
while 判断条件:
    满足的操作1
    ...2
其余代码...
7.2 for
for 临时变量 in 数据集:
    循环满足时的代码
python中for无法定义循环条件
"""
print("No matter I am rich or not,you'd remember that my name is ", end='')
for x in name:
    print(f"{x}", end=' ')
    print()
# ''里面打空格可以空出来格
# 7.3 range语句(就是一个取数字的函数罢了)
"""
不包含最后的数字!!
range(num):0<=x<num每个整数
range(num1,num2)num1<=x<num2每个整数
range(num1,num2,step)num1<=x<num2从num1开始每step选取一个整数
临时用法: for i in range(num): 来进行循环
"""
# 7.4 break continue
# continue终止本次循环,进入下次循环
# break终止紧贴层所有循环

# 8\python的函数
# 8.1常用内置函数 type() len() exit()
count = len("abbr")
print(count)

# 8.2函数基本语法
"""
def 函数名 （传入参数1，传入参数2）:
    函数体
    return 返回值
注意：当没有返回东西的时候，会返回None，等同于False
注意：!外部的全局变量想要用到函数里面并且能修改，需要在函数内声明
global 全局变量名
"""

# 9\python容器入门
"""
9.1 list
9.1.1定义列表
列表名称=[] or 列表名称 = list()
"""
name_list = ['任星宇', "王泓嘉", "邵新宇", 4, True]
# 元素类型不限,单双引号都行
school = [['天津大学', '东北大学'], ['华南理工大学', '沈阳理工大学']]
# 嵌套列表
# 9.1.2 下标访问：比如我要访问华南理工大学
print(school[1][0])
# 9.1.3列表常用操作
"""
查询列表下标
列表名.index(元素)

修改值操作
赋值替换就行

清空列表操作
列表名.clear()

插入值操作
列表名.insert(位置下标,值)

追加（在末尾）值操作[可以是一个元素，也可以是一个容器]
列表名.extend(追加的)

删除操作（指定下标）
列表名.pop(下标)

删除操作（指定值）
列表名.remove(值)

统计某元素数量
列表名.count()

统计总元素个数
len(列表名)
"""
school.index(['华南理工大学', '沈阳理工大学'])
print(school)
school.insert(1, ['北京理工大学', '华中科技大学'])
print(school)
school.extend([['华东政法大学', '华西医科大学']])
school.extend([['武汉大学'], ['华中医科大学']])
print(school)
del_school = school.pop(3)
print(f"{school},被除名的大专是{del_school}")
school.remove(['武汉大学'])
print(f"{school},这次又有哪所大专不见了呢？")
print(school.count('大学'))
# 没有叫大学的元素
school_num = len(school)
print(f"共计有{school_num}所神秘大学联盟")
school.clear()
# 9.1.4 列表的遍历
"""
while 遍历：

index = 0
while index < len(列表名)
 元素名 = 列表名[index]
 (处理元素操作)
 index += 1
 
 for 更加适合（不限定循环条件的情况）：
 
 for 临时变量 in 数据容器名
 (处理临时变量操作)
"""
# 9.2 元组tuple(与列表的差异是定义完成不可修改，为只读list)
# 其中元组的语法与list不同的就是把框住元素的[]换成了() str换成了"" set换成了{}
tuple1 = ("元组",)
"""
元组虽然不可以修改，但元组中的list可以(嵌套)
访问：tuple[0]即可
元组名.index(元素内容) 会返回元素下标
元组名.count(元素内容) 会返回元素数量
len(元组)
遍历同列表遍历
"""
# 9.3\字符串
"""
不可修改
其访问可通过 字符串名[i]访问
但是有许多特殊功能的内置函数
字符串.index(元素内容) 会返回元素下标
字符串.replace(a,b)把字符串里面的a 换成 b 
"""
str1 = "I am your father1."
print(str1.index("a"))
# 首个a下标!
print(str1.replace("fa", "mo"))
"""
注意：上面的例子我想说明的是字符串可以分割的！
字符串.split(分隔符)
"""
new_str1 = str1.split(" ")
print(new_str1)
# replace以及split可以把字符串分隔开，进阶作为文件的读取: .remove(" ","|")  .split("|")

# 9.3附 切片
"""
序列可以是str list tuple 
序列名[起始下标:结束下标（不含它）:步长]
[::-1] :反转
"""

# 9.4set集合
"""
自带去重功能,且乱序
{}
"""
set1={"dad","mom","bro","sis","son","dau","unc","aun","bro","cou","sis"}
set2={"unc","aun","bro","cou","sis"}
print(set1)
"""
.add("...")添加
.remove("...")
.pop()list里面可以返回弹出内容、下标，但set无序，故只可以返回内容
.clear()
集合1.difference(集合2) 取二集合差集
集合1.difference_update(集合2)在集合1删除与集合2相同的（删除差集）
集合1.union(集合2) 二集合合并
len(集合名)

"""
set1.difference(set2)

# 9.5dict字典
# 用法:key-value(两两关联) 当key相同的时候，value后者覆盖前者
# {key:value, key:value}
my_dict = {}
my_dict = dict()
my_dict= {"爸爸": {
    "chinese":99,
    "english":88,
    "math":77
},
    "妈妈": {
    "chinese":98,
    "english":89,
    "math":77
},
    "孩子": {
    "chinese":79,
    "english":97,
    "math":88
},

        }
# 如何获取数据：因为没有下标索引，通过把"key"放在[]中
print(f"你爹全科多少分：{my_dict["爸爸"]}")
print(f"你妈英语多少分：{my_dict["妈妈"]["english"]}")
"""
新增及其更改元素：
字典名["key"]=value
删除元素：
字典.pop("key")
清空字典：
字典.clear()
获取全部的key：
字典.keys()
统计字典元素数量：
len(字典名)
可以推导出字典遍历：（不支持while循环）
"""
for key in my_dict:
    print(key,end=" ")
    print(my_dict[key])
# for key in 字典 就可以开始遍历了（其实key为要遍历的那层字典的底标，后面是要遍历的字典名，只是因为二重）
# 注意当改变后记得更新。因为上述操作是要建立一个新字典进行修改的，我们最后需要把老字典=新字典来进行更新操作
#
# 9.6 对容器进行总结：
"""
1: max min 可以通过和len一样的格式来进行最大值最小值的寻找
e.g. {max(name)}
2:转化容器格式，同上之格式 list() tuple() str() set()即可
其中转列表、元组、集合 str是挨个字符的， 字典则只会把每个key给存进去（集合无序性及其去重性仍然存在！！）
转str样式当然一点不变
3：sorted()排序操作
注意 排序默认升序，且都会转化成列表再排序，所以根据2字典啊字符串啊啥样你也知道了
想降序？这样做： sorted(name, reverse=True)
"""
# 10\python 函数进阶
# 前情提要：#8
# 10.1 当时我们没有考虑函数有多个返回值 实际上可以这样
def test_return():
    return 1,"hello boy"
x,y= test_return()
print(x)
print(y)
# 10.2 传参的方法
# 默认的是对应位置，现在可以用变量赋值传参，好处也不多，就是可忽略顺序
def user_info(dog,cat,person):
    print(f"猫叫：{cat},狗叫：{dog},人叫{person}")
user_info(cat="Tom",dog="you",person="me")
# 10.3 想给参数设默认值，就在def 那里去赋值，但是要注意！默认值一旦设定，后面的参数都需要设置默认值
# 10.4 那如果不确定传多少参数怎么办 ?
def test_info(*args):
    print(args)
test_info("Tom",18)
# 注意参数合并为元组格式!
def test_info(**kwargs):
    print(kwargs)
test_info(name="Tom",age=18)
# 注意参数合并为字典格式!
# 10.5 函数作为参数
# def那一行参数为函数名，这个与其说是作为参数数据，不如说是作为计算逻辑的传递
def test_func(compute):
    result = compute(1,2)
def compute(x,y):  #计算逻辑函数
    return x+y
# 10.6 匿名函数 感觉没一点用
# lambda 传入参数:函数体 （注意，只能一行）

# 11\ 文件操作
# 11.1 打开文件 f= open(name,mode,encoding)
"""
f为面向对象的对象名
name 为文件名
mode 包括只读 r 写入 w 和追加 a
encoding一般为UTF-8
"""
f = open("D:/Python/pythonProject/Python study exercise/test1.txt", "r", encoding="UTF-8")

# 11.2 f.read(num) num为指定长度，若()则全部内容
# 注意read是从上次read结束那里开始读，不会重新跳回开头
# readline一次读一行，也是有个fence
# for循环可以读取文件
count = 0
for line in f:
     line = line.strip() #不然每个后面都有\n
     print(f"内容是：{line}")
     words =line.split(" ")
     for word in words:
         if word =="Lin_eclipse":
             count+=1
             print(f"出现了{count}次")
# 或者
count = 0
content = f.read()
count =content.count("Lin_eclipse")
print(f"出现了{count}次")
# 11.3 f.close()文件关闭
f.close()
# 附时间延迟
import time
time.sleep(5) # 5s

# 11.3 f.write("")
f = open("D:/Python/pythonProject/Python study exercise/test1.txt", "w", encoding="UTF-8")
f.write("Lin_eclipse is a good boy who studies in S\tC\tU\tT\t, Guangzhou,\n yeah what I talk about is Lin_eclipse.")
f.flush()# 刷新
f.close()
#注意，写入如果是w来open，就会清空内容在写，不想清空？那就去追加，用a来打开
# 写个李云龙猜数吧

# 12\ 异常 模块 包
# 12.1



