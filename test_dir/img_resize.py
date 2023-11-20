import cv2

if __name__ == '__main__':
    img = cv2.imread('../assets/play.png')
    cv2.imshow('resize before', img)

    height = img.shape[0]
    width = img.shape[1]
    img = cv2.resize(img, (int(width*1920/1280), int(height*1080/720)))
    cv2.imshow('resize after', img)
    cv2.imwrite('./newPlay.png', img)
    cv2.waitKey()

