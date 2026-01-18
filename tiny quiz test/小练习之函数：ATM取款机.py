# · 定义一个全局变量:money,用来记录银行卡余额(默认5000000)
# · 定义一个全局变量:name,用来记录客户姓名(启动程序时输入)
money = 5000000
name = " "
key = "000000"
# · 定义如下的函数:
# 密码认证函数
def defi():
    try_time = 5
    while try_time > 0:
        try_time -= 1
        user_ink = input("请输入您的密码")
        if key == user_ink:
            return True
        else:
            print(f"输入密码错误，您还有{try_time}次机会重新输入密码")
            continue
# 改名及其密码函数
def change():
    global name,key
    if defi():
            register()
# 注册账户函数
def register():
    global name,key
    user_input = input("请输入您的姓名以及密码,以空格隔开")
    name, key = user_input.split(' ')
    check_m()
# · 查询余额函数
def check_m () :
    print(f"您的账户余额为{money}")
# 存款函数
def mor_m():
    mor = int(input("请输入您本次的存款:"))
    global money
    money += mor
    print(f"成功存入{mor}元钱")
    check_m()
# · 取款函数
def les_m():
    if defi():
        les = int(input("请输入您本次的取款:"))
        global money
        if money <= les:
            print("您的余额不足！")
            check_m()
        else:
            money -= les
            print(f"成功取走{les}元钱")
            check_m()
    else: exit()
# · 主菜单函数
def MAIN_BANK():
    #1.存款 2. 取款 3.改名字或密码
    print("\tYBY银行欢迎您的使用！！！")
    print("\t\t0:退出应用")
    print("\t\t1:存款")
    print("\t\t2:取款")
    print("\t\t3:修改名字&密码")
    choice = int(input(f"尊敬的用户{name},请输入您想要进行的操作:"))

    if choice == 0:
        print("感谢您的使用！希望我们下一次相遇，再见！")
        exit()
    elif choice == 1:
        mor_m()
        MAIN_BANK()
    elif choice == 2:
        les_m()
        MAIN_BANK()
    elif choice == 3:
        change()
        MAIN_BANK()
def main():
    print("\t\t\t\t欢迎使用YBY_python_ATM线上应用")
    register()
    MAIN_BANK()
main()
# 要求:
# 程序启动后要求输入客户姓名
# · 查询余额、存款、取款后都会返回主菜单
# · 存款、取款后,都应显示一下当前余额
# · 客户选择退出或输入错误,程序会退出,否则一直运行