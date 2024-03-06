from detect import *
import time
import win32gui, win32ui, win32con, win32api,pydirectinput,keyboard,pyautogui

def window_capture(filename):
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = 1980
    h = 1080
    print(w,h)  #图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
def Valorant_Aibot_Flag0():
    global valorant_flag
    valorant_flag=1
def Valorant_Aibot_Flag1():
    global valorant_flag
    valorant_flag=0
if __name__ == '__main__':
    opt = parse_opt()
    valorant_flag=0
    while(1):
        if (valorant_flag==0):
            if os.path.exists('./runs/detect/exp/result.txt'):
                os.remove('./runs/detect/exp/result.txt')
            window_capture("./data/images/screenshot.jpg")
            main(opt)
            if os.path.exists('./runs/detect/exp/result.txt'):
                f = open('./runs/detect/exp/result.txt')
                line = f.readline().strip().split(',')  # 读取第一行
                f.close()
                # pydirectinput.move(round(float(line[0]))-960, round(float(line[1]))-540,duration=1)
                pyautogui.dragTo(float(line[0]),float(line[1]),duration=1)
            else:
                pass
            time.sleep(0.5)
            keyboard.add_hotkey('f12', Valorant_Aibot_Flag0)
        else:
            keyboard.add_hotkey('alt+f12', Valorant_Aibot_Flag1)



