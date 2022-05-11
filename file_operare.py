import csv
import pyttsx3
import voice.voice as vc
from pathlib import Path

list_file = "list.csv"

#practice_item = {"name": "", "header_time": 0, "time": 0}

def file_read():
    my_list = []
    practice_item = {"name": "", "header_time": 0, "time": 0}
    my_file = Path(list_file)
    if my_file.exists():
        # print("exit")
        f = open(list_file, 'r', encoding='gbk')
        reader = csv.DictReader(f)
        for line in reader:
            practice_item["name"] = line["name"]
            practice_item["header_time"] = int(line["header_time"])
            practice_item["time"] = int(line["time"])
            my_list.append(dict(practice_item))
            #print(line)
        #print(my_list)
        f.close()
    else:
        # print("create")
        with open(list_file, 'a', newline='') as f:
            header = list(practice_item.keys())
            # print(header)
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()  # 写入列名
    return my_list

def filelist_practice(timer_voice: pyttsx3.engine.Engine, times: int):
    practice_list = file_read()
    if len(practice_list) > 1:
        vc.timer_begin(timer_voice)
        vc.practice_item(practice_list, times, timer_voice)
        vc.timer_say(timer_voice, "恭喜完成")
    else:
        vc.timer_say(timer_voice, "训练动作列表为空")
        print("训练动作列表为空")

if __name__ == "__main__":
    timer_voice = pyttsx3.init()  # 创建一个可以说话的对象
    filelist_practice(timer_voice, 1)
