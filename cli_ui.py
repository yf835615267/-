import time

start_t = ""

def cli_ui():
    global start_t
    chose = 0
    times = 0
    print("========================================================")
    print("*             欢迎使用自定义健身计时小工具             *")
    print("========================================================")
    start_t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    while True:
        print("模式选择")
        print("1: 内置模式")
        print("2: 文件模式")
        chose = int(input('请输入一个数字选择模式(1 or 2)：'))
        if chose == 1:
            break;
        elif chose == 2:
            times = int(input('自定义动作准备练习几组(1~10):'))
            if times >= 1 and times <= 10:
                break;
            else:
                print("设置错误...")
        else:
            print("模式选择错误...")

    #print(start_t)
    return chose, times

def cli_ui_end():
    global start_t
    end_t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("========================================================")
    print("*                     今日训练完成                     *")
    print("* Start:" + start_t + "    " + "End:" + end_t + " *")
    print("========================================================")
    input('请输入任意键退出...')

if __name__ == "__main__":
    cli_ui()
    cli_ui_end()
