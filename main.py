import cv2
import keyboard

cas_face = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cas_eye = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cam = cv2.VideoCapture(0,cv2.CAP_DSHOW) #내장 웹캠으로 설정

temp = 0

while cam.isOpened():

    success, frame = cam.read()
    key = cv2.waitKey(1) & 0xFF

    if success:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = cas_face.detectMultiScale(gray, 1.3, 5)
        for x,y,w,h in faces:
            cv2.rectangle(frame,(int(x),int(y)),(int(x+w),int(y+h)),(0, 255, 0), thickness=2)
            cv2.putText(frame, 'Face', (int(x+w+5),int(y+h)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), thickness=2)

            roi_frame = frame[y:y+h, x:x+w]
            roi_gray = gray[y:y+h, x:x+w]

            eyes = cas_eye.detectMultiScale(roi_gray, 1.3, 5)

            for ix, iy, iw, ih in eyes:
                cv2.rectangle(roi_frame,(int(ix),int(iy)),(int(ix+iw),int(iy+ih)),(255, 0, 0), thickness=2)
                cv2.putText(roi_frame, 'Eye', (int(ix+iw+5),int(iy+ih)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), thickness=2)
                
                roi_frame_frame = roi_frame[iy:iy+ih, ix:ix+iw]
        
        if keyboard.is_pressed('f'):
            temp = 1
            
        elif keyboard.is_pressed('e'):
            temp = 2
            
        elif keyboard.is_pressed('b'):
            temp = 0
        
        
        if temp == 1: # f키를 눌렀을 때
            blur_Face = cv2.resize(roi_frame, dsize=(0, 0), fx= 0.06, fy = 0.06) # 가로/세로 각각 0.06배
            blur_Face = cv2.resize(blur_Face, (int(w), int(h)), interpolation=cv2.INTER_AREA)

            frame[y:y+h, x:x+w] = blur_Face # 얼굴 영역 만큼을 모자이크
            cv2.imshow('', frame)
            

        elif temp == 2: # e키를 눌렀을 때
            blur_Eyes = cv2.resize(roi_frame_frame,  dsize=(0, 0), fx= 0.03, fy = 0.03) # 가로/세로 각각 0.03배
            blur_Eyes = cv2.resize(blur_Eyes, (int(iw), int(ih)), interpolation=cv2.INTER_AREA)

            roi_frame[iy:iy+ih, ix:ix+iw] = blur_Eyes # 눈 영역 만큼을 모자이크
            cv2.imshow('', frame)

        else:
            cv2.imshow('', frame)

        if key == 27: #Esc키를 눌렀을때
            break # 프로그램 종료

cam.release()
cv2.destroyAllWindows()