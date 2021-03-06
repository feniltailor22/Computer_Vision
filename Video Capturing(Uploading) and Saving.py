import cv2

cap=cv2.VideoCapture(0);
#If we want to upload the video from computer:
#cap=cv2.VideoCapture('Video Path');

#Printing height and width of the video frame:
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#Setting up camera parameter(increasing hight and width of video)
cap.set(3, 1208) #width(3)=1208
cap.set(4, 720) #height(4)=720

#Saving the captured video

fourcc= cv2.VideoWriter_fourcc(*'XVID')
out= cv2.VideoWriter(filename='output.avi', fourcc=fourcc, fps=20.0, frameSize=(640,480))

print(cap.isOpened())

#Creating While loop to capture the frame continuosly

while (cap.isOpened()):
    ret, frame=cap.read()
    
    #Reading method gives True as an output if the cap(VideoCapture) is available and storing it as a frame.
    # ret= returning True or False 
    
    if ret == True:
    #If we want gray scale video capturing then use below command:
    #For color video capturing, we dont need it.
    #gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame',gray)
   
        out.write(frame)

        cv2.imshow('frame',frame)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:       
        break

out.release()
cap.release()
cv2.destroyAllWindows()
    
#If video frame is on and we press 'q' key then all video frame will be distroyed.
