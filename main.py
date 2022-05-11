import pyttsx3
import cli_ui as cli
import base_mode as base
import file_operare as fp

if __name__ == "__main__":
    timer_voice = pyttsx3.init() #创建一个可以说话的对象
    mode, times = cli.cli_ui()

    if mode == 1:
        base.base_practice(timer_voice)
    elif mode ==2:
        fp.filelist_practice(timer_voice, times)

    cli.cli_ui_end()