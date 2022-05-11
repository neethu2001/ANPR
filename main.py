import cv2
import numpy as np
import time
import imutils
from find_plate import detection
# from ocr import ocr 
from ocr import ocr
import os.path
from os import path
import sqlite3 as sql
from sqlite import retrieve

import remove
remove.remove()



from flask import Flask, render_template, Response
import cv2
from sqlite.retrieve import create_connection
app=Flask(__name__)
camera = cv2.VideoCapture("cardemo/cardemo/demo.mp4")



def gen_frames():  
    font = cv2.FONT_HERSHEY_PLAIN
    starting_time = time.time()
    frame_id = 0
    detector = detection()
  
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            # frame = imutils.resize(frame,width=400,height=400)
            frame_id += 1
            try:
              detector.detect(frame)
            except Exception as e:
                print(e)
         
            


            elapsed_time = time.time() - starting_time
            fps = frame_id / elapsed_time
            cv2.putText(frame, "FPS: " + str(round(fps, 2)), (10, 50), font, 4, (0, 0, 0), 3)
            if(path.exists("ocr.txt")):
                pass 
            else:
             if(path.exists("crop4.jpg")):
                 r = ocr.image_to_text()

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
     

@app.route('/detection')
def index():
    return render_template('video.html')


@app.route('/')
def detec():
    return render_template("main.html")



@app.route('/video_feed') 
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/data')
def list():
   conn = retrieve.create_connection("sqlite/data.db")
   rows = retrieve.select_all_tasks(conn)
   for i in rows:
       print(i)
   return render_template("data.html",rows = rows)

if __name__=='__main__':
    app.run(debug=True)