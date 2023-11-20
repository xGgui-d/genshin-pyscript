import pyautogui
import ctypes
import sys
import time
import datetime
import configparser
import lib_switchImg
import lib_window 
import keyboard

pyautogui.FAILSAFE = False

running = True

def logShow(msg):
    timestamp = datetime.datetime.strftime(datetime.datetime.now(), '%H:%M:%S')
    print('[%s]%s'%(timestamp, msg))

def toggle_program():
    global running
    running = not running
    if running:
        logShow("脚本已恢复运行")
    else:
        logShow("脚本已暂停")

# 获取屏幕分辨率
resolution = pyautogui.size()
# 读取配置文件
cfg = configparser.ConfigParser()
cfg.read('./settings/config.cfg', encoding = 'utf-8')
delayms = cfg.getint('allConfig', 'delay')
log = cfg.getboolean('allConfig', 'log')
key = cfg.get('allConfig', 'key')
# 绑定快捷键
keyboard.add_hotkey(key, toggle_program)
# 设置延迟
pyautogui.PAUSE = 0.1


def main():
    # 获取客户端的分辨率
    client_size = lib_window.get_window_size('UnityWndClass', '原神')
    print('『原神自动对话脚本启动成功』')
    print(' -> 当前客户端分辨率: %dx%d'%(client_size.width, client_size.height))
    print(' -> 点击延迟(ms): %d'%(delayms))
    print(' -> 是否启动日志: %s'%(str(log)))
    print(' -> 启动与暂停快捷键: %s'%(key))
    # 获取图像地址
    imgPath = lib_switchImg.get_img_path(client_size.width, client_size.height)
    print(imgPath)
    while True:
        if running == False:
            time.sleep(1)
            continue
        try: # 在屏幕上找到选项图片
            location = pyautogui.locateOnScreen(imgPath.choose\
                , region = (0, 0, resolution.width, resolution.height), confidence = 0.9)
            point = pyautogui.center(location)
            if point.x >= 0 and point.y >= 0:
                pyautogui.click(point.x, point.y)
            if log:logShow('点击选项一次<%d, %d>'%(point.x, point.y))
        except Exception:
            try: # 在屏幕上找到播放图片
                pyautogui.locateOnScreen(imgPath.play\
                    , region = (0, 0, resolution.width, resolution.height), confidence = 0.9)
                pyautogui.press(' ')
                if log:logShow('点击空格一次')
            except Exception:  
                pass
        time.sleep(delayms / 1000) # 点击延迟


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
    main()