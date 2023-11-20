import os
import sys
# 获取图像的地址
class ImgPath():
    choose: str
    play: str

def get_img_path(width, height):
    # 指定文件夹路径
    folder_path = './assets' + '/' + str(width) + 'x' + str(height) + '/'
    imgPath = ImgPath()
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for element in files:
        name, extension = os.path.splitext(element)
        if name == 'choose':
            imgPath.choose = folder_path + element
        elif name == 'play':
            imgPath.play = folder_path + element
        else:
            print('图片检测失败，请正确命名图片')
            input()
            sys.exit()                        
    return imgPath

