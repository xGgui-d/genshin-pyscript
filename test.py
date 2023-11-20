import pyautogui
import ctypes
import sys

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.1

# 获取屏幕分辨率

# print(pyautogui.size())
# 获取鼠标位置 
# print(pyautogui.position())
# 移动鼠标 0.5s
# pyautogui.moveTo(1500, 800, duration = 0.2)
# 拖动鼠标
# pyautogui.dragTo(X, Y, button='left'/'right')
# 模拟点击 在当前位置点击
# pyautogui.click()
# 模拟键盘
# pyautogui.press('f')
# 截屏
# pyautogui.screenshot("截屏.png")
def main():
    while True:
        # 模糊定位图片位置
        try:
            location = pyautogui.locateOnScreen('./assets/choose.png', region=(0, 0, 1920, 1080),confidence=0.9)
            print(location)
            point = pyautogui.center(location)
            pyautogui.click(point.x, point.y)
        except Exception as err:
            try:
                pyautogui.locateOnScreen('./assets/play.png', region=(0, 0, 1920, 1080),confidence=0.9)
                pyautogui.press(' ')
            except Exception as err:    
                print(err)             


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except BaseException as err:
        print(err)
        raise err


if __name__ == '__main__':
    # TODO:优化使用体验,跳过对话等功能
    # TODO:剧情自动
    # logger
    if not is_admin():
        if sys.version_info[0] == 3:
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
            sys.exit(0)
    main()