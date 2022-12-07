# https://www.youtube.com/watch?v=HT99qGWFpgM
import cv2
import numpy as np
import dlib
import pafy

url = 'https://www.youtube.com/watch?v=HT99qGWFpgM'
video = pafy.new(url)
video_melhor_qualidade = video.getbest()

elemento_captura = cv2.VideoCapture(video_melhor_qualidade.url)

detector_faces = dlib.get_frontal_face_detector()

while True:
    ret, frame = elemento_captura.read()
    frame = cv2.flip(frame,1)

    frame_pb =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector_faces(frame_pb)

    for face in faces:
        esq, topo = face.left(), face.top()
        dir, base = face.right(), face.bottom()
        cv2.rectangle(frame, (esq,topo), (dir, base),(255,0,0),2)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

elemento_captura.release()
cv2.destroyAllWindows()