# from pydoc import importfile
import cv2
import os
import pandas as pd
from deepface import DeepFace

cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

class VideoCamera(object):

    
    def __init__(self):
        self.video=cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()

    def get_frame(self):
        ret,frame=self.video.read()
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # print(movie)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        result=DeepFace.analyze(frame,actions=['age'])
        
        print(result.get('age'))


        faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
        )

        if(result.get('age')>0):
           if(result.get('age')<15): 
                org = (50, 50)
                fontScale = 0.7
                color = (255, 0, 0)
                thickness = 2
                cv2.putText(frame,
                    "Looks Like: "+str(result['age'])+" Skin Type: Normal + Sensitive",
                    org,
                    font, fontScale,
                    color,
                    thickness,
                    cv2.LINE_AA)

        if(result.get('age')>=15):
               if(result.get('age')<30): 
                org = (50, 50)
                fontScale = 0.7
                color = (255, 0, 0)
                thickness = 2
                cv2.putText(frame,
                    "Looks Like: "+str(result['age'])+" Skin Type: Oily + Sensitive",
                    org,
                    font, fontScale,
                    color,
                    thickness,
                    cv2.LINE_AA)
        
        
        if(result.get('age')>=30):
               if(result.get('age')<35): 
                org = (50, 50)
                fontScale = 0.7
                color = (255, 0, 0)
                thickness = 2
                cv2.putText(frame,
                    "Looks Like: "+str(result['age'])+" Skin Type: Oily + Rough",
                    org,
                    font, fontScale,
                    color,
                    thickness,
                    cv2.LINE_AA)

        if(result.get('age')>=35):
               if(result.get('age')<50): 
                org = (50, 50)
                fontScale = 0.7
                color = (255, 0, 0)
                thickness = 2
                cv2.putText(frame,
                    "Looks Like: "+str(result['age'])+" Skin Type: Dry",
                    org,
                    font, fontScale,
                    color,
                    thickness,
                    cv2.LINE_AA)
        
        if(result.get('age')>=50):
            
            org = (50, 50)
            fontScale = 0.7
            color = (255, 0, 0)
            thickness = 2
            cv2.putText(frame,
                "Looks Like: "+str(result['age'])+" Skin Type: Dry + Wrinkled",
                org,
                font, fontScale,
                color,
                thickness,
                cv2.LINE_AA)


    # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
          cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
             self.video.release()

             
        
        moviemeta=pd.read_csv('Book1.csv')
        
        movie=moviemeta.loc[moviemeta['Age']==15,['Rank','Price']].iloc[0]
      

        ret,jpeg=cv2.imencode('.jpg',frame)
        return jpeg.tobytes()

# theExample = VideoCamera()
# with open('Book1.csv', 'rb') as f:
#   contents = f.read()

mm= pd.read_csv('Book1.csv')
        
movie=mm.loc[mm['Age'].isin([15]),['Rank','Price','Brand','Label','Link']]
mov=mm.loc[mm['Age'].isin([15]),['Price']]
movi=mm.loc[mm['Age'].isin([15]),['Brand']]
mo=mm.loc[mm['Age'].isin([15]),['Label']]
ul=mm.loc[mm['Age'].isin([15]),['Link']]
df=pd.DataFrame(mov)
print(df)
df.values.tolist()
print(df)
print(mo)
print(movie)
        