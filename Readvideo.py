import cv2
def readImg():
    img = cv2.imread("girl3.png", 0)
    cv2.imshow('123', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
