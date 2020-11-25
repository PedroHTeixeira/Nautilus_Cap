import cv2 #Import the OpenCV Library


nemo = cv2.VideoCapture('nemo.mp4') #Get the video file

while nemo.isOpened(): #Loop through frames while the video is opened
    ret, frame = nemo.read()

    if not ret: #If nemo.read() returns false, there is no more frame to be analysed so the loop shouls break
        print("The video ended.")
        break
    
    #Colors in HSV of the mask 
    light_orange = (1, 190, 200)
    dark_orange = (18, 255, 255)
    light_white = (0, 0, 200)
    dark_white = (145, 60, 255)

    #Coversion of the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Definition of the masks
    mask = cv2.inRange(hsv, light_orange, dark_orange)
    mask_white = cv2.inRange(hsv, light_white, dark_white)
    result_mask = mask+mask_white

    #Sobreposition of the masks and the video
    result = cv2.bitwise_and(frame, frame, mask=result_mask)

    
    cv2.imshow('Nemo Video',frame)#display the video
    

    if cv2.waitKey(1) == ord('q'): #If the key q is pressed, the loop should break
        break

#When everything is finished stop the video and close the windows
nemo.release()
cv2.destroyAllWindows()
