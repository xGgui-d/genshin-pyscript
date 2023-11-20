import pyautogui
import ctypes
import sys
import numpy as np
import time
import datetime
import configparser
import threading
import keyboard

import lib_window 
import lib_resize_img

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.1

class CThread (threading.Thread):
    def __init__(self, n):
        threading.Thread.__init__(self)  #重写父类方法
        self.num = n

    def run(self):
        print('守护线程开启，线程id[%d]'%(self.num))
        while True: # 检测按键
            if keyboard.is_pressed('a') and keyboard.is_pressed('s'):
                print("按下了'a+s'键")
                break    


# 获取屏幕分辨率
resolution = pyautogui.size()
# 读取配置文件
cfg = configparser.ConfigParser()
cfg.read('./settings/config.cfg', encoding = 'utf-8')
delayms = cfg.getint('allConfig', 'delay')
log = cfg.getboolean('allConfig', 'log')
# 获取客户端的分辨率 client_size[0] 为 width，1 为 height
client_size = lib_window.get_window_size('原神')
print(client_size[0])
print(client_size[1])
# 更改图片大小
lib_resize_img.img_resize('./assets/choose.png',client_size[0], client_size[1])
lib_resize_img.img_resize('./assets/play.png',client_size[0], client_size[1])

def main():
    print("原神自动对话脚本启动成功")
    while True:
        try: # 找到选项图片
            location = pyautogui.locateOnScreen('./tmp/choose.png'\
                , region = (0, 0, resolution.width, resolution.height), confidence = 0.9)
            point = pyautogui.center(location)
            rand_x = point.x + np.random.randint(0,50)
            rand_y = point.y + np.random.randint(-3,3)
            pyautogui.click(rand_x, rand_y)
            if(log):
                timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
                print('[%s]点击选项<%d, %d>'%(timestamp, rand_x, rand_y))
        except Exception: # 找不到选项图片
            try: # 找到播放图片
                pyautogui.locateOnScreen('./tmp/play.png'\
                    , region = (0, 0, resolution.width, resolution.height), confidence = 0.9)
                pyautogui.press(' ')
                if(log):
                    timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
                    print('[%s]点击空格'%(timestamp))
            except Exception: # 找不到播放图片   
                pass
        randDelayms = np.random.randint((1 - 0.1) * delayms, (1 + 0.1) * delayms)    
        time.sleep(randDelayms / 1000) # 点击延迟

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except BaseException as err:
        print(err)
        raise err


if __name__ == '__main__':
    if not is_admin():
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            sys.exit(0)

    ctrl_thread = CThread(1)  # 开启一个线程
    ctrl_thread.start()  
    main()