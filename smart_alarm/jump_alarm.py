from threading import Thread
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from time import sleep
from pygame import mixer

import cv2
import mediapipe as mp
import numpy as np
from math import acos, degrees

#colors
bg_color = '#ffffff'       #whiete
line_color = '#566FC6'     #blue

#window
window = Tk()
window.title("Smart Alarm")
window.geometry('400x200')
window.configure(bg = bg_color)

#frames
frame_line = Frame(window, width=400, height=5, bg=line_color)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=290, bg=bg_color)
frame_body.grid(row=1, column=0)


#configuring frame body
img1 = Image.open('pose_gray.png')
img2 = Image.open('pose_green.png')

img1.resize((100, 100))
img2.resize((100, 100))

img = ImageTk.PhotoImage(img1)     #gray person
#img = ImageTk.PhotoImage(img2)      #green person

app_img = Label(frame_body, height=100, image=img, bg=bg_color)
app_img.place(x=40, y=75)

#Labels

label_title = Label(frame_body, text="JUMP ALARM", height=1, font=('Ivy 12 bold'), bg=bg_color)
label_title.place(x=215, y=10)

label_goal = Label(frame_body, text="Goal", height=1, font=('Ivy 9 bold'), bg=bg_color)
label_goal.place(x=22, y=15)

label_jumps = Label(frame_body, text="Jumps", height=1, font=('Ivy 9 bold'), bg=bg_color)
label_jumps.place(x=134, y=15)

hour = Label(frame_body, text="hour", height=1, font=('Ivy 7 bold'), bg=bg_color)
hour.place(x=215, y=60)

minute = Label(frame_body, text="min", height=1, font=('Ivy 7 bold'), bg=bg_color)
minute.place(x=255, y=60)

am_pm = Label(frame_body, text="AM / PM", height=1, font=('Ivy 7 bold'), bg=bg_color)
am_pm.place(x=295, y=60)

jumps = StringVar()
jumps.set("0")
current_jumps_label = Label(frame_body, textvariable=jumps, height=1, font=('Ivy 11 bold'), bg=bg_color)
current_jumps_label.place(x=145, y=40)

#Como boxes
c_goal = Combobox(frame_body, width=4, font=('arial 10'))
c_goal['values'] = ("5", "10", "15", "20", "30")
c_goal.current(0)
c_goal.place(x=22, y=40)

c_hour = Combobox(frame_body, width=2, font=('arial 10'))
c_hour['values'] = ("00","01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
c_hour.current(2)
c_hour.place(x=215, y=75)

c_min = Combobox(frame_body, width=2, font=('arial 10'))
c_min['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_min.current(49)
c_min.place(x=255, y=75)

c_am = Combobox(frame_body, width=3, font=('arial 10'))
c_am['values'] = ("AM", "PM")
c_am.current(1)
c_am.place(x=295, y=75)


def activate_alarm():
    t = Thread(target=alarm)
    t.start()

selected = IntVar()

rad1 = Radiobutton(frame_body, font=('arial 12 bold'), value=1, text="Activate", bg=bg_color, command=activate_alarm, variable=selected)
rad1.place(x=230, y=115)

def deactivate_alarm():
    mixer.music.stop()


def sound_alarm():
    mixer.music.load('beep.mp3')
    mixer.music.play()
    selected.set(0)

    mp_drawing = mp.solutions.drawing_utils
    mp_pose = mp.solutions.pose
    cap = cv2.VideoCapture(0)
    reposo = False
    salto = False
    count = 0

    with mp_pose.Pose(static_image_mode=False) as pose:
        while True:
            ret, frame = cap.read()
            if ret == False:
                break
            frame = cv2.flip(frame, 1)
            blur = (15,15)
            frame = cv2.blur(frame, blur)
            height, width, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)
            aux_image = np.zeros(frame.shape, np.uint8)
            output = cv2.addWeighted(frame, 1, aux_image, 0.5, 0)
            if results.pose_landmarks is not None:

                x_24 = int(results.pose_landmarks.landmark[24].x * width)
                y_24 = int(results.pose_landmarks.landmark[24].y * height)
                x_12 = int(results.pose_landmarks.landmark[12].x * width)
                y_12 = int(results.pose_landmarks.landmark[12].y * height)
                x_14 = int(results.pose_landmarks.landmark[14].x * width)
                y_14 = int(results.pose_landmarks.landmark[14].y * height)
                x_23 = int(results.pose_landmarks.landmark[23].x * width)
                y_23 = int(results.pose_landmarks.landmark[23].y * height)
                x_11 = int(results.pose_landmarks.landmark[11].x * width)
                y_11 = int(results.pose_landmarks.landmark[11].y * height)
                x_13 = int(results.pose_landmarks.landmark[13].x * width)
                y_13 = int(results.pose_landmarks.landmark[13].y * height)
                x_25 = int(results.pose_landmarks.landmark[25].x * width)
                y_25 = int(results.pose_landmarks.landmark[25].y * height)
                x_26 = int(results.pose_landmarks.landmark[26].x * width)
                y_26 = int(results.pose_landmarks.landmark[26].y * height)
                
                p24 = np.array([x_24, y_24])
                p12 = np.array([x_12, y_12])
                p14 = np.array([x_14, y_14])
                p23 = np.array([x_23, y_23])
                p11 = np.array([x_11, y_11])
                p13 = np.array([x_13, y_13])
                p25 = np.array([x_25, y_25])
                p26 = np.array([x_26, y_26])

                l1 = np.linalg.norm(p14 - p12)
                l2 = np.linalg.norm(p12 - p24)
                l3 = np.linalg.norm(p24 - p14)
                l4 = np.linalg.norm(p13 - p11)
                l5 = np.linalg.norm(p11 - p23)
                l6 = np.linalg.norm(p23 - p13)
                l7 = np.linalg.norm(p24 - p23)
                l8 = np.linalg.norm(p23 - p25)
                l9 = np.linalg.norm(p24 - p25)
                l10 = np.linalg.norm(p24 - p26)
                l11 = np.linalg.norm(p26 - p23)
                
                # Calcular ángulos
                if y_12 < ((height/2)-20) and y_26 > ((height/2) + 20):
                    img = ImageTk.PhotoImage(img2)      #green person
                    app_img = Label(frame_body, height=100, image=img, bg=bg_color)
                    app_img.place(x=40, y=75)
                    a1 = degrees(acos((l1**2 + l2**2 - l3**2) / (2 * l1 * l2)))          #angle 1
                    a2 = degrees(acos((l4**2 + l5**2 - l6**2) / (2 * l4 * l5)))          #angle 2
                    a3 = degrees(acos((l7**2 + l8**2 - l9**2) / (2 * l7 * l8)))          #angle 3
                    a4 = degrees(acos((l7**2 + l10**2 - l11**2) / (2 * l7 * l10)))        #angle 4

                    if a1 <= 30 and a2 <= 30 and a3 <= 100 and a4 <= 100:
                            reposo = True
                    if reposo == True and salto == False and a1 >= 120 and a2 >= 120 and a3 >= 100 and a4 >= 100:
                            salto = True
                    if reposo == True and salto == True and a1 <= 30 and a2 <= 30 and a3 <= 100 and a4 <= 100:
                            count += 1
                            jumps.set(str(count))
                            reposo = False
                            salto = False

                    cv2.line(aux_image, (x_14, y_14), (x_12, y_12), (255, 255, 0), 13)
                    cv2.line(aux_image, (x_12, y_12), (x_24, y_24), (255, 255, 0), 13)
                    cv2.line(aux_image, (x_14, y_14), (x_24, y_24), (255, 255, 0), 5, cv2.LINE_AA)
                    cv2.line(aux_image, (x_13, y_13), (x_11, y_11), (255, 255, 0), 13)
                    cv2.line(aux_image, (x_11, y_11), (x_23, y_23), (255, 255, 0), 13)
                    cv2.line(aux_image, (x_13, y_13), (x_23, y_23), (255, 255, 0), 5, cv2.LINE_AA)
                    cv2.line(aux_image, (x_24, y_24), (x_23, y_23), (255, 255, 0), 13)
                    cv2.line(aux_image, (x_23, y_23), (x_25, y_25), (255, 255, 0), 13)
                    cv2.line(aux_image, (x_25, y_25), (x_24, y_24), (255, 255, 0), 5, cv2.LINE_AA)
                    cv2.line(aux_image, (x_24, y_24), (x_26, y_26), (255, 255, 0), 13)
                    cv2.line(aux_image, (x_26, y_26), (x_23, y_23), (255, 255, 0), 5, cv2.LINE_AA)

                    contours_1 = np.array([[x_14, y_14], [x_12, y_12], [x_24, y_24]])
                    contours_2 = np.array([[x_13, y_13], [x_11, y_11], [x_23, y_23]])
                    contours_3 = np.array([[x_24, y_24], [x_23, y_23], [x_25, y_25]])
                    contours_4 = np.array([[x_24, y_24], [x_26, y_26], [x_23, y_23]])

                    cv2.fillPoly(aux_image, pts=[contours_1], color=(128, 0, 250))
                    cv2.fillPoly(aux_image, pts=[contours_2], color=(128, 0, 250))
                    cv2.fillPoly(aux_image, pts=[contours_3], color=(128, 0, 250))
                    cv2.fillPoly(aux_image, pts=[contours_4], color=(128, 0, 250))
                    output = cv2.addWeighted(frame, 1, aux_image, 0.5, 0)

                    cv2.circle(output, (x_24, y_24), 4, (0, 255, 255), 4)
                    cv2.circle(output, (x_12, y_12), 4, (0, 255, 255), 4)
                    cv2.circle(output, (x_14, y_14), 4, (0, 255, 255), 4)
                    cv2.circle(output, (x_11, y_11), 4, (0, 255, 255), 4)
                    cv2.circle(output, (x_13, y_13), 4, (0, 255, 255), 4)
                    cv2.circle(output, (x_25, y_25), 4, (0, 255, 255), 4)
                    cv2.circle(output, (x_26, y_26), 4, (0, 255, 255), 4)
                    cv2.circle(output, (x_23, y_23), 4, (0, 255, 255), 4)

                    #cv2.rectangle(output, (0, 0), (60, 60), (255, 255, 0), -1)
                    cv2.putText(output, str(int(a1)), (x_12 - 30, y_12 + 30), 1, 1, (3, 221, 243), 2)
                    cv2.putText(output, str(int(a2)), (x_11 + 30, y_11 + 30), 1, 1, (3, 221, 243), 2)
                    cv2.putText(output, str(int(a3)), (x_23 - 27, y_23 + 25), 1, 1, (3, 221, 243), 2)
                    cv2.putText(output, str(int(a4)), (x_24 + 10, y_24 + 25), 1, 1, (3, 221, 243), 2)
                else:
                     img = ImageTk.PhotoImage(img1)     #gray person
                     app_img = Label(frame_body, height=100, image=img, bg=bg_color)
                     app_img.place(x=40, y=75)

            cv2.putText(output, str(count), (10, 50), 1, 3.5, (0, 250, 250), 2)

            if count == int(c_goal.get()):
                selected.set(2)
                deactivate_alarm()
                jumps.set("0")
                break
            
            cv2.imshow("output", output)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        cap.release()
        cv2.destroyAllWindows()


def alarm():
    while True:
        control = selected.get()
        alarm_hour = c_hour.get()
        alarm_min = c_min.get()
        alarm_sec = '00'
        alarm_period = c_am.get()
        alarm_period = str(alarm_period).upper()
        now = datetime.now()
        current_hour = now.strftime("%I")
        current_min = now.strftime("%M")
        current_sec = now.strftime("%S")
        current_period = now.strftime("%p")

        img = ImageTk.PhotoImage(img1)     #gray person
        app_img = Label(frame_body, height=100, image=img, bg=bg_color)
        app_img.place(x=40, y=75)
        
        if control == 1 and alarm_period == current_period and alarm_hour == current_hour and alarm_min == current_min and alarm_sec == current_sec:
           sound_alarm()
        sleep(1)

mixer.init()
window.mainloop()