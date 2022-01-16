
import PySimpleGUI as sg
import cv2
import numpy as np
from time import time


# define color theme / カラーテーマの設定
sg.theme('Black')

# define elements / エレメント（GUIのパーツ）の設定
title_el = sg.Text('Camera View', size=(40, 1), justification='center', font='Helvetica 20',key='-status-')
camera_el = sg.Image(filename='', key='image')
snapshot_button_el = sg.Button("Snapshot", key="-SNAPSHOT-",  size=(10, 1), font='Helvetica 14')
exit_button_el = sg.Button("Exit", key="-CLOSE-", size=(10, 1), font='Helvetica 14')
fps_text_el = sg.Text("FPS: ", font='Helvetica 14')
fps_input_el = sg.Input(key="-FPS-",size=(10, 1), font='Helvetica 14')

# define window layout / ウィンドウレイアウトの設定
layout = [[title_el],
          [camera_el],
          [snapshot_button_el, exit_button_el, fps_text_el, fps_input_el]]

# create window / ウィンドウの生成
window = sg.Window('Camera GUI Demo',
                    layout, location=(800, 400))


# video capture setting, カメラの設定
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW) #1

t_old = time()

while True:
    
    # refresh window / ウィンドウの更新
    event, values = window.read(timeout=20) 

    t_new = time()
    dt = t_new - t_old
    fps = 1/dt
    t_old = t_new

    ret, frame = cap.read()
    if ret is True:
        imgbytes = cv2.imencode('.png', frame)[1].tobytes() 
        window['image'].update(data=imgbytes)
        window["-FPS-"].update(f"{fps:.1f}")

    if event == "-SNAPSHOT-":
      cv2.imwrite("snapshot.jpg", frame)

    if event == "-CLOSE-":
      cap.release() #2
      cv2.destroyAllWindows()
      window.close()
      break

    if event == sg.WIN_CLOSED:
      break

cap.release() #2
cv2.destroyAllWindows()
window.close()

