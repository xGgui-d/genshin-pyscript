import win32gui
import ctypes.wintypes
import pyautogui
# 获取屏幕分辨率
resolution = pyautogui.size()
# 获取原神窗口的分辨率大小
def get_window_size(str_name):
    hwnd = win32gui.FindWindow(None, str_name)
    try:
        f = ctypes.windll.dwmapi.DwmGetWindowAttribute
    except WindowsError:
        f = None
    if f:
        rect = ctypes.wintypes.RECT()
        f(ctypes.wintypes.HWND(hwnd), ctypes.wintypes.DWORD(9), ctypes.byref(rect), ctypes.sizeof(rect))
        width  = rect.left - rect.right
        if width < 640:
            width = resolution.width
        height = rect.top - rect.bottom
        if height < 480:
            height = resolution.height
        return width-2, height-39