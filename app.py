# import logging
# import MYSCRIPT
# from test import  VideoCamera
        
        
import os
from re import L
from unittest import result
import cv2
from numpy import float64
# import os
import pandas as pd
from deepface import DeepFace
from flask import Flask,render_template,jsonify,Response
from pyparsing import Char


from test import movie
from test import mov
from test import movi
from test import mo
from test import ul
from test import VideoCamera



# m1=m

# import MYSCRIPT
# import os

# print("heloo")

app= Flask(__name__)

@app.route('/')
def index():
    # return "bye"
    return render_template('index.html')

@app.route('/started')
def faceindex():
    # return "bye"
    return render_template('faceindex.html')


def gen(camera):

    c=0
    while c!=10:
        
        frame =camera.get_frame()
        c=c+1
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame
        + b'\r\n\r\n')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            camera.release()
    


@app.route('/product')
def proindex():
    # return "bye"
    return render_template('proindex.html')

@app.route('/comments/')
def comments():
    # for(int j=0;j<2;j++):
    # j=0
    # while j!=1:
    #   comments=movie.iloc[j]
    # n=(mov.iloc[0][0])
    m=[]
    n=[]
    k=[]
    l=[]
    li=[]
    for j in range(len(movie)):
      m.append(str(str(movie.iloc[j][0])+"  "+" Price:"+str(movie.iloc[j][1])+" Brand:"+str(movie.iloc[j][2])+" Type:"+str(movie.iloc[j][3])+" BUY"+str(movie.iloc[j][4])))
    #   n.append(float64(mov.iloc[j]))
    #   k.append(str(movi.iloc[j][0]))
    #   l.append(mo.iloc[j][0])
      li.append(ul.iloc[j][0])
     # v= str(m1)
    j=0

    # def brand():
    # for l in range(len(movi)):
    #         # m.append(float64(movie.iloc[j]))
    #      n.append((movi.iloc[l]))
     # v= str(m1)
    # l=0


    return render_template('comments.html', comments=m,j=j)

@app.route('/pic')
# def pic():
#     os.system('MYSCRIPT.py') #file.py is the script I'm trying to start
#     return "done"

def pic():
 
    return Response(gen(VideoCamera()),
    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ =='__main__':
 app.run(debug=True, port=8080)