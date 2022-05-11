import time
import pyttsx3

def timer_say(who: pyttsx3.engine.Engine, word: str):
    who.say(word)
    who.runAndWait()

def timer_count(who: pyttsx3.engine.Engine, t: int):
    time1 = 0
    time2 = 0
    for tmp in range(t, 0, -1):
        #time1 = time.time()
        timer_say(who, str(tmp))
        #time2 = time.time()
        #print(time2 - time1)

def timer_ready(who: pyttsx3.engine.Engine, t: int):
    timer_say(who, "准备")
    for tmp in range(t, 1, -1):
        #time1 = time.time()
        timer_say(who, str(tmp))
        #time2 = time.time()
        #print(time2 - time1)
    timer_say(who, "开始")

def timer_start(who: pyttsx3.engine.Engine, t: int):
    time_s = time.time()
    time.sleep(t - 6)
    timer_say(who, "最后5秒")
    timer_count(who, 5)
    return int(time.time() - time_s)

def timer_rest(who: pyttsx3.engine.Engine, t: int):
    timer_say(who, "休息一下")
    time.sleep(t - 6)
    timer_say(who, "休息即将结束")
    timer_count(who, 5)

def timer_begin(who: pyttsx3.engine.Engine):
    timer_say(who, "今天的训练将在20秒后开始")
    timer_say(who, "请做好准备，打开手环，放松身体~")
    time.sleep(20)
    timer_say(who, "Ready~~~？, Go~")

def practice_item(practice_list: list, times: int, who: pyttsx3.engine.Engine):
    yuji_coust = 0
    time_s = 0
    time_e = 0
    time_yundong = 0
    title = practice_list[0]["name"] + str(times) + "组, " + " 每组" + str(len(practice_list) - 1) + "个动作"
    timer_say(who, title)
    for i in range(1, len(practice_list)):
        yuji_coust = yuji_coust + practice_list[i]["time"] + practice_list[i]["header_time"]
    yuji_coust = yuji_coust * times * 1.3#1.22
    time_s = time.time()
    title = practice_list[0]["name"] + "   预计耗时" + str(int(yuji_coust / 60)) + "分" + str(int(yuji_coust % 60)) + "秒"
    print(title)
    timer_say(who, title)
    for t in range(0, times):
        title = "第" + str(t+1) + "组，准备， 共" + str(times) + "组"
        timer_say(who, title)
        for i in range(1, len(practice_list)):
            title = "第" + str(i) + "个动作  " + practice_list[i]["name"] + str(practice_list[i]["time"]) + "秒"
            timer_say(who, title)
            timer_ready(who, 5)
            time_yundong = time_yundong + timer_start(who, practice_list[i]["time"])
    time_e = time.time()
    print(practice_list[0]["name"] + "   总体耗时:" + str(int(time_e - time_s)) + "秒")
    print(practice_list[0]["name"] + "   运动耗时:" + str(time_yundong) + "秒")
    print(practice_list[0]["name"] + "   预计误差:" + str(int(time_e - time_s)/yuji_coust))
    print(practice_list[0]["name"] + "   时间效率:" + str(round(((time_yundong/int(time_e - time_s))*100), 2)) + "%")
    print("\n")
    return int(time_e - time_s), time_yundong