import cv2
import uuid

cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()
    imgname = 'D:/Study Items/AI/AI_J_Comp/Face Mask Dataset/WithoutMask/{}.jpg'.format(str(uuid.uuid1()))
    cv2.imwrite(imgname,frame)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()
