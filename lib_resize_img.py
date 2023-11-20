import cv2
import os
# if __name__ == '__main__':
#     img = cv2.imread('../assets/play.png')
#     cv2.imshow('resize before', img)

#     height = img.shape[0]
#     width = img.shape[1]
#     img = cv2.resize(img, (int(width*1920/1280), int(height*1080/720)))
#     cv2.imshow('resize after', img)
#     cv2.imwrite('./newPlay.png', img)
#     cv2.waitKey()

# 将 1920*1080 图片按照当前原神客户端的分辨率进行缩放
def img_resize(path, width, height):
    file_name = os.path.basename(path)
    img = cv2.imread(path)
    img_height = img.shape[0]
    img_width = img.shape[1]
    img = cv2.resize(img, (int(img_width*width/1920), int(img_height*height/1080)))
    new_path = './tmp/' + file_name
    cv2.imwrite(new_path, img)