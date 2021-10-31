import cv2
import time
def capture():
    print('Capturing')
    video=cv2.VideoCapture(0)
    while video.isOpened():
        ret,frame=video.read()
        if ret:
            ret,back=video.read() # read from webcam
            if ret:
                cv2.imshow("Display",back)
                if cv2.waitKey(5) == ord('q'):
                    # save image
                    cv2.imwrite('image.jpg',back)
                    break
    video.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    capture()