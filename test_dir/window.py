import win32gui
import ctypes.wintypes

    # 获取真实的窗口 POS
def get_window_rect(hwnd):
    try:
        f = ctypes.windll.dwmapi.DwmGetWindowAttribute
    except WindowsError:
        f = None
    if f:
        rect = ctypes.wintypes.RECT()
        f(ctypes.wintypes.HWND(hwnd), ctypes.wintypes.DWORD(9), ctypes.byref(rect), ctypes.sizeof(rect))
        return rect.left, rect.top, rect.right, rect.bottom


hid = win32gui.FindWindow(None, '原神')  # 不支持模糊查询
print(hid)
window_rect = get_window_rect(hid)
x = window_rect[0]
y = window_rect[1]
width = window_rect[2] - x
height = window_rect[3] - y
print(str(width-2) + ' ' + str(height-39))