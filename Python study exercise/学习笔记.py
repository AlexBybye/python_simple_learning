# 1\注释
# 1.1 单行注释

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
# 1.2 数据类型注解
"""
ctrl+p 查看类型
var_1: int = 10   (int var =10 的意思）
stu:student=student() (student stu =student()的意思)
def add(x: int ,y:double)->double : 最后一个double是返回值的类型
总结起来就是每个数据赋值的时候在=前加一个 :数据类型
对于容器联合型要如何去定义？
from typing import Union
my_list: list[union[int,str]]=["billionaire",13892576834]
这只是作为IDE工具来帮你做代码提示或备注，不会因为标错而报错
"""
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
mode 包括只读 r 写入 w 和追加 a，注意后二者会在没有文件的时候创建新文件
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
import time #这里就是模块的导入
time.sleep(5) # 5s

# 11.3 f.write("")
f = open("D:/Python/pythonProject/Python study exercise/test1.txt", "w", encoding="UTF-8")
f.write("Lin_eclipse is a good boy who studies in S\tC\tU\tT\t, Guangzhou,\n yeah what I talk about is Lin_eclipse.")
f.flush()# 刷新
f.close()
#注意，写入如果是w来open，就会清空内容在写，不想清空？那就去追加，用a来打开
# 写个李云龙猜数吧

# 12\ 异常 模块 包
# 12.1 异常的捕获
try: False
# 可能有bug的语句
except Exception as e:
    print(f"{e}异常了，哥，在412行，咋整")
else:
    print("这里就是没异常执行的语句，当然不写也行，那写这个干啥真是了")
finally:
    print("异不异常都执行这个语句")
    f.close()
# 写下如果有bug的解决方案
# 用处就是可以不用看终端那乱七八糟的了，异常可传递性

# 12.2模块
"""
1.导入外部模块，说白了，就是现成的库，import就完事了
2.导入自己的文件，有点像#include"" 不过在python一样 import XX 就行, 其文件名应该是 XX.py

"""
# 12.3包
"""
pip install 
常用：
科学计算中常用的:numpy包

数据分析中常用的:pandas包

大数据计算中常用的:pyspark、apache-flink

图形可视化常用的:matplotlib、pyecharts

人工智能常用的:tensorflow
"""
# 13\python可视化
"""
# 13.1 json
json文件（各个编程语言通用数据格式）
本质格式为str
和python字典、列表无缝衔接
通过:
import json
json_Str = json.dumps(python_data,ensure_ascii= False # 注意这里asc码这个没有汉语不用带) # python dict/list ->json str
python_data = json.loads(json_Str) # json str-> python dict / list
"""
# 13.2 pyecharts(之前数模那个是echarts模块python化）
# import pyecharts
# gallery.pyecharts.org 有相关代码，之后有各类是否显示的代码可以配上，如下：
"""
line.set_global_opts(
   title_opts=TitleOpts(title="it", pos_left="center", pos_bottom="1%"),
   legend_opts=LegendOpts(is_show=True),
   toolbox_opts=ToolboxOpts(is_show=True),
   visualmap_opts=VisualMapOpts(is_show=True),
   tooltip_opts=TooltipOpts(is_show=True),
)
"""
# 数据处理：有个ab173.com不错，知道就行。

# 14\面向对象的python 开始封装吧
# 14.1 类与对象
class student:
    def get_secret(self):
        return self.__secret or "No secret"
    # 公共接口调用私有
    def __secretdiscover(self):
        if self.__secret == None:
            self.EQ =0
        else: self.EQ =1
    def __init__(self,name,gender,nationality,native_place,age):
        self.name=name
        self.gender=gender
        self.nationality=nationality
        self.native_place=native_place
        self.age=age
        self.__secret = None
        self.EQ = None
    def say_hi(self,msg):
        print(f"Hi everyone, I am{self.name},glad to meet u! {msg}")
stu_1=student("Lin_eclipse","Male","China","Guangzhou",21)
stu_1.say_hi("And I don't wanna meet u twice again")
# 私有内部自由使用，但是对象无法调用，私有只需要在名字前__

# 14.2 继承
class top_student(student):
    def __init__(self, name, gender, nationality, native_place, age):
        # 必须显式调用父类构造函数
        super().__init__(name, gender, nationality, native_place, age)
        self.IQ=250

    def say_hi(self, msg):
        # 正确调用父类方法的方式
        super().say_hi(msg)
        print(f"By the way, my IQ is {self.IQ}!")
stu_2=top_student("Lin","Female","Romania","Panjin",20)
stu_2.say_hi("Emm, Lin_eclipse is a cool boy.")
# 这句话错的，不能在对象这么去调用父类的函数
# 想继承很多？就在class括号里面多加几个父类，用，隔开
# 涉及到同名调用父类？在子类里面无论变量还是函数用super().即可

# 14.3 多态
# 多态是啥？最简单的一种多态是父类定义，子类分别做实际工作
"""
这里紧接着就产生了虚拟类问题
父类因为可能没有实现，只有一个构造函数
那就写 pass
这样父类就是抽象类了
就是顶层设计，底层分别实现
"""
class Animal:
   def speak(self):
       pass
class Dog(Animal):
   def speak(self):
       print("汪汪汪")
class Cat(Animal):
   def speak(self):
       print("喵喵喵")

# 15\SQL接轨
"""
15.1 SQL注释为 单行：#
多行： /* */
SQL语言可以跳行不区分大小写
下面的语句大部分where或者from都可以根据是否需要而选择写或者不写

15.2 DDL基本规则
查看数据库 show databases;
使用数据库 use 数据库名;
创建数据库 create database 数据库名 [charset utf8];
删除数据库 drop database 数据库名;
查看正在使用数据库 select database();
表：
查看数据表 show tables;（先选库）
创建数据表 create table 数据表名 (列名称 列类型
列名称 列类型
 ...  ...
);
其中列类型有
int
float
varchar(长度)  文本,长度为数字,做最大长度限制
date          日期类型
timestamp     时间戳类型
删除数据表 drop table 数据表名;

15.3 DML基本规则
数据插入 
insert into 数据表名(列1，列2，...列N) 
values(值1，值2，...，值N) (值1，值2，...，值N); ......
数据删除 
delete from 数据表名 where 条件判断; # 比如 age>33或者 name="Lin_eclipse"
数据更新
update 数据表名 set 列名=更新值 where条件判断;

15.4 DQL基本规则
数据查询
1.普通：
select 搜查的东西（比如列名） from 数据表名 where 条件判断（即为当条件成立，从规定区域查询）
2.分组&聚合（可以单独出现）：
select 列名a,聚合函数(列名随意) from 数据表名 where 条件判断 group by 列名a
说白了就是先通过列名的列数据的不同进行分组
聚合函数都有什么？
sum(列名) avg(列名)min(列名) max(列名) count(列名)
当然可以用逗号隔开，一次写一堆聚合函数
3.排序&分页（和group by是一样的）
order by 列名 asc(升序）/desc（降序）； 
limit a,b; a为跳过的行数 b为只读取的行数
如果只有一个数字就只作为b来使用
 
总结DQL： select 列名/聚合函数 from 数据表名 where ... group by...  order by...asc/desc limit n,m;

15.5 pythonSQL接口
pip install pymysql
from pymysql import Connection
conn = Connection(
    host = "localhost",
    port=3306,
    user="root",
    password="Mimashi007"
    autocommit= True
)
# print(conn.get_sever_info()) #先试试行不行，跑的通就注释掉就行
cursor= conn.cursor()
# 获取光标对象
conn.select_db("数据库名")
# 选择数据库
cursor.execute("这里面写15.1-15.4的SQL语句")
results=cursor.fetchall()

for r in results:
    print(r)
    
conn.close()

"""

# 至此，python结题
# 后续会做一个类似于足球联赛管理系统，负责接收C++的足球俱乐部管理系统的信息，可能还涉及到数据库的调用等。