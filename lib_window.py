import win32gui
import pyautogui
import sys

# 获取窗口的大小
class WinSize():
    width: int
    height: int

    
def get_window_size(class_name, title_name):
    win_size = WinSize()
    hwnd = win32gui.FindWindow(class_name, title_name)
    if win32gui.IsIconic(hwnd):
        isfull = input('是否启用全屏游戏(y/任意键)?')
        if isfull == 'y':
            print('获取客户端分辨率成功，请使用全屏进行游戏')
            win_size.width = pyautogui.size().width
            win_size.height = pyautogui.size().height
            return win_size
        else: 
            print('请把已最小化的原神客户端窗口恢复以获取分辨率，并按下任意键继续...')
            input()
    window_rect = win32gui.GetClientRect(hwnd)
    win_size.width = window_rect[2] - window_rect[0]
    win_size.height = window_rect[3] - window_rect[1]
    if win_size.width == 0 or win_size.height == 0:
        print('获取客户端分辨率失败，启动脚本时请勿将应用程序窗口最小化')
        input()
        sys.exit()         
    return win_size   
