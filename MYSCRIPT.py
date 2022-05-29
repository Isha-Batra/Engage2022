
# from distutils.log import debug
import cv2
import os
# import json
import pandas as pd
from deepface import DeepFace
from pip import main

# def main():
cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# moviemeta=pd.read_csv('Book1.csv')     aouji.com@gmail.com

video_capture = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    # Capture frame-by-frame
    ret, frames = video_capture.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)


    # emotion = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
    # age=(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
    result=DeepFace.analyze(frames,actions=['age'])

    # r=pd.DataFrame.from_dict(result)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    org = (50, 50)
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2
    cv2.putText(frames,
            chr(result['age']),
            org,
            font, fontScale,
            color,
            thickness,
            cv2.LINE_AA)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
    # Display the resulting frame
    # movie=moviemeta.loc[moviemeta['Age']==15,['Rank','Price']].iloc[0]
    cv2.imshow('Video', frames)
    print(result)
    # if(int(r[0])>20):
    # print(r)
    # print(movie)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

# if __name__ == "__main__":
#     # main()
#     main.run(debug=True,port=8080)