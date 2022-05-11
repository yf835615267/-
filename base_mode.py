import time
import pyttsx3
import voice.voice as vc

#practice_item = {"name": "", "header_time": 0, "time": 0}

reshen_header = 5
reshen_time = 20
practice_list_reshen = [
    {"name": "热身运动", "header_time": 0, "time": 0},
    {"name": "简易开合", "header_time": reshen_header, "time": reshen_time},
    {"name": "半深蹲", "header_time": reshen_header, "time": reshen_time},
    {"name": "转体扩胸", "header_time": reshen_header, "time": reshen_time},
    {"name": "左弓步下压", "header_time": reshen_header, "time": reshen_time},
    {"name": "右弓步下压", "header_time": reshen_header, "time": reshen_time},
]

quanshen_header = 10
quanshen_time = 25
practice_list_quanshen = [
    {"name": "全身燃脂", "header_time": 0, "time": 0},
    {"name": "深蹲", "header_time": reshen_header, "time": reshen_time},
    {"name": "摆臂对侧肘碰膝", "header_time": quanshen_header, "time": quanshen_time},
    {"name": "左右弓步手触地", "header_time": reshen_header, "time": reshen_time},
    {"name": "胯下击掌", "header_time": reshen_header, "time": reshen_time},
    {"name": "连续半深蹲", "header_time": reshen_header, "time": reshen_time},
    {"name": "左侧外摆腿", "header_time": reshen_header, "time": reshen_time},
    {"name": "右侧外摆腿", "header_time": reshen_header, "time": reshen_time},
    {"name": "支撑拉伸大腿", "header_time": reshen_header, "time": reshen_time},
    {"name": "支撑拉伸小腿", "header_time": reshen_header, "time": reshen_time},
    {"name": "简易开合", "header_time": reshen_header, "time": reshen_time},
]

fubu_header = 10
fubu_time = 25
practice_list_fubu = [
    {"name": "腹部燃脂", "header_time": 0, "time": 0},
    {"name": "摆臂对侧肘碰膝", "header_time": fubu_header, "time": fubu_time},
    {"name": "简易开合", "header_time": reshen_header, "time": reshen_time - 10},
    {"name": "胯下击掌", "header_time": fubu_header, "time": fubu_time},
    {"name": "简易开合", "header_time": reshen_header, "time": reshen_time - 10},
    {"name": "俄罗斯转体", "header_time": reshen_header, "time": reshen_time},
    {"name": "仰卧踩单车", "header_time": reshen_header, "time": reshen_time},
    {"name": "俯身登山", "header_time": reshen_header, "time": reshen_time},
    {"name": "腹直肌拉伸", "header_time": reshen_header, "time": reshen_time},
]

def base_practice(timer_voice: pyttsx3.engine.Engine):
    time_item_all = 0
    time_yundong_all = 0
    am_or_pm = time.localtime()

    vc.timer_begin(timer_voice)
    # 热身运动
    t1, t2 = vc.practice_item(practice_list_reshen, 1, timer_voice)
    time_item_all = time_item_all + t1
    time_yundong_all = time_yundong_all + t2

    if am_or_pm.tm_hour < 12:
        # 腹部燃脂
        vc.timer_say(timer_voice, "AM.上午   腹部燃脂")
        t1, t2 = vc.practice_item(practice_list_fubu, 5, timer_voice)
        time_item_all = time_item_all + t1
        time_yundong_all = time_yundong_all + t2
    else:
        # 全身燃脂
        vc.timer_say(timer_voice, "PM.下午   全身燃脂")
        t1, t2 = vc.practice_item(practice_list_quanshen, 5, timer_voice)
        time_item_all = time_item_all + t1
        time_yundong_all = time_yundong_all + t2

    print("总体耗时:" + str(round(time_item_all / 60, 2)) + "分"+ str(time_item_all % 60) + "秒")
    print("运动耗时:" + str(round(time_yundong_all / 60)) + "分"+ str(time_yundong_all % 60) + "秒")
    print("时间效率:" + str(round(((time_yundong_all/time_item_all)*100), 2)) + "%")
    vc.timer_say(timer_voice, "恭喜完成")

if __name__ == "__main__":
    timer_voice = pyttsx3.init() #创建一个可以说话的对象
    base_practice(timer_voice)